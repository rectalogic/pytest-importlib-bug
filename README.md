When using both `--doctest-modules` and `--import-mode=importlib` with pytest, it imports the same class as two different classes.

You can see the `id()` of the class imported in `test_google_workspace.py` is `140177692791520` and in `google_workspace.py` it is `140177692783968` - and then the assertion fails because the two `Event` classes are actually different.

Remove either of the above pytest options from `pyproject.toml` and tests pass.


```sh-session
$ poetry run pytest -s
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug, configfile: pyproject.toml
collecting ... /Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/google_workspace.py 140177692783968
/Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/tests/test_google_workspace.py 140177692791520
/Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/tests/test_google_workspace.py 140177692791520
collected 2 items

pybug/integration.py .
pybug/tests/test_google_workspace.py F

=================================== FAILURES ===================================
___________________________________ test_it ____________________________________

>   ???
E   AssertionError: assert <class 'pybug.integration.Event'> is Event
E    +  where <class 'pybug.integration.Event'> = getclass()

/Users/aw/Projects/cureatr/dev/cureatr/experiments/pybug/pybug/tests/test_google_workspace.py:9: AssertionError
=========================== short test summary info ============================
FAILED pybug/tests/test_google_workspace.py::test_it - AssertionError: assert...
========================= 1 failed, 1 passed in 0.07s ==========================
```

Also running the test in isolation passes:
```sh-session
$ poetry run pytest -s pybug/tests/test_google_workspace.py
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug, configfile: pyproject.toml
collecting ... /Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/google_workspace.py 140551538264096
/Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/tests/test_google_workspace.py 140551538264096
/Users/aw/Projects/cureatr/dev/cureatr/experiments/pytest-importlib-bug/pybug/tests/test_google_workspace.py 140551538264096
collected 1 item

pybug/tests/test_google_workspace.py .

============================== 1 passed in 0.02s ===============================
```