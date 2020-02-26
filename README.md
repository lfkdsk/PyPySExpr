# PyPySExpr of [Python-Compiler-Tools](https://github.com/python-compiler-tools)

[![PyPI version](https://img.shields.io/pypi/v/pysexpr.svg)](https://pypi.org/project/pysexpr)
[![Build Status](https://travis-ci.com/thautwarm/PySExpr.svg?branch=master)](https://travis-ci.com/thautwarm/PySExpr)
[![codecov](https://codecov.io/gh/thautwarm/PySExpr/branch/master/graph/badge.svg)](https://codecov.io/gh/thautwarm/PySExpr)
[![MIT License](https://img.shields.io/badge/license-MIT-Green.svg?style=flat)](https://github.com/thautwarm/EBNFParser/blob/boating-new/LICENSE)

A general-purpose package for generate PySExpr from Python. 

See [documentation](http://htmlpreview.github.io/?https://github.com/thautwarm/PySExpr/blob/gh-pages/docs/py_sexpr/index.html).


## Installation

```shell
pip install pypysexpr
```


## Preview

```python
from pypy_expr.apis import py_to_sexpr
from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code

code = """
x = 100
def lfkdsk(x = 200):
    {"num": 100}
"""
sexpr = py_to_sexpr(code)

assert sexpr == block(
    assign_star('x', const(100)),
    define('lfkdsk', ['x'], record(num=100), const(200))
)
```
