import random as _r;import sys as _sys
class Maybe:__bool__,__init__=lambda s:s.n*2*_r.random()>=1,lambda s,n:setattr(s,'n',n)
def self(n):
  @lambda f:setattr(f,'__code__',_sys._getframe(n+1).f_code)
  def wrapper(*a,**k):...
  return wrapper
def Switch():
    """python can't tell me I can't have a switch suite :/"""
    call=lambda*args,**kwargs:lambda f:f(*args,**kwargs)
    named_as=lambda n:lambda f:setattr(f,'__name__',n)or f
    @call()
    class case:
     def __init__(self): self.state, self.value =- 1, None
     def __getitem__(self, item):
      if self.state <- 0:raise SyntaxError("Cannot find matching switch") # __annotations__ hack only works in globals
      if self.value == item and not self.state:self.state=1;return(lambda f,*u,**ck:f(*u,**ck))
      else:return(lambda*No,**ne:None) # XD
    def switch(value):case.value,case.state = value,0
    @named_as('default')
    def otherwise(f,*u,**ck):
      if case.state <- 0 :raise SyntaxError("Cannot find matching switch")
      elif not case.state:case.state =- 1;f(*u,**ck)
    return switch, case, otherwise
# dot notation
hack=lambda victim:py_object.from_address(id(victim)+8)
class struct:
 __dims__,__list__,__dict__=(0,0),[],{}
 __bool__=lambda s:all(__dims__)
 def __init__(s,*a,**k):
    setattr=__builtins__.object.__setattr__
    getattr=__builtins__.object.__getattribute__
    setattr(s,'__dict__',k)	
    if a and a[0]in[[],{},()]or(isinstance(a[0],getattr(s,'__class__'))and not all(getattr(a[0],'__dims__'))):assert not k
    elif not a:setattr(s,'__dims__',(1,1))or k and(getattr(s,'__list__').append(k),setattr(s,'__dict__',k))or getattr(s,'__list__').append([])
    elif a[0].__class__ is s.__class__:setattr(s,'__list__',getattr(a[0],'__list__'))or setattr(s,'__dims__',getattr(a[0],'__list__'))
    elif len(a)==2 and getattr(a[1],__class__)is set:
      setattr(s,'__list__',[{a[0]:b}for b in a[1]])
      setattr(s,'__dims__',(1,len(getattr(s,'__list__'))))
    elif len(a)==1:
      try:setattr(s,'__dims__',(1,len(a[0])));setattr(s,'__list__',[dict(derp)for derp in a[0]])
      except:raise ValueError('object cannot be converted to a struct')
    else:
      getattr(s,'__list__').append({})
      for f,v in zip(a[::2],a[1::2]):getattr(self,'__list__')[0]|={f:v}
      getattr(self,'__list__')[0]|=k
    for d in getattr(s,'__list__')[::-1]:getattr(self,'__dict__').update(d)
 def __getattr__(s,a):
    setattr=__builtins__.object.__setattr__
    getattr=__builtins__.object.__getattribute__
    v=[d[a]if a in d else[]for d in getattr(s,'__list__')]
    try:        v ,=              (v)
    except:     v=__builtins__.set(v)
    if          v:        return  (v)
    elif a in getattr(s,'__dict__'):return getattr(s,'__dict__')[a]
    else:getattr(s,'__dict__').update({a:getattr(s,'__class__')()})
    return getattr(s,'__dict__')[a]
 def __call__(s,*x):
   if not len(x)-1:x=(1,x[0])
   x,y=(x[0]-1,x[1]-1)if all(x)else x
   return getattr(s,'__class__')([getattr(s,'__list__')[x*getattr(s,'__dims__')[1]+y]])
 @classmethod
 def bootstrap(c,__g={}):
  import attr
  try:assert __g
  except AssertionError as e:__g=e.__traceback__.tb_frame.f_back.f_globals
  @lambda s:setattr(c,'gulag',s)
  class gulag(metaclass=lambda*a:attr.s(type(*a))(hack(__g))):
   victim:type=attr.ib(dict)
   def __del__(self):hack(__g).value=self.victim
  @lambda __missing__:setattr(hack(globals()),'value',type('dict',(gulag.victim,),{'__missing__':__missing__}))
  def __missing__(self,key):
    try:return getattr(__builtins__,key)
    except:self[key] =_= struct()
    object.__setattr__(_,'__name__',key)
    return _
 __repr__=lambda s:f"""{object.__getattribute__(s,'__name__')} =
    struct {object.__getattribute__(s,'__dims__')[0]}x{object.__getattribute__(s,'__dims__')[1]}{''.join([chr(10)+a for a in object.__getattibute__(s,'__dict__')])}"""
 def __setattr__(self,n,v):
  if isinstance(v,(lambda:None).__class__):
    victim=__import__('ctypes').py_object.from_address(id(self)+8)
    victim.value=type("struct",(victim.value,),{n:v})
  elif isinstance(v,print.__class__):
    victim=__import__('ctypes').py_object.from_address(id(self)+8)
    victim.value=type("struct",(victim.value,),{n:lambda s,*a,**k:v(*a,**k)})#bound builtin behaviour
  else:getattr(self,'__dict__').update({n:v})

