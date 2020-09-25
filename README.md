## Project Title

> See our [Python Project Templates](https://github.com/sportsdatasolutions/python_project_template) project to ***understand*** and ***customise*** this clone-able template for yourself 💻 🐍 ⚡️ 🎉 🤝

```markdown
## First Timers - Fork this repo first!
```

```markdown
## Local Setup

#### 1. Clone your Fork to new local project
#### 2. Delete the ```.git``` folder
#### 3. Create new empty Github repo
#### 4. Clone new Github repo within local project (using dot expression ```.```)

$ git clone git@github.com:user_name/new_project.git .

#### 5. Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push

#### 6. Setup ```Pipfile``` for dependencies

$ pipenv install
```

```markdown
## Deepnote Setup

#### 1. Link your Fork to new Deepnote project
#### 2. Delete the ```.git``` folder
#### 3. Move project files out of the cloned folder and delete empty folder
#### 4. Create new empty Github repo
#### 5. Unlink old repo and link new repo
#### 6. Move new ```.git``` folder out of cloned folder and delete empty folder
#### 7. Open a Terminal and Git Add, Commit and Push

$ git add .
$ git commit -m "init"
$ git push

#### 6. Setup ```pipenv``` by editing code cell in ```init.ipynb``` and restarting the project machine:

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
