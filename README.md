# pygrunt

![PyPI](https://img.shields.io/pypi/v/pygrunt) ![PyPI - License](https://img.shields.io/pypi/l/pygrunt)

A minimal Terragrunt wrapper for Python.

## Usage
```python
from pygrunt import pygrunt as pg

pg.action('/path/to/files/', 'plan')
pg.action('/path/to/files/', 'apply')
```

## Installation

```
pip3 install pygrunt
```

## Requirements
* Terragrunt
* Terraform

## Compatibility
Built and tested with Python 3.8, and it should work on any version of Python 3.x.

## Authors

`pygrunt` was written by Conor Farrell `<conor dot farrell8 at gmail dot com>`.
