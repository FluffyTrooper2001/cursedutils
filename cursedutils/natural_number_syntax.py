class Cursed(float):
  class CursedCore:
      def __init__(self):self.value=Cursed(0.0,cc=self);self.n=0
      def __call__(self,n):self.n=(n/2 if n.i else n);return self
      def get_value(self):_=self.value;self.__init__();return Cursed(_,cc=self)
      def __bool__(self):self.value-=self.n/2;self.n=0;return False
  class Kwursed:
      _default={"point":lambda s,n:n.cc.__setattr__('point',True)or NotImplemented}
      def __init__(s,n="point"):
          if isinstance(n,str):s.__call__=s._default[n]
          elif hasattr(n,'__call__'):s.__call__=n.__call__
  def __init__(s,*_a,**_k):super().__init__()
  def __new__(c,a,b=0,cc=None):s=super().__new__(c,a);s.i=b;s.cc=cc;return s
  __mul__=lambda s,n:Cursed(super().__mul__(n),s.i,s.cc)
  __sub__=lambda s,n:Cursed((isinstance(n,Cursed)and n.i)and s*n or super().__add__(n*0.1**s._numdec()),cc=s.cc)
  __add__=lambda s,n:Cursed(super().__sub__(n),s.i,s.cc)
  __neg__=lambda s:Cursed(0.0,s.i,s.cc)+s
  _getstr=lambda s:super(float,s).__str__()
  _numdec=lambda s:0 if s._getstr().endswith('.0')else len(s._getstr().split('.')[1])+1
  __str__=lambda s:super(Cursed,s-s.cc.get_value()).__str__()
  __bool__=lambda s:not s.cc(s)
#  __and__ # outdated methods
#  def __getattr__(s,k):return Cursed(eval(s._getstr())+s.stuff[k]*0.1,s.i,s.cc)
  @classmethod
  def _bootstrap(_):
    cc=_.CursedCore()
    hundred=Cursed(100,1,cc);thousand=Cursed(1000,1,cc);million=Cursed(1000000,1,cc)
    billion=million*thousand;trillion=billion*thousand;quadrillion=billion*million;septillion=quadrillion*billion
    zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve=(Cursed(_,cc=cc)for _ in range(13));thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen=(Cursed(_,cc=cc)for _ in range(13,20));twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety=(ten*Cursed(_,cc=cc)for _ in range(2,10))
    a=one
    _.stuff = locals()
    return locals()
globals().update(Cursed._bootstrap())
