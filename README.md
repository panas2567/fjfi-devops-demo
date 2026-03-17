[Continuous integration pipeline](https://github.com/panas2567/fjfi-devops-demo/actions/workflows/ci-tests.yaml)

# Contribution guideline

To start contributing on this repository, create new branch locally based on the `main` branch.
The new branch's name should be in the following format:

- `feature/<initials>/fix-unit-tests-evaluate`

After making your changes, push them to remote:

- `git add .` (from project's root),
- `git commit -m "<commit message>"`
- `git push`

Once the remote branch is created, create a `pull request` to apply the changes to the `main` branch.

`Main` branch is protected and each PR needs at least one approval from the reviewers in order to be merged.

Try to use `semantic commits` convention. For reference check: [semantic commits](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).

# fjfi-devops-demo

Demonstration of the CI/CD routine

Steps to download the repo and set up the environment using command line (Powershell, Terminal):

- **Prerequisites**:
  - Git installed.
    - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    - Make sure the git binary or its parent directory is on your PATH environment variable.
    - Confirm with `git --version`.
  - uv installed.
    - [Install uv]([https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/))
- Get the project repository:
  - Navigate to the directory you want the repo to be stored in.
  - Clone the repo:
    - `git clone https://github.com/panas2567/fjfi-devops-demo.git`
- Simple env setup (with uv):
  - `uv sync` (creates `.venv`, installs dependencies, uses lockfile)
  - `uv run pytest` (or activate `.venv` and run tools as usual)
- Perform changes to the code:
  - Navigate to the project directory:
    - `cd fjfi-devops-demo`
  - Create your feature branch:
    - Replace the placeholder `<initials>` in the following line with your initials.
    - `git checkout -b feature/<initials>/ci-demo`
  - Open the project in your favorite IDE, e.g. PyCharm, or you can continue working from a text editor of your choice.
    - Recommended options:
      - [PyCharm](https://www.jetbrains.com/pycharm/) ([JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/))
      - [Cursor]([https://cursor.com/download](https://cursor.com/download))
      - [VS Code]([https://code.visualstudio.com/download](https://code.visualstudio.com/download))

## Setup virtual environment

**With uv (recommended):**

- Install uv, then in the project root run: `uv sync`
- uv uses `.venv` by default. Run tools with `uv run ruff check .`, `uv run ruff format .`, `uv run pytest`, or activate the venv:
  - Mac: `source .venv/bin/activate`
  - Win: `.\.venv\Scripts\activate`

## Fixing ruff warning

Commands to fix different linting errors.

- formatting errors:
  - `uv run ruff format .`
- other linting errors:
  - `uv run ruff --check . --fix`
- isort (import) errors:
  - `ruff check --select I --fix .`

