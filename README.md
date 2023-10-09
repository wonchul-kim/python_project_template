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
```python -m build --wheel``` or ```python setup.py bdist_wheel```

    > reference: https://pypa-build.readthedocs.io/en/stable/

## 3. Consider code style/format

##  