## Project Title

> See our [Python Project Templates](https://github.com/sportsdatasolutions/python_project_template) project to ***understand*** and ***customise*** this clone-able template for yourself 💻 🐍 ⚡️ 🎉 🤝

```markdown
## First Timers - Fork this repo first!
```

```markdown
## Local Setup

#### 1. Create new empty Github repo using the ```Use this template``` button on your Fork
#### 2. Clone new Github repo. e.g.

$ git clone git@github.com:user_name/new_python_project.git new_python_project

#### 3. Setup ```Pipfile``` for dependencies (packages the project will depend on) e.g.

$ pipenv install jupyter pandas

#### 4. Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push
```

```markdown
## Deepnote Setup (Option 1)

#### 1. Create new Github repo using the ```Use this template``` button on your Fork
#### 2. Link your Github repo to a new Deepnote project
#### 3. Move all files and folders, including ```.git```, into project root and delete the empty folder
#### 4. Setup ```pipenv``` by editing the code cell in ```init.ipynb``` and restarting the project machine:

%%bash
# If your project has a 'Pipfile' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f Pipfile
  then
    sed -i '/jedi/d;/jupyter/d;' Pipfile
    pip install pipenv
    pipenv install
  else 
    pip install pipenv
    pipenv install
fi

#### 5. Optionally add additional customisation in new code cell and run the cell e.g. Git Aliases:

%%bash
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

#### 6. Open a Terminal and Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push
```

```markdown
## Deepnote Setup (Option 2)

#### 1. Duplicate this Deepnote Project: https://deepnote.com/project/41043ef0-40b2-438a-99f7-872138598685 (On the header ```Python Project (Template) > Duplicate project```).

#### 2. Create and Link a new empty Github repo to your new Deepnote project

#### 3. Move the ```.git``` folder into the Deepnote project root and delete the empty folder

#### 4. Open a Terminal and Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push
```

### Getting Started

> Place a more detailed description of your project, how it came about, inspiration, reading.

#### ```User Story```

> User Story for your project. Decribe what you solutions does, in a brief step by step story.

#### ```Dependencies```

> Instructions for installing project dependencies (packages the project will depend on).

#### ```Running```

> Instructions for running the solution.

#### ```Contributing```

> Instructions for contributing to the project. e.g. See [contributing.md](./contributing.md).
