# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 was to understand how computer systems handle information through the Input, Processing, Output, and Storage (IPOS) model, distinguish between computer hardware and different types of software (operating system, application, and utility), and examine computer-based embedded systems used in daily life.

## 2. Work completed
- Analyzed a real-world computing task ("Typing and saving a programming assignment document") and mapped each step to the IPOS cycle.
- Identified four essential hardware components and four distinct software examples, classifying the software into OS, application, and utility categories.
- Studied three everyday computer-based systems outside of regular laptops or phones (ATM, Smart Traffic Light, and Metro Ticket Machine).
- Documented all findings and tables directly into this README.

## 3. Commands / tools used
- Text Editor / IDE: Used to compile observations and format markdown tables.
- System Profiler / macOS Information: Referenced hardware and system specifications.

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing and saving a programming assignment document.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | I press keys on the keyboard to enter code and click save with the trackpad. | Built-in Keyboard, Trackpad |
| **Processing** | The CPU interprets keyboard signals, updates the document state in memory, and handles formatting. | CPU (Apple Silicon M-series), Unified RAM |
| **Output** | The display refreshes immediately to show the typed characters and save notifications on screen. | Retina Display screen |
| **Storage** | When I press Save (`Cmd + S`), the document data is written from temporary RAM onto the permanent drive. | Internal NVMe SSD |

**How the activity moves from input to storage:**
When I press a key, the keyboard hardware sends a scan code to the operating system as an input. The OS passes this to the CPU, which processes the input by updating the active text buffer held in volatile RAM. The graphics processor then immediately updates the frame buffer to render the new characters on the display so I can see what I typed. When I choose to save the document, the CPU instructs the storage controller to write the data from RAM onto the solid-state drive (SSD), making the file permanent so it stays intact even after the computer is turned off.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Used to enter text, commands, and shortcuts into the computer. |
| **Apple M-series CPU** | Hardware | Not applicable | The brain of the computer that fetches, decodes, and runs program instructions. |
| **Internal SSD** | Hardware | Not applicable | Non-volatile storage where the operating system, programs, and files are permanently kept. |
| **Retina Display** | Hardware | Not applicable | Output device that visually presents user interfaces, text, images, and videos. |
| **macOS** | Software | Operating system software | Manages computer hardware resources, memory, files, and runs user applications. |
| **Visual Studio Code** | Software | Application software | Interactive code editor used for writing, editing, and managing source code files. |
| **Terminal (zsh)** | Software | Utility software | Command-line shell allowing users to directly interact with the operating system using text commands. |
| **Activity Monitor** | Software | Utility software | System diagnostics tool used to monitor CPU usage, memory consumption, and active running processes. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Allows bank customers to check balances, deposit money, and withdraw cash securely. | Numeric PIN keypad / Touchscreen card reader | Cash dispenser slot / Printed paper receipt |
| **Smart Traffic Signal** | Regulates the safe flow of traffic and pedestrian crossings at intersections. | Inductive loop vehicle sensor embedded in the road / Pedestrian push button | Red, Yellow, and Green LED signal lights |
| **Metro Ticket Vending Machine** | Issues single-journey tokens or recharges electronic transit smartcards. | Touchscreen fare selection / Cash note and coin acceptor | Dispensed plastic token/ticket / On-screen transaction receipt |

## 5. Difficulties faced
Distinguishing between application software and utility software initially felt a bit subtle. For example, deciding whether the Terminal and Activity Monitor count as utility or application software.

## 6. How I resolved them
I reviewed the definitions: application software helps users perform productive end-user tasks (like writing code in VS Code or browsing the web), whereas utility software helps maintain, optimize, diagnose, or interact directly with system functions (like Activity Monitor monitoring resources or Terminal running administrative commands).

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (this file)

## 8. Commit details
- Branch: `main`
- Commit message: `Complete computer basics and IPOS mission`
