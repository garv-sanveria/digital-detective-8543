# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 was to understand version control workflows using Git, distinguish between staging and committing, create and manage feature branches, understand the Pull Request (PR) review process, and compile a clear glossary of everyday Git commands.

## 2. Work completed
- Inspected the repository lifecycle through `git status`, `git add`, `git commit`, and `git log`.
- Explained the conceptual difference between staging files and committing them.
- Created a separate feature branch called `update-about` to practice non-destructive development.
- Updated the root `README.md` on the feature branch by adding a "My Learning" section highlighting key takeaways.
- Documented the Pull Request review and merge workflow and compiled a one-line Git command glossary.

## 3. Commands / tools used
- `git status`: Monitored file states and untracked changes.
- `git add <file>`: Staged modified files to the index.
- `git commit -m "..."`: Saved versioned snapshots with clear messages.
- `git log --oneline`: Reviewed commit history.
- `git checkout -b update-about` (or `git switch -c`): Created and switched to a new branch.
- `git branch`: Listed existing branches in the repository.

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which files are currently tracked, untracked, modified, or staged for commit. |
| **Stage selected changes (`git add`)** | Moves specific file changes into the staging index, choosing what will be in the next snapshot. |
| **Create a commit (`git commit`)** | Permanently records a snapshot of all staged changes with an author and message. |
| **View commit history (`git log`)** | Displays a historical log of past commits showing commit hashes, authors, dates, and descriptions. |

#### Difference between staging a change and committing it:
Staging (`git add`) is an intermediate holding area where you carefully select and organize which changes should go into the next commit. It is like placing chosen items into a shipping box. Committing (`git commit`) is sealing the box and recording it permanently into the repository history with a timestamp and descriptive label. Staging allows you to commit specific parts of your work without being forced to commit everything at once.

---

### Task 6.2 — Create and use a branch
I created and checked out a dedicated feature branch named `update-about`:
```bash
git checkout -b update-about
```
On this branch, I added the `## My Learning` section to the root `README.md` and committed the update cleanly.

---

### Task 6.3 — Create a Pull Request
- **What is a branch?**
  A branch is an independent line of development that splits off from the main codebase (`main`). It lets a developer build new features, test ideas, or fix bugs without affecting the stable code that everyone else is using.
- **What is a Pull Request (PR)?**
  A Pull Request is a formal request on GitHub proposing that changes from a feature branch be merged into another branch (usually `main`).
- **Why are they useful in team projects?**
  They allow team members to view visual code diffs, discuss changes line-by-line, run automated tests, and suggest improvements before any new code gets merged into production, preventing bugs and conflicts.

---

### Task 6.4 — Build your Git command glossary

- `git init`: Initializes a brand new, empty Git repository in the current folder.
- `git status`: Checks the working tree and staging area to show which files were modified, untracked, or staged.
- `git add`: Adds specific modified or new files to the staging index in preparation for a commit.
- `git commit`: Permanently saves a snapshot of all staged changes to the local repository log.
- `git log`: Prints the commit history showing previous snapshots, commit hashes, and messages.
- `git branch`: Lists all existing branches, or creates a new branch pointer when a branch name is supplied.
- `git switch` (or `git checkout`): Switches the active working environment from one branch to another.
- `git push`: Uploads local commits from your computer up to a remote repository on GitHub.
- `git pull`: Fetches and merges new commits from the remote repository down into your current local branch.

## 5. Difficulties faced
Remembering whether `git checkout -b <branch>` or `git switch -c <branch>` is preferred in modern Git.

## 6. How I resolved them
Both achieve the exact same result, but `git switch -c` was introduced in newer versions of Git specifically for branching to make command syntax clearer.

## 7. Evidence / files
- `mission-06-git-github/README.md` (this file)
- Branch `update-about` created in repository

## 8. Commit details
- Branch: `main` (and feature branch `update-about`)
- Commit message: `Complete Git and GitHub collaboration mission`
