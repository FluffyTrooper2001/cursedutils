"""Provides several ways to die, from raising an error to nuking the entire host process or device.
if :class: RecreationalMcNuke is ever instantiated, cancel its effects by using the abort function.
"""

from os import abort
class RecreationalMcNuke:
 """Making an instance will do nothing.
deleting an instance will bomb your device.
exit the interpreter or use execute to bomb immediately."""
 def __del__(self):
  try:[self.__class__()for _ in range(4)]
  except BaseException:self.__class__()
 @classmethod
 def execute(cls):cls()
def kill_python(*_):
 import sys,os;os.system("")or sys.stderr.write('\x1b[31mFatal Python error: _Py_MorsObitusDecessus: Python has died.\nPython runtime state: deceased\x1b[0m\r\n')
 def morte():
  try:sys.setrecursionlimit(99999);morte()
  except:morte()
 try:morte()
 except: - mors . obitus . decessus ( *_ )
from.wrappers import named_as as _named_as
def raise_error(exception=_named_as('')(__import__('_locale')).Error,*args):raise exception(*args)
kill_all=nuke_pc=blue_screen_induction_protocol=lambda*_:[RecreationalMcNuke(),exit(139)][1]
