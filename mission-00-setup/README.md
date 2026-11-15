# Mission 00 - Create your GitHub workspace

Status: Complete. The public repository, setup commit and pushed files were verified on GitHub.

## 1. Task / objective

Prepare a repository named `digital-detective-8427`, create the required folders and README files, check the setup tools, and publish the setup to a public GitHub repository. The student confirmed that 8427 matches the last four USN digits.

## 2. Work completed

- Inspected the existing project folder; it was empty. The folder already had the correct repository name, so it did not need to be created again.
- Read all 12 pages of the scanned assignment using macOS OCR, including the Mission 0 instructions, README format and mandatory commit rules.
- Created the root README, all nine mission folders and their READMEs.
- Added the required empty `mission-05-numbers-data/number_converter.py` scaffold. No converter code or other later mission work was written.
- Created `evidence/` with `.gitkeep` and added `.gitignore` to exclude common local files.
- Checked Git, Python and VS Code versions, initialized Git on `main`, and verified GitHub CLI authentication for `aryangetsreal`.
- Confirmed that GitHub could not find `aryangetsreal/digital-detective-8427` at the time of the check. The public repository was then created with approval and the setup commit was pushed.

Opened the project folder in Terminal and VS Code using macOS `open`; both commands succeeded. No screenshot or personal terminal output has been added.

## 3. Commands / tools used

Commands were run by the coding assistant inside the project. Private paths and authentication output are not copied here.

| Command / tool | Purpose and actual result |
| --- | --- |
| `pwd`, `ls -la`, `rg --files` | Inspect the working folder and look for project instructions; the folder was initially empty. |
| `file`, `command -v`, Python module checks, `mdls` | Inspect the PDF and available reading tools. Metadata lookup failed and no checked Python PDF library was available. |
| Swift with PDFKit and Vision | Read all 12 PDF pages using OCR after the sandboxed attempt failed. |
| `git --version` | Reported `git version 2.54.0 (Apple Git-157)`. |
| `python3 --version` | Reported `Python 3.9.6`. |
| `code --version` | Reported VS Code `1.146.0` for `arm64`, with a macOS diagnostic. This does not verify that the editor opened. |
| `sw_vers` | Checked the macOS environment; no identifying output is included. |
| `git check-ref-format --branch main` | Confirmed that `main` is a valid branch name. |
| `git config --get` | Checked whether author settings were present without copying personal values. A public-safe repository-local author identity was configured before committing. |
| `git init -b main` | Initialized the local repository with `main` as its starting branch. |
| `gh auth status` | Verified authentication for `aryangetsreal` with network access. |
| `gh repo view aryangetsreal/digital-detective-8427 --json nameWithOwner,url,visibility,isEmpty,defaultBranchRef` | GitHub could not find the target repository. |
| `python3` setup and validation scripts | Created the folders and text files, checked the scaffold, and printed its directory structure. |
| `gh api user` | Retrieved only the public account ID and username to form the GitHub noreply address. |
| `git config --local user.name`, `git config --local user.email`, `git var GIT_AUTHOR_IDENT` | Set and checked a privacy-safe author for this repository. |
| `open -a "Visual Studio Code" .`, `open -a Terminal .` | Opened this project folder in the editor and Terminal; both commands succeeded. |
| `git add` with explicit file paths, `git diff --cached --check`, `git diff --cached --stat` | Staged and reviewed the 14 approved setup files. |
| `git commit -m "Set up Digital Detective mission structure"` | Created the dedicated Mission 0 setup commit. |
| `gh repo create aryangetsreal/digital-detective-8427 --public --source=. --remote=origin --push` | Created the public repository, added `origin` and pushed `main`. |
| `gh repo view`, `gh api` repository tree and commit checks, `git rev-parse HEAD` | Verified public visibility, file paths and matching local/remote setup commit hashes. |
| `git status --short --branch`, `git diff --check` | Review the local setup and check whitespace before approval. |

With approval, staged the 14 reviewed setup files and created the setup commit. Created the public repository and pushed `main` using GitHub CLI. Verified the public visibility, remote commit hash and root file listing through GitHub. A separate Mission 0 documentation update records these verified results.

## 4. My understanding

The following explanation was supplied by the student:

A Git repository is a place where we store our project files and keep track of changes made to them over time. The assignment files are grouped into different mission folders so that each task stays organized and is easier to find, understand, and manage.

## 5. Difficulties faced

The assignment was a scanned PDF. The first OCR attempt failed inside the execution sandbox. The first Git initialization was also blocked by the workspace permission policy. GitHub authentication initially appeared invalid inside the sandbox. The existing Git author settings were not ready for a privacy-safe public setup commit.

These are observed setup issues from the assistant's run, rather than invented personal experiences.

## 6. How I resolved them

With permission, OCR was retried outside the sandbox and all 12 pages were read. Git initialization succeeded after permission was granted. The network-enabled authentication check confirmed that GitHub CLI was authenticated. Configured a repository-local Git author using the public GitHub username and GitHub's account-specific noreply email. Global Git settings were left unchanged.

## 7. Evidence / files

- [Root README](../README.md): assignment overview, mission index, tool checks and learning summary.
- This README: setup work, actual checks and understanding.
- [Setup-time directory structure](../evidence/mission-00-structure.txt): the original scaffold; Git internals are excluded. Later approved changes are recorded in subsequent missions.
- [Converter file](../mission-05-numbers-data/number_converter.py): created empty during Mission 0 and implemented during Mission 5.
- [Ignore rules](../.gitignore): common local files excluded from version control.
- All nine mission README files are linked from the root README. At the setup checkpoint, Missions 1–8 contained templates only; current progress is shown in the root README.

No screenshots were taken. No passwords, tokens, full USN, private account email or computer/network identifiers are included in the setup files.

## 8. Evidence / links

- Verified public repository: https://github.com/aryangetsreal/digital-detective-8427
- Remote setup commit: https://github.com/aryangetsreal/digital-detective-8427/commit/121ff322def414f7e9a0b70c28e5ead7bd6a7684
- GitHub file visibility: verified through the remote tree listing on `main`; [browse the setup files](https://github.com/aryangetsreal/digital-detective-8427/tree/121ff322def414f7e9a0b70c28e5ead7bd6a7684).

## 9. Commit details

- Setup commit message: `Set up Digital Detective mission structure`
- Scope: Mission 0 workspace, root documentation, empty later mission templates and required scaffolds only.
- Branch: `main`.
- Setup commit hash: `121ff322def414f7e9a0b70c28e5ead7bd6a7684`.
- Push status: Successful; `main` tracks `origin/main`.
- Remote verification: GitHub reported public visibility and the same setup commit hash as the local repository. All required root folders were visible.

The setup commit hash above was recorded after its push was verified. This documentation correction uses the separate message `Record verified Mission 0 publishing details`. Its final hash is available from Git history; a commit cannot contain its own final hash.

Mission 0 setup was completed and verified on GitHub, and the project was opened in Terminal and VS Code. At that setup checkpoint, Missions 1–8 had not started. Current progress is recorded in the root README.
