"""Provides several ways to die, from raising an error to nuking the entire host process or device.
if :class: RecreationalMcNuke is ever instantiated, cancel its effects by using the abort function.
"""

from os import abort,system; system('')
class RecreationalMcNuke:#For recreational purposes only
 """Making an instance will do nothing.
deleting an instance will bomb your device.
exit the interpreter or use execute to bomb immediately.
Use provided abort function to cancel."""
 purposes = ('recreational',)
 def __del__(self):
  try:[self.__class__()for _ in range(128)]
  except BaseException:self.__class__()
 @classmethod
 def execute(cls):
  print('\x1b[0;48;2;0;0;255m :(                                              \n    Generating BlueScreen, please wait...        \n')
  cls()
def kill_python(*_):
 __import__('os').system("")or __import__('sys').stderr.write('\x1b[31mFatal Python error: _Py_Decessus: Python has died.\nPython runtime state: deceased\x1b[0m\r\n')
 from ctypes import*
 py_object.from_address(0).value = 69
try:from.wrappers import named_as as _named_as
except ImportError:from wrappers import named_as as _named_as
def raise_error(exception=_named_as('')(__import__('_locale')).Error,*args):raise exception(*args)
kill_all=nuke_pc=blue_screen_induction_protocol=lambda*_:[RecreationalMcNuke(),exit(0xC0000005)][1]
