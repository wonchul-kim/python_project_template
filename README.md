# Template to start Python project with team members

## 1. Make a repository

- [x] README.md
- [x] .gitignore

## 2. Code style/format in the process of pre-commit

- [x] .pre-commit-config.yaml

  - [x] pre-commit-hooks
  - [x] pyupgrade
  - [x] isort
  - [x] yapf
  - [x] black
  - [x] mdformat
  - [x] autoflake
  - [x] flake8
  - [x] codespell
  - [x] docformatter

- Apply .pre-commit-config.yaml

  ```
  pre-commit install
  ```

  Then, pre-commit-config configuration will be defined in .git

## 3. unit tests

- Install

  ```
  pip install coverage pytest-cov
  ```

- Execute

  ```
  pytest --cov
  ```

## 4. Settings for a package

- [x] project folder with `__init__.py` including `__version__`
- [x] requirements.txt
- [x] LINCENSE
- [x] MANIFEST.in
- [x] setup.py / setup.cfg

#### To distribute/deploy a package

- Install the below

  ```
  pip install 'build[virtualenv]'
  ```

- Execute the below command to make package

  ```
  python -m build --wheel
  ```

  This is same to `python setup.py bdist_wheel`

  > reference: https://pypa-build.readthedocs.io/en/stable/

## 5. Docs

#### mkdocs

- Install

  ```
  pip install mkdocs
  ```

- Start mkdocs

  ```
  mkdocs new .
  ```

  or you can make mkdocs on each project fodler using `mkdocs new <project folder>`

- Select theme
  in the `mkdocs.yml`, you can define theme like the below:

  ```yaml
  theme:
  name: 'material'
  ```

  Or, you can use `ReadtheDocs` theme by `pip install mkdocs-rtd-dropdown` and then,

  ```yaml
  theme:
      name: 'material'
  ```

- Add each module's page in docs
  in the `docs/<page name>.md`, add the below

  ```
  ::: project.src.calculator
  ```

  Then, the docstrings written in the `project/src/calculator.py` will be displayed in the mkdocs page.

  Then, add that page in the `nav` in `mkdocs.yml`,

  ```
  nav:
    - main: index.md
    - project: project.md
    - calculation: calculation.md

  ```

  This will be displayed in the side-bar

- Serve locally

  ```
  mkdocs serve
  ```

  Then, access to `https://127.0.0.1:8000` or `https://localhost:8000`

- Deploy MKDocs pages *in the github*

  ```
  mkdocs gh-deploy
  ```

  Then, you can see the mkdocs pages at `https://<github ID>.github.io/<repository name>`

#### sphinx
