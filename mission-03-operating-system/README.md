# Mission 3 — Understand the operating system

## 1. Task / objective
The goal of Mission 3 was to examine the operating system (OS) running on my machine, observe active processes and system storage, understand the difference between absolute and relative file paths, inspect Unix file permissions, and explain the core responsibilities of an OS.

## 2. Work completed
- Explored system details using terminal commands to inspect OS type, architecture, active user account, storage allocation, and running processes.
- Defined what processes and PIDs are and identified active system processes.
- Navigated between project folders to analyze absolute and relative paths.
- Inspected file permission strings (`-rw-r--r--`) and explained the meaning of read (`r`), write (`w`), and execute (`x`) permissions.
- Outlined the six core responsibilities of an operating system with clear real-world examples.

## 3. Commands / tools used
- `uname -srm`: Checked the OS kernel name, version, and CPU architecture.
- `whoami`: Checked the active user account name.
- `df -h /`: Displayed storage capacity, used space, and free space on the root mount.
- `ps -A` / `ps aux`: Inspected the active process table and PIDs.
- `ls -l`: Inspected file permissions and ownership.
- `cd` and `pwd`: Practiced path navigation.

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | The operating system kernel and hardware architecture. | `Darwin 27.2.0 arm64` (macOS kernel running on 64-bit Apple Silicon). |
| **Current account identity** | The username of the user currently running the terminal session. | `[redacted]` (current local user account). |
| **Available and used storage** | Total disk space, amount consumed, and free space available for storage. | Root volume size: `460Gi`, Used: `13Gi`, Available: `218Gi` (~6% volume capacity used). |
| **System activity snapshot** | Active processes running on the machine with their PIDs, TTY, CPU time, and names. | Active processes running across background daemons, window server, and user shell. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active, executing instance of a computer program loaded into system memory (RAM). When you run an application or command, the OS loads its instructions and data into memory, gives it system resources, and begins executing its code as a process.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to identify and keep track of each active process during its lifecycle.
- **Two examples of processes running on my computer:**
  1. `launchd` (PID 1): The parent bootstrap process on macOS that initializes the user environment and manages system services.
  2. `zsh`: The interactive command-line shell process running inside Terminal to execute my shell commands.

---

### Task 3.3 — Understand paths and permissions
- **Difference between an absolute path and a relative path:**
  - **Absolute path:** Starts from the root of the file system (`/`) and specifies the full location of a file regardless of where you currently are.
    *Example:* `/Users/[redacted]/Desktop/digital-detective-8543/mission-03-operating-system/README.md`
  - **Relative path:** Points to a file relative to your current working directory.
    *Example:* If my terminal is currently inside `digital-detective-8543`, the relative path is simply `mission-03-operating-system/README.md`. If I am inside `mission-03-operating-system`, the relative path back to the root README is `../README.md`.
- **Understanding file permissions (`r`, `w`, `x`):**
  Running `ls -l practice.txt` showed `-rw-r--r--`:
  - `r` (Read): Grants permission to view or read the file's contents (or list items in a folder).
  - `w` (Write): Grants permission to edit, modify, or delete the file (or add/remove files in a directory).
  - `x` (Execute): Grants permission to run the file as a program or executable script (or enter into a folder).
  The permissions breakdown into three groups: Owner (`rw-` = read and write), Group (`r--` = read only), and Others (`r--` = read only).

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | The OS creates, schedules, and cleans up processes, distributing CPU time so multiple programs run concurrently without freezing. | Switching CPU execution between a web browser, code editor, and music player seamlessly. |
| **Memory management** | The OS allocates RAM blocks to active programs and reclaims memory when they close, ensuring apps do not overwrite each other's data. | Providing RAM when a new browser tab opens and freeing that memory when the tab is closed. |
| **Device management** | The OS communicates with hardware peripherals using device drivers, translating software requests into hardware signals. | Translating keypresses on a keyboard into text input or sending print jobs to a printer. |
| **File management** | The OS manages physical storage drives by organizing files and folders into a structured filesystem and regulating read/write operations. | Organizing files on the SSD using Apple File System (APFS) and maintaining folder paths. |
| **User interface / shell** | The OS provides an interface enabling humans to interact with system hardware and software via graphic or command-based controls. | The macOS desktop/Finder graphical interface and the Terminal `zsh` command shell. |
| **Security and permissions** | The OS verifies user identities, isolates applications in sandboxes, and checks permission flags before allowing file access. | Requiring password/Touch ID confirmation for administrative changes and blocking unauthorized file edits. |

## 5. Difficulties faced
Reading Unix permission strings can look confusing at first because all 9 characters (`rwxr-xr-x`) are bunched together without spaces.

## 6. How I resolved them
I broke the string into three distinct groups of three: the first set of three for the Owner (`rw-`), the second for the Group (`r--`), and the third for Others (`r--`).

## 7. Evidence / files
- `mission-03-operating-system/README.md` (this file)

## 8. Commit details
- Branch: `main`
- Commit message: `Document operating system and file management`
