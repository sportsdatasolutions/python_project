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

#### 3. Setup ```Pipfile``` for dependencies e.g.

$ pipenv install jupyter pandas

#### 4. Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push
```

```markdown
## Deepnote Setup

#### 1. Create new Github repo using the ```Use this template``` button on your Fork
#### 2. Link your Github repo to a new Deepnote project
#### 3. Move all files and folders, including ```.git```, into project root and delete the empty folder
#### 4. Setup ```pipenv``` by editing code cell in ```init.ipynb``` and restarting the project machine:

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

#### 5. Open a Terminal and Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push
```

### Getting Started

> Place a more detailed description of your project, how it came about, inspiration, reading.

#### ```User Story```

> User Story for your project. Decribe what you solutions does, in a brief step by step story.

#### ```Dependencies```

> Instructions for installing project dependencies.

#### ```Running```

> Instructions for running the solution.

#### ```Contributing```

> Instructions for contributing to the project. e.g. See [contributing.md](./contributing.md).
