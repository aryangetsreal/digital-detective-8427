# Mission 06 - Git and GitHub

Status: Task 6.1 practice notes. Branch, PR, glossary and final documentation are still pending.

## 1. Task / objective

Practise the Git workflow, create the required `update-about` branch, add a learning update and open a Pull Request into `main`.

## 2. Work completed

Codex ran the commands in my Mac's zsh environment.

### Task 6.1 - Understand the basic Git workflow

The initial `git status` showed a clean working tree on `main`. The latest commit was `f4b238d`, completing Mission 5. `git remote -v` showed the expected GitHub repository.

This README adds notes for the required staging and commit exercise. The next steps are to stage this specific file, create the practice commit and inspect the updated history. The final Mission 6 documentation will wait for review.

| Git operation | Meaning |
| --- | --- |
| Check status | Shows the current branch and files that are changed, staged or untracked. |
| Stage selected changes | Chooses a snapshot of specific changes for the next commit. |
| Create a commit | Saves the staged snapshot in the local Git history with a message. |
| View history | Shows earlier commits and their messages. |

The working directory contains editable project files. The staging area holds the changes selected for the next commit. The local repository stores committed history. The remote repository is the copy hosted on GitHub.

Staging selects changes; committing saves the selected snapshot. Pushing later sends local commits to GitHub.

## 3. Commands / tools used

- `pwd`: checked the project directory; its private path is redacted in local evidence.
- `git status`: verified the clean starting state on `main`.
- `git branch` and `git branch --all`: checked the existing branches.
- `git log --oneline -5`: viewed recent history and confirmed Mission 5's commit.
- `git remote -v`: checked the GitHub remote.

## 4. My understanding

Awaiting review after the required branch and PR activity.

## 5. Difficulties faced

No command errors so far. Personal difficulties have not been confirmed.

## 6. How I resolved them

No command error needed a resolution. Personal difficulties will be recorded after confirmation.

## 7. Evidence / files

This README records the basic workflow notes. The actual command transcript is being collected locally and will be included in the final documentation after review.

## 8. Evidence / links

- [Project overview](../README.md).
- Repository: https://github.com/aryangetsreal/digital-detective-8427.
- Branch and PR evidence: not created yet.

## 9. Commit details

- Required Task 6.1 practice commit message: `Document basic Git workflow`.
- Scope: this README only.
- Final mission commit message after approval: `Complete Git and GitHub mission`.
- Final documentation has not been committed or pushed.
