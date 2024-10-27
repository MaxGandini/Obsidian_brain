[[Bash]]
Bash piping is done by using the operator "|" , you can take the output of one program and put it inside the input of another program. This is very useful for scripting>
```
- dmenu (it's an application that takes the input you give it and gives it as a menu)
- Zathura (it's a text file gui viewer and what is important, is that it accepts stdin with its API)
 - man -k lattex (this gets all the manuals that takes all the hits for lattex)
 - man -k . (lists all the manuals on our system. For my arch distro it was necessary to run sudo mandb to update the database of manuals.)
 - man -k . | dmenu (this pipes all the manuals found into dmenu)
 - man -Tpdf ls (Is a way of making man print to STDoutput the list in a pdf format)
 - man -Tpdf ls | zathura - (Pipes the STDoutput of man to the STDIN of zathura. The way the stdin is accessed is with the -key)
```
 This achieves getting the whole manual in a pdf format. It's not like you are accesing a PDF in your computer, you are actually creating a pdf using the pipe and the programs APIS. 
 Let's make another example:
 - man -k . | dmenu -l 30 | awk '{print $1}' | xargs -r man -Tpdf | zathura - 
It's a complicated example of piping:
awk and xargs are powerful command-line tools often used in Unix-like operating systems for text processing and command execution. Here’s a brief overview of each:

awk
Purpose: awk is a programming language and utility designed for pattern scanning and processing. It's especially useful for working with structured text files (like CSVs or tab-delimited data).

Functionality:

You can use awk to read input line by line and perform actions based on patterns.
It allows for field-based processing, meaning you can easily extract and manipulate specific columns from text data.
Basic Usage:
```bash
Copy code
awk '{print $1}' filename
```

This command prints the first column of filename. Fields are separated by whitespace by default.

Common Features:

Supports variables, loops, and conditionals.
Can perform calculations and string manipulation.
xargs
Purpose: xargs is a command that builds and executes command lines from standard input. It's particularly useful for handling output from other commands, especially when that output consists of filenames or arguments.

Functionality:

xargs takes the output from one command and uses it as input for another command.
It can be used to avoid issues with command-line length limits.
Basic Usage:

```bash
find . -name "*.txt" | xargs cat
```
This command finds all .txt files in the current directory and its subdirectories and then uses xargs to pass them to cat, which concatenates their content.

Common Features:

You can use -n to specify how many arguments to pass to the command.
Supports options for handling spaces and special characters in filenames.
Example Usage
A common combination of these tools could look like this:

```bash
ls | awk '{print $1}' | xargs rm
```

This command lists files, extracts the first column (filenames), and deletes them.


