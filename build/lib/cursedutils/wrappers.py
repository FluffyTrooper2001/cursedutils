def Chain():
    """:return: cause, effect"""
    def cause(f):
        t=type("chained_function",(),{'__call__':lambda*a:lambda*a:None,'call':lambda s,*a:f.__call__(*a),'__code__':f.__code__,'__name__':f.__name__})()
        def decorator(F):_f=t.call;t.call = lambda*a,:F(*_f(*a));return t
        t.__setattr__('__call__',decorator)
        return t
    def effect(t):
      def wrapper(f):
        _f=lambda*a:f(*t.call(*a));_f.__name__,_f.__doc__=f.__name__,f.__doc__
        return _f
      return wrapper
    return cause, effect
cause, effect = Chain()
def named_as(name):
 def decorator(f):
  f.__name__=name
  return f
 return decorator
def self_reference(self):
 def wrapper(*a,**k):
   if'self'in globals():
      rollback=globals()['self']
   globals()['self']=self
   v = self(*a,**k)
   if'self'in globals()and'rollback'in locals():globals()['self']=locals()['rollback']
   return v
 return wrapper
execute=(execute_with:=lambda*u,**ck:lambda f:f(*u,**ck))()
@execute
def _funcutils():
 def_for=lambda iterabe:lambda f:lambda*u,**ck:[f(i,*u,**ck)for i in iterable]
 def_while=lambda*a:lambda f:lambda*u,**ck:{f(*u,**ck)for _ in iter(*a)}
 @execute_with()
 class def_if:
  def __init__(self):self.state=0
  def __call__(self,c):
    def decorator(f):
     if not c:self.state=0;return lambda*a,**k:None
     else:self.state=1;return f
 def def_elif(c):
     def decorator(f):
      if not c or def_if.state:return lambda*a,**k:None
      else:self.state=1;return f
     return decorator
 def def_else(f):
    if def_if.state:return f
    else:return lambda*a,**k:None
 return def_if,def_elif,def_else,def_for,def_while
def_if,def_elif,def_else,def_for,def_while=_funcutils
