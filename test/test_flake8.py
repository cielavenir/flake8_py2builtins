from sys import version_info
from pytest import mark
from ast import parse
from flake8_py2builtins.checker import Py2BuiltinsChecker

def test_positive():
    tree = parse('''
True
''')
    violations = list(Py2BuiltinsChecker(tree).run())
    assert len(violations) == 0

def test_StandardError():
    tree = parse('''
try:
    pass
except StandardError as e:
    pass
''')
    violations = list(Py2BuiltinsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('IIB010 ')

def test_basestring():
    tree = parse('''
isinstance('', basestring)
''')
    violations = list(Py2BuiltinsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('IIB010 ')

