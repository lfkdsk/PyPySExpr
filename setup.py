from setuptools import setup, find_packages
from pathlib import Path

with Path('README.md').open() as readme:
    readme = readme.read()

version = "0.1"

setup(
    name='pypysexpr',
    version=version if isinstance(version, str) else str(version),
    keywords=
    "Python, LISP s-expressions, expression-first, compiler, bytecode, metaprogramming",
    description="Generate Best s-expression builder targeting Python bytecode with Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.5.0',
    url='https://github.com/lfkdsk/PyPySExpr',
    author='lfkdsk',
    author_email='lfkdsk@gmail.com',
    packages=find_packages(),
    entry_points={"console_scripts": []},
    install_requires=['attrs', 'pysexpr>=0.4.0'],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)