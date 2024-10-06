# Smart Mailbox

## Overview

**Smart Mailbox** is an IoT-enabled solution designed to enhance the convenience and security of traditional mail management systems.

## Running the Project on Your Device

### Prerequisites
Before running the project, make sure you have the following installed:
- **Node.js** (with npm) – You can download it from [here](https://nodejs.org/).

### Steps to Run the Project

1. **Clone the Repository**:

This repository uses Git hooks to streamline contributions. First, clone the repository and navigate to the project directory. Then to set up your environment, run the following commands:

```bash
git clone https://github.com/Iot-group39/smart-mailbox.git
cd smart-mailbox
./setup-git-hooks.sh  # For Linux or macOS
setup-git-hooks.cmd  # For Windows
```

2. **Install Frontend Dependencies**:
   Navigate to the `frontend` folder and install the dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. **Run the Frontend**:
   After the dependencies are installed, start the local development server:
   ```bash
   npm run dev
   ```

   This will launch the website on a local server. You can access it in your browser at:
   - Local URL: `http://localhost:5173/`
   

## Committing Your Changes

### Staging and Committing

All changes must be staged before committing for the code formatter to work. Use:

```bash
git add -A  # If you created new files or moved files around
git commit -am "Your commit message"  # If you only modified existing files
```

### Commit Message Format

Your commit messages should follow this format to ensure clarity and consistency:

- **Type**: Specify the type of change, such as `feat` (new feature), `fix` (bug fix), `docs` (documentation), `style` (code style changes), `refactor` (code changes that do not fix bugs or add features), `test` (adding or updating tests), or `chore` (minor tasks).
- **Scope** (optional): Indicate the area affected, such as `backend`, `device`, or `frontend`.
- **Description**: Provide a brief summary of the change (10 to 50 characters).

For example, a commit message might look like `feat(device): add mail detection`.

## Pushing to GitHub

After committing your changes, push them to the `main` branch of the remote repository using:

```bash
git push -u origin main
```

The `-u` flag sets the remote `main` branch as the default upstream branch for your local `main` branch, simplifying future push and pull operations.

**Important**: Avoid using `-f` (force push), as it can overwrite others' work and lead to data loss.
