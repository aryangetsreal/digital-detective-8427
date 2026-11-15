# Mission 03 - Understand the operating system

Status: Completed.

## 1. Task / objective

Explore macOS, running processes, storage, paths and file permissions. Explain the main responsibilities of an operating system.

## 2. Work completed

The commands were executed in my Mac's terminal environment using the coding assistant. The results below come from that run. Private paths and account names are redacted in the evidence.

### Task 3.1 - Explore your operating system

| Information explored | What it tells you | Actual observation |
| --- | --- | --- |
| Operating system / system details | Identifies the operating system, version and architecture. | `sw_vers` reported macOS `27.0`, build `26A428`. `uname -m` reported `arm64`. |
| Current account identity | Shows the account running the command. | `id -un` returned the active account name. It is recorded as `[redacted]`. |
| Available and used storage | Shows space on the filesystem containing this project. | `df -h .` reported `926Gi` total, `125Gi` used, `773Gi` available and `14%` capacity used on `/System/Volumes/Data`. |
| System activity snapshot | Shows a brief view of processes and CPU activity. | `top -l 1 -n 0` reported 571 processes: 2 running and 569 sleeping. CPU usage was 6.27% user, 11.56% system and 82.15% idle. |

The storage figures describe the project's filesystem, not the space used by the project folder. They are rounded values reported by `df`; total, used and available need not add up directly because of filesystem accounting and reserved space.

The process count, free space and CPU usage are snapshots. They can change while programs run. The account check identifies who is running the commands; the actual name is not needed in a public report.

### Task 3.2 - Understand processes

The assistant opened this project in VS Code with `open -a "Visual Studio Code" .`, then inspected processes using `ps -axo pid,comm`.

Selected results from the process list:

| PID | Process name | What it represents |
| --- | --- | --- |
| 1 | launchd | A background process that starts and manages services. |
| 401 | WindowServer | A system process that helps display application windows. |
| 691 | Finder | The application used to browse and manage files. |
| 26743 | Terminal | The Terminal application. |
| 41547 | Code | The VS Code text editor. |
| 42522 | Safari | The Safari browser. |

A **process** is a program that is running. A **PID** is the number the operating system uses to identify a process while it exists. The `ps` command displays process information; this command selected the PID and executable-name columns.

The process list included applications such as Code and Safari, along with background processes such as launchd. These are examples actually found during the check. macOS schedules CPU time for processes and manages the memory and resources they use.

Only selected PID/name rows are saved. Executable directory paths were removed, and command arguments were not requested. No processes were terminated.

### Task 3.3 - Understand paths and permissions

#### Paths

The assistant navigated between the project folder and its Mission 3 subfolder.

| Working location | Commands executed | Actual result, with private paths redacted |
| --- | --- | --- |
| Project root | `pwd` | `[PROJECT]` |
| Project root | `cd mission-03-operating-system`, then `pwd` | `[PROJECT]/mission-03-operating-system` |
| Mission 3 folder | `cd ..`, then `pwd` | `[PROJECT]` |

`[PROJECT]` stands for the full absolute project path printed by `pwd`. It is a redaction label, not text to type into the shell.

- An **absolute path** starts at `/` and gives the full location. A redacted example from this project is `/[redacted]/digital-detective-8427/mission-03-operating-system/README.md`.
- A **relative path** starts from the current directory. From the project root, `mission-03-operating-system/README.md` points to this file.
- The **parent directory** is one level above the current directory. `cd ..` moved from the mission folder back to the project root.
- The **home directory** is the current user's personal folder. `~` is shell shorthand for it. No private home-folder contents were explored.
- The **current working directory** is where relative paths are resolved. `pwd` displays it.

The assistant created an empty `.hidden-example` file inside the practice directory. `ls` showed only `permissions-example.txt`. `ls -la` also showed `.hidden-example`, `.` and `..`. Names beginning with a dot are normally hidden by `ls`; `-a` includes them. The `-l` option adds details.

#### File permissions

The new practice file is [permissions-example.txt](practice/permissions-example.txt). Its contents are `Mission 3 permission practice.`

Command run inside `practice/`:

```sh
ls -l permissions-example.txt
```

Actual output, with owner and group redacted:

```text
-rw-r--r--@ 1 [redacted]  [redacted]  31 Nov 15 19:22 permissions-example.txt
```

The first `-` identifies a regular file. The next nine permission positions are grouped into owner, group and others: `rw-`, `r--`, `r--`.

| Permission | Meaning | Owner's result for this file |
| --- | --- | --- |
| Read (`r`) | Allows the file's contents to be read. | Allowed. |
| Write (`w`) | Allows the file to be changed. | Allowed. |
| Execute (`x`) | Allows a file to be run when it is a valid program or script. For a directory, it allows access/traversal. | Not allowed; the third owner position is `-`. |

The **owner** has `rw-`, so the owner can read and write the file but cannot execute it. The **group** has `r--`, and **others** have `r--`, so both can read it but do not have write or execute permission through these permission bits.

Permissions were inspected only. The PDF does not require changing them or explaining numeric notation, so no `chmod` command was run.

### Task 3.4 - Operating-system responsibilities

The table explains OS responsibilities using examples. The run directly showed processes, shell commands, file creation, navigation and permission bits. Memory allocation, device handling and permission-denial behavior were not experimentally tested.

| OS responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Shares CPU time between running processes and manages their execution. | Lets VS Code and Safari run at the same time. |
| Memory management | Gives processes memory and tracks how it is used. | Provides working memory for an open document. |
| Device management | Helps programs use devices through system services and drivers. | Handles keyboard input and sends output to the display. |
| File management | Organizes files and folders and manages access to stored data. | Saves a file and finds it again by its path. |
| User interface / shell | Provides ways to interact with the computer through windows or commands. | Finder provides a graphical interface; a shell runs commands through Terminal. |
| Security and permissions | Controls access to files and system resources. | Checks whether a process is allowed to write to a file. |

## 3. Commands / tools used

| Command / tool | Purpose |
| --- | --- |
| `sw_vers` | Checked the actual macOS name, version and build. |
| `uname -m` | Checked processor architecture. |
| `id -un` | Identified the active account; the output is redacted. |
| `df -h .` | Checked storage for the filesystem containing this project. |
| `top -l 1 -n 0` | Collected one system activity snapshot without individual process rows. |
| `open -a "Visual Studio Code" .` | Opened the project in a text editor before checking processes. |
| `ps -axo pid,comm` | Listed process IDs and executable names; only selected names and PIDs were preserved. |
| `pwd`, `cd`, `cd ..` | Checked the location and navigated between the project and mission folder. |
| `mkdir practice` | Created the isolated practice folder. |
| `printf` with `>` | Wrote one line to a new practice file. |
| `touch .hidden-example` | Created an empty hidden file for the listing comparison. |
| `ls`, `ls -la`, `ls -l permissions-example.txt` | Compared listings and inspected the practice file's permissions. |
| Python and macOS zsh | Ran commands, saved selected redacted outputs and checked results through the assistant. |
| Swift, PDFKit and Vision | Read the exact Mission 3 pages from the scanned assignment PDF using OCR. |

## 4. My understanding

I learned that the operating system manages the programs and files on my computer. Using ps and top, I could see different processes running, each with its own PID. I also understood how file paths help us locate files and how permissions decide whether a file can be read, written or executed. The practical commands helped me understand these concepts better.

## 5. Difficulties faced

No personal difficulties. All commands run by the assistant for this mission succeeded.

## 6. How I resolved them

Not applicable. No personal difficulties or assistant command errors needed a resolution.

## 7. Evidence / files

- [Command transcript](evidence/terminal-session.txt): commands, exit statuses, selected actual outputs and redacted details.
- [Permission practice file](practice/permissions-example.txt): the new file inspected in Task 3.3.
- [Hidden practice file](practice/.hidden-example): the empty file used to compare listings.
- [This README](README.md): task tables, results and explanations.

The transcript includes the four relevant `top` summary lines and selected `ps` rows. No screenshots were required or created.

## 8. Evidence / links

- [Project overview](../README.md).
- [Local command evidence](evidence/terminal-session.txt).
- [Mission 3 commit history](https://github.com/aryangetsreal/digital-detective-8427/commits/main/mission-03-operating-system/README.md).

## 9. Commit details

- Commit message: `Complete operating system exploration mission`.
- Scope: Mission 3 documentation, evidence and practice files, plus the approved root Mission 3 status update.
- Branch: `main`.
- Publishing: authorized for the approved files on `origin/main`.
- The actual commit hash and verified push result will be recorded in the completion report after publishing. The commit can also be found through the mission history link above.

Verification compares the local and remote hashes, checks the public repository and published README, and confirms a clean working tree.
