# Mission 04 - How programs run

Status: Completed.

## 1. Task / objective

Create and run the Python program required by the PDF. Compare a compiler and an interpreter using a table and a short explanation.

## 2. Work completed

Codex ran the commands in my Mac's zsh environment.

### Task 4.1 - Create and run a Python program

Created [hello.py](hello.py) with the required one-line program:

```python
print("Hello from Python")
```

The interpreter checks gave these actual results:

| Command | Actual output |
| --- | --- |
| `python3 --version` | `Python 3.9.6` |
| `python3 -c 'import platform; print(platform.python_implementation())'` | `CPython` |

From the Mission 4 folder, the program was run with:

```sh
python3 hello.py
```

Actual output:

```text
Hello from Python
```

The command finished with exit status `0` and no error output. Python ran the `print` instruction and displayed the message. No separate executable was created for this task.

A **program** is a set of instructions for a computer. **Source code** is the text written in a programming language, such as the line in `hello.py`. When this program runs, Python carries out the instruction and sends the message to the terminal.

The operating system starts the Python process and provides resources such as memory and access to terminal output. This explains the OS role; memory allocation was not separately tested here.

### Task 4.2 - Compare compiler and interpreter

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation / execution happens | Translates source code before the translated program runs. | Executes code through a runtime while the program runs. |
| Typical output | Translated code, often machine code or an executable. | The program's results during execution; usually no separate native executable for the user. |
| One example | A C compiler such as Clang. | The Python interpreter, such as CPython. |
| One advantage | A built executable can be run without compiling the original source again each time. | Makes it easy to run small programs and try changes during development. |

A compiler translates source code into another form before that translated program runs. An interpreter executes code through a runtime rather than requiring the user to build a separate native executable first. C commonly uses a compiler, while Python is commonly run through an interpreter. CPython combines both approaches by compiling Python source to bytecode (intermediate instructions) and then executing it.

The Python run was demonstrated. The compiler example and the explanation of CPython's internal steps are conceptual comparisons; no C compilation or bytecode inspection was performed. Performance depends on the implementation and the program, so compiled programs are not always faster.

## 3. Commands / tools used

- `python3 --version`: checked the interpreter version used for the run.
- `python3 -c 'import platform; print(platform.python_implementation())'`: identified the implementation as CPython.
- `python3 hello.py`: ran the program from the Mission 4 folder.
- Python `print()`: displayed the required message.
- macOS zsh: the shell used to run the commands.
- Python helper: wrote the source file, captured output and checked the exit status.
- Swift, PDFKit and Vision: read the exact Mission 4 instructions from the scanned PDF.
- Git: checked the repository, branch, clean starting state and previous mission commit.

## 4. My understanding

I learned that a program is basically a set of instructions written in a programming language. I used Python to run `hello.py`, which printed 'Hello from Python' in the terminal. I also understood that a compiler translates code before the resulting program runs, while an interpreter runs code through a runtime. Python can use both approaches internally.

## 5. Difficulties faced

No personal difficulties. The interpreter checks and program run completed without errors.

## 6. How I resolved them

Not applicable. No personal difficulties or technical errors needed a resolution.

## 7. Evidence / files

- [hello.py](hello.py): the required one-line Python program.
- [Command transcript](evidence/terminal-session.txt): the three commands, actual output, error output and exit statuses.
- [This README](README.md): program explanation and comparison table.

The PDF does not require screenshots, a compiled program or an error experiment for this mission. No generated executable or temporary build files are included.

## 8. Evidence / links

- [Project overview](../README.md).
- [Program execution evidence](evidence/terminal-session.txt).
- [Mission 4 commit history](https://github.com/aryangetsreal/digital-detective-8427/commits/main/mission-04-programs/README.md).

## 9. Commit details

- Commit message: `Complete program execution mission`.
- Scope: Mission 4 README, `hello.py`, command transcript and the approved root README status and progress corrections.
- Branch: `main`.
- Commit hash: `0ad93de4573547d5126e56187243d2d20e9b836e`.
- Push status: Verified on GitHub `main`; the published commit and files were checked during the final review.
- [Published commit](https://github.com/aryangetsreal/digital-detective-8427/commit/0ad93de4573547d5126e56187243d2d20e9b836e).

Verification compares the local and remote hashes, checks the public repository and published README, and confirms a clean working tree.
