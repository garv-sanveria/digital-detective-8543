# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 was to write and run a simple Python script from the command line and understand the difference between compiled programming languages and interpreted programming languages in how they translate and execute source code.

## 2. Work completed
- Created a Python script named `hello.py` inside the `mission-04-programs/` directory with a one-line print statement.
- Executed the script from the terminal using `python3 hello.py` and verified the output.
- Researched and constructed a comparison table between compilers and interpreters across execution timing, output formats, real-world language examples, and key advantages.
- Wrote a clear explanation summarizing the practical differences between both translation methods.

## 3. Commands / tools used
- `python3 hello.py`: Executed the Python script through the Python 3 interpreter runtime.
- Terminal: Navigated to the folder and ran tests.

## 4. My understanding

### Task 4.1 — Create and run a Python program
Inside this folder, I created `hello.py` containing:
```python
print("Hello from Python")
```

Running the script in Terminal:
```bash
$ python3 hello.py
Hello from Python
```
The terminal immediately printed `Hello from Python` and returned to the prompt with exit code 0.

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into native machine code all at once before the program is executed. | Translates and executes instructions step-by-step at runtime (often via an intermediate bytecode stage). |
| **Typical output** | Produces a standalone machine-code binary executable file (e.g., `.exe` or Mach-O executable). | Executes code directly in memory; does not output a permanent standalone machine binary. |
| **One example** | C, C++, Rust, Go. | Python, JavaScript, Ruby. |
| **One advantage** | Runs significantly faster because the code is already converted and optimized for the CPU ahead of time. | Much faster development and debugging cycle since changes can be tested immediately without waiting for a build step. |

#### Explanation of differences:
A compiler processes the entire source code file beforehand and converts it directly into machine code that the CPU can execute natively, creating a standalone executable file that runs very fast. In contrast, an interpreter reads the program and executes the instructions line-by-line while the program is running, without producing a separate machine executable file first. As a result, compiled programs (like C or Rust) have superior execution performance, while interpreted programs (like Python or JavaScript) provide an interactive, flexible workflow where you can write code and run it immediately across different operating systems.

## 5. Difficulties faced
Understanding whether Python is purely interpreted or uses compilation, since Python creates `.pyc` bytecode files under `__pycache__`.

## 6. How I resolved them
I learned that Python actually uses a hybrid model: it compiles source code into platform-independent intermediate bytecode first, and then the Python Virtual Machine (PVM) interpreter executes that bytecode line-by-line.

## 7. Evidence / files
- `mission-04-programs/README.md` (this file)
- `mission-04-programs/hello.py`

## 8. Commit details
- Branch: `main`
- Commit message: `Compare compilers and interpreters`
