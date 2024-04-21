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

Try to use `semantic commits` convention. For reference check: https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716



# fjfi-devops-demo
Demonstration of the CI/CD routine

Steps to download the repo and set up the environment using command line (Powershell, Terminal):

- Prerequisite: Python 3 installed.
  - Check which version is installed (if any at all): `python --version` or `python3 --version`.
  - If not, install Python 3.12, e.g. with `conda`, `pyenv` or a package manager.
    - Mac: https://docs.python-guide.org/starting/install3/osx/
    - Win: https://www.simplilearn.com/tutorials/python-tutorial/python-installation-on-windows
  - Make sure the Python binary is on PATH.
  - Check again.
  - Install the needed packages with `pip` from `requirements.txt`

  
- Prerequisite: Git installed.
  - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  - Make sure the git binary or its parent directory is on your PATH environment variable.
  - Confirm with `git --version`.


- Get the project repository:
  - Navigate to the directory you want the repo to be stored in.
  - Clone the repo:
    - git clone https://github.com/panas2567/fjfi-devops-demo.git

- Simple env setup:
  - `python3 -m venv venv`
  - `source ./venv/bin/activate`
  - `pip3 install pytest`

- Perform changes to the code:
  - Navigate to the project directory:
    - `cd fjfi-devops-demo`
  - Create your feature branch:
    - Replace the placeholder `<initials>` in the following line with your initials.
    - `git checkout -b <initials>/ci-demo`
  - Open the project in your favorite IDE, e.g. PyCharm, or you can continue working from a text editor of your choice.
    - Recommended: https://www.jetbrains.com/pycharm/

    
## Optional - setup virtual environment:
  - `pyenv install 3.12` 
  - `pyenv local 3.12`
    - Check with `python3 --version`, if it's not the `3.12`, then
      - on Mac run: `eval "$(pyenv init --path)"`
      - on Windows move the correct version to the top of the PATH environment variable.
        - Restart the command line.
  - `python3 -m venv .venv-dev`
  - Activate the `.venv-dev`:
    - Mac: `source .venv-dev/bin/activate`
    - Win: `. .\.venv-dev\bin\activate`
  - `pip3 install -r requirements.txt`
  - Check the correct installation in the venv with `pip freeze --local`.