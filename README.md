To get started

```
pip install virtualenv
virtualenv env
```

Activate the environment

```
source virtualenv/bin/activate

```

- Requirements
```
touch requirements.txt 
```


### Install

```
pip install -r requirements.txt

```


### TOx
- Tox acts as the virtual environment for test cases
```
[tox]
envlist = py38
skipsdist = True

[testenv]
deps = -rrequirements.txt
commands = 
    pytest -v
```

run

``` tox``` and ```pytest v ```