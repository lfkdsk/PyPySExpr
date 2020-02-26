from py_sexpr.stack_vm.emit import module_code
from pypy_expr.visitor import PyPySExprVisitor
from pprintast import *
import dis
from typing import *


def code_runner(source: str, expect: List, **kwargs):
    visitor = PyPySExprVisitor()
    sexpr = visitor(source=source)
    xs = []
    exec(module_code(sexpr), dict(result=xs.append, print=print, *kwargs))
    print(f'source: {visitor._source}\nresult: {xs}')
    print('ast:')
    pprintast(source=visitor._source)
    assert xs == expect


# Test Binary

bin_op = """
result(1 + 2)
"""

code_runner(bin_op, [3])

bin_op = """
result(1.0 / 2.0)
"""

code_runner(bin_op, [0.5])

bin_op = """
result(1.0 * 2.0)
"""

code_runner(bin_op, [2])

bin_op = """
result('lfk' + 'dsk')
"""

code_runner(bin_op, ['lfkdsk'])

# Test Assign (single assign)
assign_op = """
x = 100
result(x)
"""
code_runner(assign_op, [100])

assign_op = """
x = (100,200)
result(x)
"""
code_runner(assign_op, [(100, 200)])

assign_op = """
x : str = "lfkdsk"
result(x)
"""
code_runner(assign_op, ["lfkdsk"])

# Control Flow
for_code = """
for i in range(0, 10):
    print(i)
"""
code_runner(for_code, [])

for_code = """
for i in (0, 10):
    print(i)
"""
code_runner(for_code, [])

# Define Functions

define_code = """
def lfkdsk(a):
    print(a)
    a
result(lfkdsk(1000))    
"""
code_runner(define_code, [1000])
define_code = """
def lfkdsk(a=2000):
    print(a)
    a
result(lfkdsk())    
"""
code_runner(define_code, [2000])

# Record Support

define_code = """
x = 100
def lfkdsk():
    {name: 1, value: x}
result(lfkdsk())    
"""
code_runner(define_code, [{"name": 1, "value": 100}])
