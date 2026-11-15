# Mission 02 - Become comfortable with the Terminal

Status: Completed.

## 1. Task / objective

Use Terminal commands to navigate folders, create and manage files, compare listing options, pass output through a pipe, and inspect Homebrew without installing or removing software.

## 2. Work completed

The coding assistant ran the commands below in the actual macOS zsh environment inside this repository. These are results from that run, rather than a claim that I manually typed every command. Practice files are isolated in `mission-02-terminal/terminal-practice/`.

### Task 2.1 - Basic Terminal operations

The command table records the actual results and explains what each operation means. `[PROJECT]` replaces the private absolute project path in the evidence.

| Operation / command used | Purpose | Actual observed result | What the operation means |
| --- | --- | --- | --- |
| `pwd` | Display the current directory. | Printed the project path, recorded as `[PROJECT]`. | It shows where commands are currently working. |
| `ls` | List the current directory. | The initial mission folder listing contained `README.md`. | A listing helps find files and check whether a change worked. |
| `ls -l` | Show a detailed listing. | Displayed the README with permissions, owner/group, size and modification time; owner/group are redacted in the evidence. | The long format provides more information than file names alone. |
| `cd terminal-practice` followed by `pwd` | Enter the practice folder and check the location. | Printed `[PROJECT]/mission-02-terminal/terminal-practice`. | `cd` changes the working directory for subsequent commands in that shell. |
| `cd ..` followed by `pwd` | Move to the parent directory and check the location. | Printed `[PROJECT]/mission-02-terminal`. | `..` refers to the parent folder. This navigation stayed inside the repository. |
| `mkdir terminal-practice` | Create the practice directory from the mission folder. | `ls -d terminal-practice` printed `terminal-practice`. | A directory keeps related practice files together. |
| `touch original.txt` | Create an empty practice file. | `ls -l original.txt` showed a size of zero bytes. | `touch` creates a file when it does not exist; for an existing file it updates timestamps without clearing its contents. |
| `cp original.txt copied.txt` | Copy the file. | A listing showed both `copied.txt` and `original.txt`. | Copying leaves the original and makes another file. |
| `mv copied.txt renamed.txt` | Rename the copy. | The listing showed `renamed.txt` and `original.txt`; `copied.txt` no longer existed. | Moving changes a file's location or name. |
| `cat original.txt` | Display the file contents. | Initially printed no text because the file was empty. | `cat` sends file contents to the terminal output. |

No files were deleted. Tasks 2.1–2.2 in the PDF do not require a deletion exercise, so `rm` was not executed. It would require separate approval with an exact target.

### Task 2.2 - Safe file changes

The following commands ran in `terminal-practice/`. Only the new practice file was written to.

| Command used | Actual result |
| --- | --- |
| `printf '%s\n' 'First practice line.' > original.txt` | Wrote the first line. `cat original.txt` displayed `First practice line.` |
| `printf '%s\n' 'Second practice line.' >> original.txt` | Added the second line. `cat original.txt` displayed both lines in order. |
| `cp original.txt backup.txt` | Created a backup; a listing showed both file names. |
| `mv backup.txt backup-renamed.txt` | Renamed the backup. The old backup name no longer existed. |
| `cat backup-renamed.txt` | Displayed the same two lines as the original; their contents were also checked for equality. |

Actual final contents of both `original.txt` and `backup-renamed.txt`:

```text
First practice line.
Second practice line.
```

`>` creates a file or replaces its existing contents. `>>` creates a file if needed or adds text to the end without removing earlier contents. In this run, the first command wrote to an empty file and the second preserved the first line while adding another.

Copying makes a separate file while keeping the original. Moving changes a name or location; the previous name is no longer present after a successful rename. `pwd` identifies the current working directory, while `ls` helps inspect its contents and verify file operations.

### Task 2.3 - Options and pipes

An empty hidden practice file was created using `touch .listing-example` so the effect of `-a` could be observed.

| Command used | Actual observed result | Meaning of the option |
| --- | --- | --- |
| `ls` | Listed `backup-renamed.txt`, `original.txt` and `renamed.txt`; omitted the hidden file. | A normal listing shows visible entries. |
| `ls -l` | Added details; the original and backup were 43 bytes and the renamed empty file was zero bytes. | `-l` selects the long format. |
| `ls -la` | Also displayed `.`, `..` and `.listing-example`. | `-a` includes names beginning with a dot. |
| `ls -lah` | Included hidden entries and displayed sizes such as `43B` and `0B`. | `-h` formats sizes in human-readable units; larger sizes can use units such as K or M. |

The pipe command executed was:

```sh
ls -lah | head -n 4
```

Actual output, with owner/group information redacted:

```text
total 16
drwxr-xr-x@ 6 [redacted]  [redacted]   192B Nov 15 18:47 .
drwxr-xr-x@ 4 [redacted]  [redacted]   128B Nov 15 18:47 ..
-rw-r--r--@ 1 [redacted]  [redacted]     0B Nov 15 18:47 .listing-example
```

The pipe symbol `|` connects the standard output of the left command to the standard input of the right command. Here, `ls -lah` produces a detailed listing and `head -n 4` displays its first four lines. The `total` line counts as one line, so the result is not four file names. The complete captured output is in the transcript.

These listings were captured during the practice run. Later evidence and README edits can change the parent folder's size or time, so a new listing may differ.

### Task 2.4 - Package managers

| Command used | Actual observed result |
| --- | --- |
| `command -v brew` | Found Homebrew at `/opt/homebrew/bin/brew`. |
| `brew --version` | Printed `Homebrew 7.0.13`. |
| `brew list --versions` | Listed installed packages and versions, including `gh 2.97.0`, `htop 3.5.3` and `python@3.12 3.12.15`. The full list is preserved in the transcript. |

A package manager helps install, update and remove software while tracking the packages it manages. When asked to install software, it obtains the package and any required dependencies; an upgrade installs a newer available version. This saves users from managing every download and dependency separately.

Only read-only checks were run. No package was installed, updated or removed. Homebrew auto-update and analytics were disabled for these checks. The Python version listed by Homebrew describes that managed package; it does not establish which Python interpreter every shell command uses.

## 3. Commands / tools used

- macOS zsh shell: ran the practice commands through the coding assistant.
- `pwd`, `ls`, `cd`: checked locations and directory contents.
- `mkdir`, `touch`, `cp`, `mv`, `cat`: created and verified practice directories and files, copied files, renamed files and displayed their contents.
- `printf`, `>` and `>>`: wrote and appended the two practice lines.
- `ls -l`, `ls -la`, `ls -lah`: compared detailed, hidden-entry and human-readable-size listings.
- `head -n 4` and `|`: selected the first four lines from the listing output.
- `command -v brew`, `brew --version`, `brew list --versions`: checked Homebrew and its installed packages without making package changes.
- Python: the assistant used it to run commands, check results and save a redacted transcript.
- Git: used to check the working tree and review changes. The approved publishing steps use explicit file staging, a dedicated mission commit and a push to `main`.

## 4. My understanding

Terminal commands act in a working directory, so checking the current location helps avoid changing the wrong files. Creating, copying and renaming files have different effects, and command output can be checked to confirm the result. Options change a command's behavior, while a pipe lets one command process another command's output. A package manager makes installed software and its dependencies easier to manage.

This explanation reflects my understanding. The practice commands were run by the coding assistant in the macOS shell, as recorded above.

## 5. Difficulties faced

The assistant's first Python transcript helper failed before any practice commands ran. Python 3.9 reported `SyntaxError: f-string expression part cannot include a backslash` because the helper put newline-containing fallback strings inside an f-string expression.

All subsequent practice and Homebrew commands completed successfully. I have no personal difficulty to add.

## 6. How I resolved them

The assistant corrected the helper by preparing the output strings before formatting the transcript block. The corrected helper then ran the commands, checked the results and saved the evidence. This was an assistant tooling issue, rather than an invented personal experience.

## 7. Evidence / files

- [Actual command transcript](evidence/terminal-session.txt): executed commands, working directories, exit statuses, standard output and error output. Private paths and owner/group names are redacted.
- [Original practice file](terminal-practice/original.txt): contains the two lines.
- [Renamed backup](terminal-practice/backup-renamed.txt): matches the original contents.
- [Renamed empty copy](terminal-practice/renamed.txt): retained from Task 2.1.
- [Hidden listing example](terminal-practice/.listing-example): empty file used to demonstrate `ls -a`.

No screenshots were created. The transcript preserves the actual run; it does not claim that its historical directory listing is the current listing after documentation edits.

## 8. Evidence / links

- [Project overview](../README.md).
- [This mission README](README.md).
- [Mission 2 commit history](https://github.com/aryangetsreal/digital-detective-8427/commits/main/mission-02-terminal/README.md).

## 9. Commit details

- Commit message: `Complete terminal basics and file operations`.
- Scope: Mission 2 README, practice files and transcript, plus the approved root README mission-status corrections.
- Branch: `main`.
- Commit hash: `726446883ca63d93fbaa70b7d23453f1b83a7223`.
- Push status: Verified on GitHub `main`; the published commit and files were checked during the final review.
- [Published commit](https://github.com/aryangetsreal/digital-detective-8427/commit/726446883ca63d93fbaa70b7d23453f1b83a7223).

Verification compares the local and remote hashes, checks public visibility and the published README, and confirms a clean working tree before reporting success.
