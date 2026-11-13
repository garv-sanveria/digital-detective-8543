# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The goal of this mission was to set up a clean, organized local workspace for the assignment, create the required folder structure for all 8 missions, prepare the initial README files, and check that Python and Git are properly installed on my computer.

## 2. Work completed
- Decided on the repository name matching the rule: assignment name plus the last four digits of my USN (`digital-detective-8543`).
- Created the main project folder on my Desktop.
- Created all the mission subfolders (`mission-00-setup` through `mission-08-final-report`) and the `evidence/` folder.
- Created starter README markdown files in each folder and added the placeholder Python script for the converter in Mission 5.
- Wrote the root `README.md` with an introduction, mission index table, and privacy notes.

## 3. Commands / tools used
- `mkdir -p`: Created multiple nested directories at once from the terminal.
- `touch`: Created initial blank files and `.gitkeep` for tracking empty directories.
- `python3 --version`: Checked the installed Python version (`Python 3.15.2`).
- `git --version`: Checked the Git version (`git version 2.56.0`).
- `git init`: Initialized the local Git repository.
- `git branch -M main`: Renamed the default branch to `main`.

## 4. My understanding
A repository is basically a tracked folder where Git records every snapshot and change over time. Keeping missions in separate folders makes the assignment organized and prevents files from getting mixed up. Having a standard structure from the start means I always know where my scripts, notes, and screenshots belong.

## 5. Difficulties faced
Git does not track empty folders by default, so the `evidence/` folder would not show up in commits if it had nothing in it.

## 6. How I resolved them
I added a simple `.gitkeep` file inside the `evidence/` folder so Git recognizes and includes the folder in commits.

## 7. Evidence / files
- `README.md` (root project index)
- `mission-00-setup/README.md` (this file)
- `evidence/.gitkeep`

## 8. Commit details
- Branch: `main`
- Commit message: `Set up Digital Detective mission structure`
