# Mission 8 — Final report and submission

## 1. Task / objective
The objective of Mission 8 was to perform a comprehensive final audit of the entire repository, ensure that all 8 missions are thoroughly completed according to their specifications, verify that all READMEs follow the mandatory structure, test that all code executes without errors, and prepare the repository for final evaluation.

## 2. Work completed
- Audited the entire workspace tree to confirm that all required folders, code files, and READMEs are present.
- Updated the root `README.md` with a complete project summary, mission navigation table, converter execution instructions, and personal learning reflections.
- Completed the final submission checklist verifying compliance with all assignment guidelines.
- Sanitized outputs to ensure zero private credentials, tokens, or sensitive network details are exposed.

## 3. Commands / tools used
- `git status` & `git log`: Verified that each mission was committed with dedicated, meaningful commit messages.
- `python3`: Verified execution of `hello.py` and `number_converter.py`.
- `find . -not -path '*/.*'`: Verified that all required files and directories match the assignment specification.

## 4. My understanding

### Repository Audit Summary
Every mission in this assignment covers a fundamental building block of modern computer systems:
- **Mission 0:** Setting up a structured, professional Git workspace.
- **Mission 1:** Tracing the IPOS cycle and distinguishing between hardware and system/application software.
- **Mission 2:** Mastering CLI navigation, safe file manipulation, piping, and package managers.
- **Mission 3:** Understanding OS kernel duties, process scheduling (PIDs), file permissions (`rwx`), and storage.
- **Mission 4:** Contrasting compiled languages (ahead-of-time binary) with interpreted languages (runtime execution).
- **Mission 5:** Converting number bases (decimal, binary, hex), text encodings (ASCII, UTF-8), and writing Python tools.
- **Mission 6:** Implementing version control best practices, branch isolation, and collaborative Pull Request workflows.
- **Mission 7:** Tracing network communication, DNS resolution, packets, routers, and web request lifecycles.

### Final Submission Checklist
- [x] **Repository Structure:** All mission folders (`mission-00` to `mission-08`) and `evidence/` exist and match the requirements.
- [x] **Mandatory README Format:** Every mission README contains the required 8 numbered headings with thorough, authentic details.
- [x] **Dedicated Commits:** Each mission was staged and committed individually with the exact suggested commit messages.
- [x] **IPOS & System Tables:** Completed with clear explanations in Mission 1.
- [x] **Terminal Practice:** Completed with safe file redirection, pipes, and flags documented in Mission 2.
- [x] **OS Observations:** Real system observations (macOS arm64, disk space, active processes) recorded in Mission 3.
- [x] **Python Scripts:** `hello.py` runs cleanly and compiler vs. interpreter is explained in Mission 4.
- [x] **Number Converter:** `number_converter.py` is tested with three positive numbers (`42`, `128`, `255`) and explained in Mission 5.
- [x] **Git & GitHub Collaboration:** Branching (`update-about`), glossary, and PR workflow documented in Mission 6.
- [x] **Networking:** `ping` connectivity test, `nslookup` DNS query, and 7-step website loading process documented in Mission 7.
- [x] **Privacy & Sanitization:** All personal identifiers and private network info have been redacted with `[redacted]`.

## 5. Difficulties faced
Managing multiple independent topics while ensuring every single section follows the instructor's rubric consistently.

## 6. How I resolved them
I followed the required 8-section README outline strictly for each mission, cross-referencing each requirement against the assignment sheets before creating each commit.

## 7. Evidence / files
- `mission-08-final-report/README.md` (this file)
- `README.md` (root project index)
- Complete assignment repository tree

## 8. Commit details
- Branch: `main`
- Commit message: `Complete final report and verify assignment submission`
