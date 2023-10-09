# Template to start Python project with team members 

## 1. Make a repository 

- [x] README.md
- [x] .gitignore


## 2. Settings for a package 

- [x] project folder with `__init__.py` including `__version__`
- [x] requirements.txt
- [x] LINCENSE
- [x] MANIFEST.in
- [x] setup.py / setup.cfg

####  To distribute/deploy a package

- Install the below
    ```
    pip install 'build[virtualenv]'
    ```

- Execute the below command to make package
    ```
    python -m build --wheel
    ``` 

    This is same to ```python setup.py bdist_wheel```
    > reference: https://pypa-build.readthedocs.io/en/stable/

## 3. unit tests

- Install
    ```
    pip install coverage pytest-cov
    ```

- Execute
    ```
    pytest --cov
    ```

## 4. Docs

#### mkdocs 

- Install
    ```
    pip install mkdocs
    ```

- Start mkdocs
    ```
    mkdocs new .
    ```
    or you can make mkdocs on each project fodler using ```mkdocs new <project folder>```

- Select theme
    in the `mkdocs.yml`, you can define theme like the below:
    ```yaml
    theme:
    name: 'material'
    ```

    Or, you can use `ReadtheDocs` theme by ```pip install mkdocs-rtd-dropdown``` and then,
    ```yaml
    theme:
        name: 'material'
    ```

- Add modules' docs
    in the `docs/<page name>.md`, add the below
    ```
    ::: project.src.calculator
    ```

    Then, the docstrings written in the `project/src/calculator.py` will be displayed in the mkdocs page.

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
