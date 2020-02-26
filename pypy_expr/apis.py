from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
import ast

from pypy_expr.visitor import PyPySExprVisitor


def py_to_sexpr(source: str,
                name: str = "<unknown>",
                filename: str = "<unknown>",
                lineno: int = 1,
                doc: str = ""):
    visitor = PyPySExprVisitor()
    sexpr = visitor(source=source)
    return module_code(sexpr, name, filename, lineno, doc)
