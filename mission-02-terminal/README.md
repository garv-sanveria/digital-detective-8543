# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 was to gain confidence using the Unix command-line interface (CLI) on macOS. This involved navigating directory paths, managing files safely, understanding how flags modify command behavior, chaining commands with pipes, and exploring how package managers (Homebrew) function.

## 2. Work completed
- Explored essential terminal commands for inspecting, moving, copying, creating, and displaying files.
- Created a safe practice folder (`mission-02-terminal/terminal-practice`) and tested file creation, appending text without overwriting, making backups, and renaming files.
- Investigated flags (`-l`, `-a`, `-h`) on directory listings and experimented with piping command output into `head`.
- Checked Homebrew version and inspected installed formulas.
- Documented all commands, observations, answers to practice questions, and reflections in this README.

## 3. Commands / tools used
- `pwd`: Displayed the absolute path of the working directory.
- `ls`, `ls -l`, `ls -lah`: Listed files with permissions, hidden entries, and human-readable sizes.
- `cd` and `cd ..`: Changed directories and navigated up to the parent directory.
- `mkdir`: Created new directories.
- `touch`: Created an empty text file.
- `echo "..." >` and `echo "..." >>`: Wrote and safely appended lines of text to a file.
- `cat`: Output file contents directly to the terminal screen.
- `cp`: Created a duplicated backup file.
- `mv`: Renamed a file.
- `|` (pipe) with `head -n 5`: Redirected terminal output to display only the top five lines.
- `brew --version` & `brew list`: Inspected the local package manager.

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the exact absolute path from the root directory to where the terminal currently is. | Returned `/Users/[redacted]/Desktop/digital-detective-8543`. |
| **Directory listing (`ls`)** | Lists the visible files and folders in the current directory. | Displayed all the mission folders cleanly in column format. |
| **Detailed listing (`ls -l`)** | Shows detailed metadata including file permissions, number of links, owner, group, byte size, and modification timestamp. | Showed permissions like `drwxr-xr-x`, file sizes, and date stamps for each item. |
| **Change directory (`cd ..`)** | Changes the active directory to the parent directory. | Navigated up from the project folder to `Desktop`, changing the terminal prompt location. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new subdirectory at the specified path. | A new folder named `terminal-practice` appeared in the directory listing. |
| **Create empty file (`touch practice.txt`)** | Creates a new 0-byte file if it does not exist, or updates its timestamp. | A new blank file `practice.txt` was created with a size of 0 bytes. |
| **Copy file (`cp practice.txt practice_backup.txt`)** | Duplicates the source file to a new target file while keeping the original intact. | Two identical files existed side-by-side: `practice.txt` and `practice_backup.txt`. |
| **Move / rename file (`mv practice_backup.txt practice_backup_old.txt`)** | Moves or renames a file to a new name or location without duplicating data. | `practice_backup.txt` disappeared and was renamed to `practice_backup_old.txt`. |
| **Display file contents (`cat practice.txt`)** | Reads and prints the entire contents of a text file directly to standard output. | Printed the exact lines of text stored inside `practice.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside `mission-02-terminal/terminal-practice`, I performed the following:
1. Created `practice.txt` and added a first line using `>`:
   ```bash
   echo "First line of terminal practice." > practice.txt
   ```
2. Appended a second line without removing the first line using `>>`:
   ```bash
   echo "Second line appended safely." >> practice.txt
   ```
3. Verified both lines using `cat practice.txt`:
   ```text
   First line of terminal practice.
   Second line appended safely.
   ```
4. Made a backup copy and renamed it:
   ```bash
   cp practice.txt practice_backup.txt
   mv practice_backup.txt practice_backup_old.txt
   ```

#### Answers to questions:
- **What is the difference between replacing a file's contents and adding text to the end?**
  Using a single redirection operator (`>`) truncates and overwrites the entire file, deleting whatever was there before. Using double redirection (`>>`) appends new text to the end of the existing file while keeping all previous content intact.
- **What is the difference between copying a file and moving a file?**
  `cp` creates an independent duplicate of the file, leaving the original unchanged in its original place. `mv` renames or shifts the file to a new path without keeping the original copy.
- **What information does the current-directory display provide?**
  `pwd` provides the full, unabbreviated absolute path starting from the root directory (`/`), preventing confusion about which folder you are working in.
- **Why is a directory-listing operation useful?**
  It lets you verify that files were created or modified as expected, check spelling and file extensions, and ensure you are working with the correct filenames before running destructive commands.

---

### Task 2.3 — Understand flags and pipes
- **Comparing directory listings:**
  Running plain `ls` only prints visible file and folder names. Adding flags (`ls -lah`) dramatically changes the output:
  - `-l`: Formats as a long list with permissions, owners, and sizes.
  - `-a`: Includes hidden files (those starting with `.`, like `.git` and `.DS_Store`).
  - `-h`: Makes file sizes human-readable (e.g., `4.0K` or `12M` instead of raw byte counts like `4096`).
- **Piping output (`ls -lah | head -n 5`):**
  The pipe operator (`|`) takes standard output from the command on the left (`ls -lah`) and feeds it directly as standard input to the command on the right (`head -n 5`). Instead of flooding the screen with dozens of entries, `head` intercepts the stream and displays only the first five lines.

---

### Task 2.4 — Understand package managers
- **Tool tested:** Homebrew on macOS (`Homebrew 7.0.13` at `/opt/homebrew/bin/brew`).
- **Why package managers are useful:**
  A package manager automates downloading, compiling, configuring, installing, and updating software libraries and CLI tools from trusted central repositories. Instead of manually searching websites, unzipping binaries, setting up environment variables, and resolving missing dependencies by hand, a single command like `brew install <tool>` handles everything safely.

## 5. Difficulties faced
A common slip-up when editing files from the terminal is typing `>` instead of `>>`. Doing that accidentally erases the previous file content immediately.

## 6. How I resolved them
I got into the habit of running `cat <filename>` right after appending to double-check that both the old content and the new line were present.

## 7. Evidence / files
- `mission-02-terminal/README.md` (this file)
- `mission-02-terminal/terminal-practice/practice.txt`
- `mission-02-terminal/terminal-practice/practice_backup_old.txt`

## 8. Commit details
- Branch: `main`
- Commit message: `Complete Terminal and file management mission`
