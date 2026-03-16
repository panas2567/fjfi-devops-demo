[![Continuous integration pipeline](https://github.com/panas2567/fjfi-devops-demo/actions/workflows/ci-tests.yaml/badge.svg?branch=main)](https://github.com/panas2567/fjfi-devops-demo/actions/workflows/ci-tests.yaml)

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

- Prerequisite: Python 3.12 and [uv](https://docs.astral.sh/uv/) (recommended) or pip.
  - Check which version is installed (if any at all): `python --version` or `python3 --version`.
  - If not, install Python 3.12, e.g. with `conda`, `pyenv` or a package manager.
    - Mac: [Install Python on macOS](https://docs.python-guide.org/starting/install3/osx/)
    - Win: [Install Python on Windows](https://www.simplilearn.com/tutorials/python-tutorial/python-installation-on-windows)
  - Make sure the Python binary is on PATH.
  - Check again.
  - **With uv:** Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run `uv sync` in the project root to create a venv and install dependencies from `pyproject.toml` and `uv.lock`.
  - **With pip:** Install the needed packages with `pip install -r requirements.txt`.

- Prerequisite: Git installed.
  - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - Make sure the git binary or its parent directory is on your PATH environment variable.
  - Confirm with `git --version`.

- Get the project repository:
  - Navigate to the directory you want the repo to be stored in.
  - Clone the repo:
    - `git clone https://github.com/panas2567/fjfi-devops-demo.git`

- Simple env setup (with uv):
  - `uv sync` (creates `.venv`, installs dependencies, uses lockfile)
  - `uv run pytest` (or activate `.venv` and run tools as usual)
- Alternative (with pip):
  - `python3 -m venv venv`
  - `source ./venv/bin/activate` (or `. .\venv\Scripts\activate` on Windows)
  - `pip3 install -r requirements.txt`

- Perform changes to the code:
  - Navigate to the project directory:
    - `cd fjfi-devops-demo`
  - Create your feature branch:
    - Replace the placeholder `<initials>` in the following line with your initials.
    - `git checkout -b <initials>/ci-demo`
  - Open the project in your favorite IDE, e.g. PyCharm, or you can continue working from a text editor of your choice.
    - Recommended: [PyCharm](https://www.jetbrains.com/pycharm/)

## Optional - setup virtual environment

**With uv (recommended):**

- Install uv, then in the project root: `uv sync`
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
