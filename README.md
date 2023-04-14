# fjfi-devops-demo
Demonstration of the CI/CD routine

Steps to download the repo and set up the environment using command line (Powershell, Terminal):

- Prerequisite: Python 3 installed.
  - Check which version is installed (if any at all): `python --version` or `python3 --version`.
  - If not, install Python 3.10, e.g. with `conda`, `pyenv` or a package manager.
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


- Perform changes to the code:
  - Navigate to the project directory:
    - `cd fjfi-devops-demo`
  - Create your feature branch:
    - Replace the placeholder `<initials>` in the following line with your initials.
    - `git checkout -b <initials>/ci-demo`
  - Open the project in your favorite IDE, e.g. PyCharm, or you can continue working from a text editor of your choice.
    - Recommended: https://www.jetbrains.com/pycharm/

    
## Optional - setup virtual environment:
  - `pyenv install 3.10` 
  - `pyenv local 3.10`
    - Check with `python3 --version`, if it's not the `3.10`, then
      - on Mac run: `eval "$(pyenv init --path)"`
      - on Windows move the correct version to the top of the PATH environment variable.
        - Restart the command line.
  - `python3 -m venv local/.venv-dev`
  - Activate the `.venv-dev`:
    - Mac: `source local/.venv-dev/bin/activate`
    - Win: `. .\local\.venv-dev\bin\activate`
  - `pip3 install -r requirements.txt`
  - Check the correct installation in the venv with `pip freeze --local`.