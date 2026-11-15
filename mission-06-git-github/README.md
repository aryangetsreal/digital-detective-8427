# Mission 06 - Git and GitHub

Status: Completed.

## 1. Task / objective

Practise staging and committing, create the required `update-about` branch, publish a learning update, open a Pull Request into `main`, and explain the Git workflow.

## 2. Work completed

Codex ran the commands in my Mac's zsh environment. The two learning statements used in the branch update came from explanations I had already approved.

### Task 6.1 - Understand the basic Git workflow

The starting state was a clean working tree on `main`. The latest commit was Mission 5's `f4b238d01886090cf9a6690dbe43a8bb792d0274`. The remote was the expected GitHub repository.

| Git operation | What it does | Actual result |
| --- | --- | --- |
| `git status` | Shows the branch and changed, staged or untracked files. | Initially showed `main` and a clean working tree. After editing, it showed this README as modified. |
| `git add -- mission-06-git-github/README.md` | Selects this README's changes for the next commit. | A second status check showed the README under Changes to be committed. The evidence folder remained untracked. |
| `git commit -m "Document basic Git workflow"` | Saves the staged snapshot in local history. | Created commit `6e4ee0228517baac04bf0b9d24132468981ccb46`. Only this README was committed. |
| `git log --oneline -5` | Displays recent commit messages and short hashes. | The new `6e4ee02 Document basic Git workflow` entry appeared above Mission 5. |

The practice commit was pushed to `main`. GitHub reported the same full hash as the local `main` branch.

| Part of the workflow | Meaning |
| --- | --- |
| Working directory | The files being edited on the computer. |
| Staging area | The snapshot selected for the next commit. |
| Local repository | The committed history stored by Git on the computer. |
| Remote repository | The GitHub repository where commits are published. |

Staging selects changes; committing saves that selected snapshot locally. Pushing sends the commits to GitHub. The basic sequence is **edit → stage → commit → push**.

### Task 6.2 - Create and use a branch

The required branch did not exist locally or on GitHub. It was created with `git branch update-about` and selected with `git checkout update-about`.

A section titled **My Learning** was added to the root README with two points:

- I learned that a program is basically a set of instructions written in a programming language.
- I learned that the same number can be written in decimal, binary and hexadecimal.

After `git status`, only `README.md` was staged using `git add -- README.md`. The commit message was `Add My Learning section`. The resulting commit was `1b2e69182e99f8fd55b3b91e68e0443c82a67102`, and `git push origin update-about` published it.

A branch is a separate line of work in the repository. It lets a change be prepared while `main` keeps its current version.

### Task 6.3 - Create a Pull Request

The repository was opened on GitHub using macOS `open`. GitHub CLI then created the real Pull Request and retrieved its details and diff.

| Detail | Verified result |
| --- | --- |
| PR | [#1 - Add My Learning section](https://github.com/aryangetsreal/digital-detective-8427/pull/1) |
| Source branch | `update-about` |
| Target branch | `main` |
| Status | **MERGED**; GitHub merge commit `07b816ae6d8cf9634dc19605b7c1b92cea9f7ab5`. |
| Changed file | `README.md` only: five added lines, zero deleted lines. |
| Branch commit | `1b2e69182e99f8fd55b3b91e68e0443c82a67102` |

A Pull Request shows a proposed change and lets it be reviewed before it is merged. Branches keep work separate, while the PR gives people a place to compare and discuss the change.

The diff was reviewed and saved as evidence. I manually merged PR #1 using GitHub's interface. The merge was intentional and authorized by me. Codex verified the merged state and did not run a merge command.

After creating the PR, the assistant returned to `main` with `git checkout main`; the first `git pull origin main` reported `Already up to date.` After I merged the PR on GitHub, another pull brought in the five-line README change. The My Learning section is now on local and remote `main`, at merge commit `07b816ae6d8cf9634dc19605b7c1b92cea9f7ab5`.

### Task 6.4 - Git command glossary

| Operation | Command | Meaning |
| --- | --- | --- |
| Initialize a repository | `git init` | Creates a local Git repository. This was already done in Mission 0 and was not repeated. |
| Check status | `git status` | Shows the branch and whether files are changed, staged or untracked. |
| Stage changes | `git add <file>` | Selects a specific file's current changes for the next commit. |
| Commit changes | `git commit -m "message"` | Saves the staged snapshot with a meaningful message. |
| View history | `git log --oneline` | Shows earlier commits in a short form. |
| Create or list branches | `git branch update-about`; `git branch` | Creates a branch, or lists branches when no name is given. |
| Switch branches | `git checkout <branch>` | Changes to another branch. |
| Publish changes | `git push origin <branch>` | Sends local commits on that branch to GitHub. |
| Retrieve remote changes | `git pull origin main` | Retrieves remote changes and integrates them into the current branch; here it ran on `main`. |

## 3. Commands / tools used

- `pwd`, `git status`, `git branch`, `git log --oneline -5`, `git remote -v`: checked the starting repository, branch, history and remote.
- `git add`, `git commit`, `git push`: performed the required practice and branch-update commits with explicit file paths.
- `git branch update-about`, `git checkout update-about`, `git checkout main`: created the required branch and switched between it and `main`.
- `git pull origin main`: first confirmed that `main` was up to date, then retrieved the README update after I merged the PR.
- `git branch --all`: showed the local and remote branch names.
- `git diff`, `git diff --cached --check`: reviewed the README change and checked the staged file before each required commit.
- `git log main -1 --format=%H`: read the full main-branch commit hash for comparison with GitHub.
- `open`, `gh pr create`, `gh pr view`, `gh pr diff`, `gh api`: opened the repository, created the PR and verified its branches, commit, files and actual diff.
- Swift, PDFKit and Vision: read all Mission 6 instructions from PDF pages 8–9 using OCR.
- Python helper: captured actual command output and redacted private paths.

The glossary explains `git init`; it was not executed again in this mission.

## 4. My understanding

I learned that Git keeps a history of changes, while GitHub stores a shared copy online. Editing a file changes the working directory. Staging selects the changes for a commit, and committing saves that snapshot locally. Pushing publishes the commits to GitHub. A branch lets me work on an update without changing main straight away. A Pull Request shows the differences between branches so the change can be reviewed before merging. After a merge, pulling updates the local main branch.

## 5. Difficulties faced

No personal difficulties. The required commands completed without errors. I manually merged PR #1 using GitHub's interface as part of the exercise.

## 6. How I resolved them

Not applicable. No personal difficulties or command errors needed a resolution.

## 7. Evidence / files

- [Git command transcript](evidence/git-session.txt): actual commands, exit statuses and outputs, including the working-directory and staging-area checks.
- [PR details](evidence/pull-request.json): verified PR URL, branches, state, head commit and changed-file details.
- [PR diff](evidence/pull-request.diff): the reviewed learning-section change, kept as display evidence with trailing line spaces omitted.
- [This README](README.md): task explanations, command glossary and my approved understanding.

No screenshots were required or created. Historical status outputs describe the state at the time each command ran.

## 8. Evidence / links

- [Project overview](../README.md).
- [Task 6.1 practice commit](https://github.com/aryangetsreal/digital-detective-8427/commit/6e4ee0228517baac04bf0b9d24132468981ccb46).
- [Task 6.2 learning commit](https://github.com/aryangetsreal/digital-detective-8427/commit/1b2e69182e99f8fd55b3b91e68e0443c82a67102).
- [Learning update on update-about](https://github.com/aryangetsreal/digital-detective-8427/blob/update-about/README.md).
- [Merged PR #1](https://github.com/aryangetsreal/digital-detective-8427/pull/1).

## 9. Commit details

- Task 6.1: `Document basic Git workflow` - `6e4ee0228517baac04bf0b9d24132468981ccb46`, pushed to `main`.
- Task 6.2: `Add My Learning section` - `1b2e69182e99f8fd55b3b91e68e0443c82a67102`, pushed to `update-about`.
- PR #1: merged on GitHub, from `update-about` into `main`; merge commit `07b816ae6d8cf9634dc19605b7c1b92cea9f7ab5`. I manually merged it using GitHub's interface.
- Final documentation commit message: `Complete Git and GitHub mission`.
- Current branch: `main`.
- Commit hash: `b4c37d825075cf97c06784bb488f05f6c7c07628`.
- Push status: Verified on GitHub `main`; the published commit and files were checked during the final review.
- [Published commit](https://github.com/aryangetsreal/digital-detective-8427/commit/b4c37d825075cf97c06784bb488f05f6c7c07628).

The two earlier commits are required Git exercises. Final verification checks the published files, matching local and remote commits, public visibility and a clean working tree. The existing branch, PR and merge history are preserved.
