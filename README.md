# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Tech Stack](#tech-stack)
  - [Collaborators](#collaborators)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 Python Coding Challenges <a name="about-project"></a>

Welcome Sienberg Students! Today we'll be exploring basic github functionality while working on python code challenges!
Record your own score using the rubric below, provide a link to git proving each one is completed.

Please note that AI tools CAN be used to explain topics, provide context, or resolve uncertainties.

DO NOT LET AI TOOLS WRITE YOUR CODE.

Points will be deducted for poor behavior: mean comments, frivolous use of `Request Changes`, ect... BE KIND TO EACH OTHER!

- [ ] Publish repository
  - [ ] Update README Collaborators
- [ ] Open a `Draft Pull Request` and ask for help from your teammates.
- [ ] Use Pull Request to Peer Review solutions
  - [ ] Identify an unhandled edge case.
    - [ ] Add a test case for the edge case.
  - [ ] Suggest an improvement to the current approach.
  - [ ] Suggest an alternate approach and discuss tradeoffs.
- [ ] Resolve a merge conflict.
- [ ] Add items to `Lessons_Learned.md`.
  - [ ] What was the team's methodology for working on problems?
  - [ ] What was the most difficult non-technical part of the project?
  - [ ] What non-technical skills helped the team work together better?
  - [ ] How did you best resolve differences of opinion?
  - [ ] What is something you want to get better at?


## 🛠 Tech Stack <a name="tech-stack"></a>
- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)


## Collaborators <a name="collaborators"></a>
- [Watson Blair](https://github.com/WatsonWBlair)


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- [ ] [python3](https://docs.python-guide.org/starting/install3/osx/)
- [ ] [github cli](https://github.com/cli/cli#installation)
- [ ] [github account](https://github.com/)
- [ ] [make for mac](https://formulae.brew.sh/formula/make) or [make for windows](https://gnuwin32.sourceforge.net/packages/make.htm)

Verify prerequisites by typing the following into the terminal:
```Shell
python3 --version # Python is installed
git --version # Github is installed
gh auth login # Sign into github
which make # make is installed
```

### Setup

Clone this repository to your desired folder:

```Shell
gh repo create <team_name> -p WatsonWBlair/git_together
```


### Install

Setup can be accomplished with:
```Shell
sudo make init
```

`make init` is an alias for the following shell commands:
```Shell
python3 -m venv env # initialize a python virtual environment
source env/bin/activate # start the virtual environment
pip3 install -r requirements.txt # install non-standard python libraries
```
If `make` does not work or produces errors, the above commands can be run individually in the terminal.
Some may require administrative privileges to execute successfully.

### Suggested Workflow

Use the following as a starting point for your teams workflow. Change any and every part of this proposed process to best suit the team.

```bash
# create a working branch for a given challenge
git checkout -b reverse-string 

# implement code to complete a challenge:
rm -f reverse-string/reverse_string.py
echo "def reverse_string(str):\n  return str[::-1]\n" > reverse-string/reverse_string.py

# verify that all test cases pass
pytest reverse-string

# Commit changes to your local branch
git commit -am 'solve: reverse-string'

# Update the remote branches git history to match the local branch
git push --set-upstream origin reverse-string

# Create a pull request and solicit peer review and approval
gh pr create --fill
```

Please note that by default your `main` branch will not be protected, and can be directly altered by any collaborator.