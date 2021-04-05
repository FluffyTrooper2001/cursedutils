try:
 from.import*
 import __main__ as ctx
 from.import __main__ as main
 __import__('sys').modules['cursedutils']=type("cursed.module",(),globals())()
except ImportError:import cursed,death,wrappers,iostreams
