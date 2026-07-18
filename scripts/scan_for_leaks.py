#!/usr/bin/env python3
"""Scan tracked/staged files for personal info and secrets before they go public.

Usage:
    scan_for_leaks.py --staged   (default) scan what's about to be committed
    scan_for_leaks.py --all      scan every tracked file (full audit)

Exit code 1 and a report on any hit, 0 if clean. Stdlib only, no dependencies,
so it runs on any machine with Python 3 (desktop, laptop, CI) without an
install step.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
)

ALLOWLIST_FILE = REPO_ROOT / ".leakscan-allowlist"

# Real personal emails that have shown up in this vault before — always flagged.
KNOWN_PERSONAL_EMAILS = {
    "maximiliano.gandini.27@gmail.com",
    "maximiliano.gandini.manfreda@gmail.com",
}

# Local machine usernames whose presence in an absolute path leaks machine info.
LOCAL_USERNAMES = {"Xilligan", "Xilian"}

PLACEHOLDER_EMAIL_DOMAINS = {
    "example.com", "example.org", "example.net",
    "contoso.com", "test.com", "proxy.server.com", "yourdomain.com",
}

# IPs/ranges commonly used as generic teaching examples in this vault.
IP_ALLOWLIST_PREFIXES = (
    "127.", "0.0.0.0", "255.255.255.255",
    "192.168.0.", "192.168.1.",
    "10.0.0.1", "192.0.2.", "198.51.100.", "203.0.113.",
)

PLACEHOLDER_MARKERS = (
    "your", "example", "xxx", "<", "changeme", "insert", "here",
    "placeholder", "todo", "dummy", "fake",
    "ollama",  # conventional dummy api_key value for local Ollama servers
)

# This file itself references the patterns above as literal example strings,
# not vault content — scanning it would just self-flag its own detection data.
SKIP_FILES = {"scripts/scan_for_leaks.py"}

# Directories/extensions holding third-party or binary content — not worth scanning.
SKIP_DIR_PREFIXES = (".obsidian/plugins/", ".git/")
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".pdf", ".zip",
    ".ttf", ".woff", ".woff2", ".eot", ".mp3", ".mp4", ".mov", ".webm",
    ".bin", ".exe",
}

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_OCTET = r"(?:25[0-5]|2[0-4]\d|1?\d?\d)"
IPV4_RE = re.compile(r"(?<![\w./])" + _OCTET + r"(?:\." + _OCTET + r"){3}(?!\.?\d)")
# A JSON line whose entire value is a dotted version number, e.g.
# "nvidia-cublas-cu12": "12.6.1.4" — package version dumps, not IPs.
JSON_VERSION_LINE_RE = re.compile(r'^\s*"[^"]+"\s*:\s*"[\d.]+",?\s*$')
PEM_RE = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
PHONE_RE = re.compile(
    r"(?i)\b(?:phone|tel|cell|mobile|whatsapp)\s*[:=]?\s*"
    r"([+]?[\d][\d\-.\s]{7,}\d)"
)

SECRET_PATTERNS = [
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub Token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("GitHub Fine-grained PAT", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("Slack Token", re.compile(r"xox[baprs]-[A-Za-z0-9-]+")),
    ("Google API Key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Bearer Token", re.compile(r"Bearer\s+[A-Za-z0-9\-._~+/]{20,}")),
    (
        "Password/API key assignment",
        re.compile(
            r"(?i)(password|passwd|pwd|api[_-]?key|secret|token)\s*[:=]\s*"
            r"['\"]([^'\"]{6,})['\"]"
        ),
    ),
]


def load_allowlist():
    patterns = []
    if ALLOWLIST_FILE.exists():
        for line in ALLOWLIST_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            patterns.append(re.compile(line))
    return patterns


def is_allowlisted(text, allow_patterns):
    return any(p.search(text) for p in allow_patterns)


def should_skip(path_str):
    if path_str in SKIP_FILES:
        return True
    if any(path_str.startswith(p) for p in SKIP_DIR_PREFIXES):
        return True
    if Path(path_str).suffix.lower() in SKIP_EXTENSIONS:
        return True
    return False


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout


def staged_files():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACM")
    return [f for f in out.splitlines() if f]


def all_files():
    out = git("ls-files")
    return [f for f in out.splitlines() if f]


def read_staged(path_str):
    try:
        return git("show", f":{path_str}")
    except subprocess.CalledProcessError:
        return None


def read_worktree(path_str):
    p = REPO_ROOT / path_str
    try:
        return p.read_text(errors="strict")
    except (UnicodeDecodeError, OSError):
        return None


def notebook_source_only(text):
    """Reduce a Jupyter notebook to just its human-authored cell source.

    Cell outputs (pip freeze dumps, library banners, execution results) are
    full of dotted-version-number noise that looks like IPv4 addresses but
    isn't authored content, so they're excluded from scanning.
    """
    try:
        nb = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return text
    lines = []
    for cell in nb.get("cells", []):
        source = cell.get("source", "")
        if isinstance(source, list):
            lines.append("".join(source))
        else:
            lines.append(source)
    return "\n".join(lines)


def mask(value):
    if len(value) <= 8:
        return "*" * len(value)
    return f"{value[:4]}...{value[-4:]}"


def scan_text(path_str, text, allow_patterns):
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if is_allowlisted(line, allow_patterns):
            continue

        for email in EMAIL_RE.findall(line):
            if email in KNOWN_PERSONAL_EMAILS:
                findings.append((lineno, "Known personal email", email))
                continue
            domain = email.split("@", 1)[1].lower()
            if domain in PLACEHOLDER_EMAIL_DOMAINS:
                continue
            findings.append((lineno, "Email address", email))

        for name, pattern in SECRET_PATTERNS:
            for m in pattern.finditer(line):
                value = m.group(2) if m.groups() and len(m.groups()) > 1 else m.group(0)
                if any(marker in value.lower() for marker in PLACEHOLDER_MARKERS):
                    continue
                findings.append((lineno, name, mask(value)))

        if PEM_RE.search(line):
            findings.append((lineno, "Private key header", "-----BEGIN ... PRIVATE KEY-----"))

        if not JSON_VERSION_LINE_RE.match(line):
            for ip in IPV4_RE.findall(line):
                if ip.startswith(IP_ALLOWLIST_PREFIXES):
                    continue
                findings.append((lineno, "IPv4 address", ip))

        for username in LOCAL_USERNAMES:
            if f"/home/{username}" in line or f"/Users/{username}" in line:
                findings.append((lineno, "Local machine path/username", f"~{username}"))

        phone_match = PHONE_RE.search(line)
        if phone_match:
            findings.append((lineno, "Phone number", mask(phone_match.group(1))))

    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--staged", action="store_true", help="scan staged changes (default)")
    mode.add_argument("--all", action="store_true", help="scan every tracked file")
    args = parser.parse_args()

    allow_patterns = load_allowlist()

    if args.all:
        files = all_files()
        reader = read_worktree
    else:
        files = staged_files()
        reader = read_staged

    total_findings = 0
    for path_str in files:
        if should_skip(path_str):
            continue
        text = reader(path_str)
        if text is None:
            continue
        if path_str.endswith(".ipynb"):
            text = notebook_source_only(text)
        findings = scan_text(path_str, text, allow_patterns)
        for lineno, category, value in findings:
            print(f"{path_str}:{lineno}: [{category}] {value}")
            total_findings += 1

    if total_findings:
        print(
            f"\n{total_findings} potential leak(s) found. Fix the content, or if this "
            f"is a false positive add a regex line to .leakscan-allowlist explaining why.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
