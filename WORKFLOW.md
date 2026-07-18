# Workflow: publishing safely

This vault is a **public** GitHub repo. The `obsidian-git` plugin auto-commits
changes roughly every 90 seconds and auto-pushes them — there is no manual
review step in between. That means anything typed into a note can go public
within minutes. This document is the checklist and rulebook for keeping
personal and work information out of it.

## Never commit

- **Real emails, phone numbers, or addresses.** Use placeholders in any
  code/config example: `john.doe@example.com`, `you@example.com` — matching
  the style already used in `Requests and Responses.md` and
  `Git-basic-comm.md`.
- **Real company, client, or employer names**, internal project codenames,
  internal URLs or hostnames.
- **API keys, tokens, passwords, private keys, connection strings** — even in
  "throwaway" examples. Use obvious placeholders like `your-key-here`.
- **Screenshots or pasted terminal output** containing any of the above.
- **Local machine details** — absolute paths containing your username,
  local hostnames. This is why `.obsidian/workspace.json` and
  `.obsidian/plugins/obsidian-git/data.json` are gitignored: they're
  per-machine state, not vault content, and they leaked a local path in the
  past.

## One-time setup, per device

Git hooks aren't versioned by default, so enable the repo's hook path once
per clone/device:

```
git config core.hooksPath .githooks
```

## Before every manual publish

Just commit — the pre-commit hook runs the scanner automatically
(`scripts/scan_for_leaks.py --staged`) and blocks the commit if it finds
something. You can also run it by hand at any time:

```
python3 scripts/scan_for_leaks.py --staged
```

## Full audit

To sweep every tracked file (not just what's staged), e.g. after adding this
workflow or periodically:

```
python3 scripts/scan_for_leaks.py --all
```

## If the scanner blocks a commit

Fix the content — don't bypass it with `git commit --no-verify`. If it's a
genuine false positive (e.g. a new placeholder pattern), add a regex line to
`.leakscan-allowlist` with a comment explaining why, rather than skipping the
check.

## If something sensitive already got pushed

Stop. Don't force-push or rewrite history yourself — flag it and get
confirmation first. Rewriting history on a public repo is a shared-state,
hard-to-reverse action, and simply deleting the file in a new commit does
**not** remove it from earlier commits still visible in the repo's history.

## Branch policy

Keep a single long-lived branch: `master`. Don't create parallel
`main`/`main_`/`desk_main`-style branches again — those existed only because
`obsidian-git` was pushing from multiple devices without a shared branch
config. If you use `obsidian-git` on more than one device, make sure each one
is configured to push to `master`.

## Note on auto-push

Because commits can be created and pushed automatically within ~90 seconds of
a save, the pre-commit hook is the real safety net, not this checklist — this
document is a backup for anyone committing manually, and the reference for
what the hook is actually checking for.
