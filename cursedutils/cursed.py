import sys as _sys
class Maybe(metaclass=(lambda*_:type(*_)())):
    __bool__ = lambda _: bool(__import__("random").randint(0,1))
    __str__ = lambda _: str(bool(_))
    __getattribute__ = lambda _, v: bool(_).__getattribute__(v)

class EscapeSequence:
 def __new__(cls, *whatever):
     return type('EscapeSequenceType',(type,),{'__format__':cls._ANSI.__format__,'__str__':lambda s:cls._ANSI})(cls)
 _ANSI = '\x1b['
 set, get = '\x1b[s','\x1b[u'
 up,down,left,right='\x1b[A','\x1b[B','\x1b[D','\x1b[C'
 colours={a:f'\x1b[{b}m'for a,b in{
    'end':0,'bold':1,'italics':2,'_underline':3,'underline':4,
    'blink':5,'_blink':6,'invert':7,
    'off_white':30,
    'red':31,
    'green':32,
    'gold':33,
    'blue':34,
    'turquoise':35,
    'purple':36,
    'black':37,
    'pink':91,
    'bright_green':92,
    'yellow':93,
    'sky_blue':94,
    'cyan':95,
    'magenta':96,
    'grey':97,
    'white':90
 }.items()}
 colourise = colorize = lambda*rgb:f'\x1b[38;2;'+';'.join(rgb)+'m'
 newline, tab, NUL, BEL, CR, backslash, ESC = '\n\t\0\7\r\\\x1b'

def self(n):
  @lambda f:setattr(f,'__code__',_sys._getframe(n+1).f_code)
  def wrapper(*a,**k):...
  return wrapper

#borderline_truthiness = lambda n,a=1<<64:[
#    a-(a+(1<<10)+eval("2048.000000000000227373675443232059478759765625")),
#    a-(a+(1<<10)+eval("2048.000000000000227373675443232059478759765625"+'0'*2048+'1'))
#][bool(n)]<0 # sensitive gamminness detection

#pattern matching before it was cool
def Switch():
    """python can't tell me I can't have a switch suite :/"""
    call=lambda*_0,**_1:lambda _00:_00(*_0,**_1)
    named_as=lambda _0:lambda _1:setattr(_1,'__name__',_0)or _1
    @call()
    class case:
     tr=[]
     @property
     def args(sw,at):return at.tr
     def __setattr__(self, attr, value):
       if attr=='args':attr='tr'
       super().__setattr__(attr,value)
     def __init__(self): self.state, self.value =- 1, None
     def __getitem__(ire, item):
      if ire.state <- 0:raise SyntaxError("Cannot find matching switch") # __annotations__ hack only works in globals
      if ire.value == item and not ire.state:ire.state=1;return(lambda f,*u,**ck: f(*ire. tr,*u,**ck))
      else:return(lambda*No,**ne:None) # XD
    class switch(metaclass=lambda*a:type(*a)()):
      def __getattribute__(_,a):return getattr(case,a)
      def __getitem__(_,a):return _(a)
      def __enter__(self): return case
      def __exit__(self,*whatever):case.state=-1
      def __call__(_,_0):case.value,case.state=_0,0;return _
    @named_as('default')
    def otherwise(f,*u,**ck):
      if case.state <- 0 :raise SyntaxError("Cannot find matching switch")
      elif not case.state:case.state =- 1;f(*u,**ck)
    return switch, case, otherwise

#magic wrapper
class apply(metaclass=lambda*a:type(*a)()):
    class apply_0_base:
        self=wrapper=source=index=None;
        def __mul__(s,index):
            getattr=object.__getattribute__
            return getattr(s,'self')(lambda*a:getattr(s,'wrapper')(*a),getattr(s,'source'),index)
        def __call__(s,index):
            g=lambda a:object.__getattribute__(s,a)
            return g('self')(g('wrapper'),g('source'),index)
        def __getattribute__(s,attr):
            g=lambda a:object.__getattribute__(s,a)
            v=g('wrapper')(getattr(g('source'),attr))
            setattr(g('source'),attr,v);return v
        def __setattr__(s,attr,value):
            g=lambda a:object.__getattribute__(s,a)
            v=g('wrapper')(value);setattr(g('source'),attr,v)
            return v
    class apply_1_base(apply_0_base):
        def __mul__(s,source,index=None):
            object.__setattr__(s,'source',source)
            return object.__getattribute__(super(),'__mul__')(index)
        def __call__(s,source,index):
            object.__setattr__(s,'source',source)
            return object.__getattribute__(super(),'__call__')(index)
        __getattribute__=object.__getattribute__
        def __setattr__(s,attr,source):
            object.__setattr__(s,'source',source)
            return super().__getattribute__(attr)
    class apply_starred_base:
        self=source=index=wrapper=None;
        def __mul__(s,source,index=None):
            return s.self(lambda**k:s.wrapper(**k),source,index)
        def __getattribute(s,attr):
            v=s.wrapper(*getattr(s.source,attr))
            setattr(s.source,attr,v)
            return v
        def __setattr__(s,attr,value):
            v=s.wrapper(*value);setattr(s.source,attr,v)
            return v
        def __call__(s,source,index=None):
            return s.self(lambda*a:s.wrapper(*a),source,index)
    def __call__(self,wrapper,source=None,index=None):
        if[source,index]==[None,None]:
            return type("application",(self.apply_1_base,),locals())()
        if source is None and index is not None:
            source=__import__('sys')._getframe(1).f_globals
        if index is None:
            return type("application",(self.apply_0_base,),locals())()
        source[index]=wrapper(source[index])
        return source[index]
    def __mul__(self, _t):
        if type(_t)is list:raise TypeError("'apply*' function is not subscriptable")
        elif type(_t)is not tuple:raise SyntaxError("Was expecting function call at this time.")
        switch, case, default = Switch();
        switch(len(_t));
        @case [0]
        def result0():raise RuntimeError("'apply*' function takes at least one argument.")
        @case [1]
        def result1():
            wrapper,=_t
            return self(lambda*a:wrapper(*a))
        @case [2]
        def result2(index=None):
            wrapper, source = _t
            return (lambda*a:wrapper(*a)),source

class hack:
  def __new__(cls, a, *b):
    from ctypes import py_object as p
    return super().__new__(cls)if b else p.from_address(id(a)+8)
  @property
  def value(self):
      """Kept here just to keep pycharm happy."""
      from ctypes import py_object as p
      return p.from_address(id(self)+8).value
  @value.setter
  def value(self, v):
      from ctypes import py_object as p
      p.from_address(id(self)+8).value = v
  def __init__(self, *pairs):
    v = self.victims = []
    for i,j in zip(pairs[::2],pairs[1::2]):
      if i not in[k for k,_ in v]:v.append((i,hack(i).value))
      hack(i).value = j
  def __enter__(self):return self
  def __exit__(self, a, b, c):
    self.__del__()
    return a is b is c is None
  def __del__(self):
    for victim, prisoner in self.victims:
      hack(victim).value = prisoner

def test_hacker():
    with hack(True, int, False, int,type,type('type',(hack(type).value,),{'__getattribute__':print})):
        print (False, not 0, not 1)
        type. hello_world;
    print (False, not 0, not 1)

class Cell:
  _reg = {}
  def __new__(cls, victim):
    if id(victim)in cls._reg:return cls._reg[id(victim)]
    else:return super().__new__(cls)
  def __init__(self, prisoner):
    from ctypes import*
    type(self)._reg |= {id(prisoner):self}
    self.cell_contents = prisoner
    self._content_type = py_object.from_address(id(prisoner)+8).value
  def hack(self, new:type):
    from ctypes import*
    victim = py_object.from_address(id(self.cell_contents)+8)
    old, victim.value = victim.value, new
    return old
  def __del__(self):
    self.hack(self._content_type)
    del self._reg[id(self.cell_contents)]

# dot notation
def _bootstrap(*a):
  if __name__!='__main__':g=__import__('sys')._getframe(2).f_globals
  else:g=globals();
  a=[*a];victim=hack(g).value;a[2]|={'gulag':victim};struct=type(*a)
  class global_dict(victim):
    def __del__(self): print('exiting corrupted globals...')
    def __missing__(self, key):
      if key in dir(__builtins__):return getattr(__builtins__,key)
      else:
        new = struct()
        object.__setattr__(new, '__name__', key)
        return new
  hack(g).value = global_dict
  return struct
class struct(list,metaclass=_bootstrap):
  gulag:type = dict
  __name__ = globals().get('__name__','<string>')
  def __del__(self):hack(self).value=object.__getattribute__(self, 'gulag')
  def __repr__(self):
    getattr = object.__getattribute__
    __dict__ = getattr(self, '__dict__')
    __name__ = getattr(self, '__name__')
    return f"<struct '{__name__}' size={len(__dict__)}>"
  def __getattribute__(self, key):
    getattr = object.__getattribute__
    __class__ = type(self)
    __dict__ = getattr(self, '__dict__')
    __name__ = getattr(self, '__name__')
    if key not in [*dir(__class__),*__dict__]:
      self.__dict__[key] = new = __class__()
      object.__setattr__(new, '__name__', key)
      if key.startswith('__')and key.endswith('__'):
         hack(self).value = type('struct',(__class__,),{key:new,'__name__':__name__+'.'+key})
      return new
    return self.__dict__[key]
  def __setattr__(self, key, value):
    getattr = object.__getattribute__
    __class__ = getattr(self,'__class__')
    __dict__ = getattr(self, '__dict__')
    self.__dict__[key] = value
    if isinstance(value, struct) or issubclass(value.__class__, struct):
      object.__setattr__(struct, '__name__', getattr(self, '__name__')+'.'+key)
    if key.startswith('__')and key.endswith('__'):
      hack(self).value = type('struct',(__class__,),{key:value})
