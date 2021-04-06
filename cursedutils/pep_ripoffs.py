from.wrappers import execute_with
#PEP 3150 "given" status=deferred
class Given:
 def __init__(s,**k):([setattr(s,this,that)for this,that in k.items()],[setattr(s,this,getattr(s,this)())for this in dir(s.__class__)if hasattr(this,'__call__')and not this[0]=='_'])
def _pep3150_example(a=4,b=5,op=lambda x,y:x*y):
 """PEP 3150 example:
op(?.f, ?.g) given bound_a=a, bound_b=b in:
    def f():
        return bound_a + bound_b
    def g():
        return bound_a - bound_b
"""
 @print
 @lambda _: op(_.f, _.g)
 @execute_with(bound_a=a, bound_b=b)
 class evaluate(Given):
  def f(s):return s.bound_a + s.bound_b
  def g(s):return s.bound_a - s.bound_b

