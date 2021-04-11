# pygrunt

![GitHub](https://img.shields.io/github/license/lithiumoxide/pygrunt) | ![GitHub contributors](https://img.shields.io/github/contributors/lithiumoxide/pygrunt)

A minimal Terragrunt wrapper for Python

## Usage
```python
from pygrunt import pygrunt as pg

pg.action('/path/to/files/', 'plan')
pg.action('/path/to/files/', 'apply')
```

## Requirements
* Terragrunt
* Terraform

## Compatibility
Built with Python 3.8

## Authors

`pygrunt` was written by `Conor Farrell <conor.farrell8@gmail.com>`.
