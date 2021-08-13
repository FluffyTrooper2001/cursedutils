#PEP 3150 "given" status=deferred
class PEP3150_Given_MetaClass(type):
 def __init__(cls,name,parents,attrs):
  for name,attr in attrs.items():
    try:attrs[name] = property(attr)
    except Exception:pass
  super().__init__(name,parents,attrs)
class Given(metaclass = PEP3150_Given_MetaClas):
 def __init__(s,**k):[setattr(s,this,that)for this,that in k.items()]
def _pep3150_example(a=4,b=5,op=lambda x,y:x*y):
 """PEP 3150 example:
op(?.f, ?.g) given bound_a=a, bound_b=b in:
    def f():
        return bound_a + bound_b
    def g():
        return bound_a - bound_b
"""
 call = lambda*a,**k:lambda f:f (*a,**k)
 @call(bound_a=a,bound_b=b)
 class given(Given):
  def f(s):return s.bound_a + s.bound_b
  def g(s):return s.bound_a - s.bound_b
 return op(given.f,given.g)

