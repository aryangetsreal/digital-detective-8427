# THE DIGITAL DETECTIVE

This first-year CSE assignment explores how a computer works through a series of practical missions. This repository stores the work, notes and evidence for each mission.

Repository name: `digital-detective-8427`. The suffix matches the last four USN digits, confirmed by the student. Full student details are omitted for privacy.

## My Learning

- I learned that a program is basically a set of instructions written in a programming language.
- I learned that the same number can be written in decimal, binary and hexadecimal.

## Assignment objectives

- Understand computer input, processing, output and storage.
- Practise Terminal commands and safe file management.
- Explore operating systems and how programs run.
- Learn number systems, text encoding and basic Python.
- Use Git and GitHub to record and publish work.
- Understand basic networking and review the final assignment.

## Mission index

| Mission | Topic | Status |
| --- | --- | --- |
| 00 | [Create your GitHub workspace](mission-00-setup/README.md) | Completed |
| 01 | [Know your computer](mission-01-computer/README.md) | Completed |
| 02 | [Become comfortable with the Terminal](mission-02-terminal/README.md) | Completed |
| 03 | [Understand the operating system](mission-03-operating-system/README.md) | Completed |
| 04 | [How programs run](mission-04-programs/README.md) | Completed |
| 05 | [Numbers and data](mission-05-numbers-data/README.md) | Completed |
| 06 | [Git and GitHub](mission-06-git-github/README.md) | Completed |
| 07 | [How computers communicate](mission-07-networking/README.md) | Completed |
| 08 | [Final report and submission](mission-08-final-report/README.md) | Completed |

## Project organization

Each mission has its own folder and README. All nine missions are complete for repository preparation. Mission 8 records the final audit and the separate college-submission checklist. The [number converter](mission-05-numbers-data/number_converter.py) uses functions and while loops to convert decimal integers to binary and hexadecimal. The Mission 5 README also demonstrates Python's built-in `bin()` and `hex()` functions. Evidence folders hold privacy-safe screenshots or selected command output.

Each mission is documented and committed separately. The Git history also includes the learning branch and merged PR #1.

## Run the number converter

From the project root:

```sh
cd mission-05-numbers-data
python3 number_converter.py
```

Enter a decimal integer, such as `13`. The program prints binary and hexadecimal results. The main converter uses while loops; Mission 5 also demonstrates the built-in `bin()` and `hex()` functions separately.

## Tools used

| Tool | Setup use or verification |
| --- | --- |
| macOS | Operating system used for setup. |
| Terminal | Command-line setup checks run through the coding assistant; project opened in Terminal using `open -a Terminal .`. |
| VS Code | Command-line version checked: 1.146.0; project opened using `open -a "Visual Studio Code" .`. |
| Python | Python 3.9.6 checked; used by the assistant to create and validate setup files. |
| Git | Git 2.54.0 (Apple Git-157) checked; local repository initialized on `main`. |
| GitHub | GitHub CLI authentication verified for `aryangetsreal`; public repository created; setup commit pushed and verified on `main`. |

## Final learning summary

This assignment helped me connect basic computer concepts with practical examples. The Apple Notes activity showed input, processing, output and storage working together. Reviewing Terminal output helped me understand files, paths, options and pipes. The process and permission checks showed how macOS manages running programs and file access. Running Python connected source code with output. The converter and character checks connected binary, hexadecimal, ASCII, Unicode and UTF-8 with actual results. Git history and the branch showed how changes are recorded, and I manually merged PR #1 on GitHub. The networking tests helped me distinguish DNS lookup from a connectivity check.

Progress: **9/9 missions completed** for the repository. College Google Form submission is still pending and remains my responsibility.
