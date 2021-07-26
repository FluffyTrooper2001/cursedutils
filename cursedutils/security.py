_dependancies = {'Thread':__import__('threading').Thread,
                 'defaultdict':__import__('collections').defaultdict,
                 'randint':__import__('random').randint}
def generate(k:int,*,sec:int=99999) -> int:
  a=[];assert sec.__class__ is int
  f=lambda n:a.append(int('9'*n)**sec);assert k.__class__ is int
  for i in str(k):_dependancies['Thread'](target=f,args=[int(i)]).start()
  while len(a)<len(k.__str__()):...
  return sum(a)
def decrypt(seed:int, KEY:list[int],sec:int=99999):
  mess=str(generate(seed,sec=sec))
  extract=lambda*a:[mess[i%len(mess)]for i in a]
  return int(str().join(extract(*KEY)))
class bf:
  def __init__(s,c:str):s.c=c
  def __int__(s):return int(''.join([t for t in s.c if t in'+-<>[],.']).translate(str.maketrans('+-<>.,[]','23456789')))
class quick_encode:
  _h=8;__index__=__int__=lambda s:int(s.r);__repr__=__str__=lambda s:str(int(s.r))
  def __init__(s,m:str):
    while 1<<s._h<ord(max(m)):s._h+=1
    r='1'*(s._h-8)*(s._h>8);b=[ord(c)for c in str(m)];d=[i for i in range((max(b)+2)//10)if any([t//10==i for t in b])];d+=[max(b)//10]
    r+='2'*10+'85'+'5'.join([t*'2'for t in d])+'4'*len(d)+'395';j=0
    for c in b:
      a = c.__divmod__(10)
      while a[0]>d[j]:j+=1;r+='5'
      while a[0]<d[j]:j-=1;r+='4'
      r+='2'*a[1]+'6'+'3'*a[1]
    _,*__=({_ and(r:=r[:-1])for _ in iter(lambda:r.endswith('3'),False)},
      {_ and(r:=r.replace('23',''))for _ in iter(lambda:'23'in r,False)},{_ and(r:=r.replace('32',''))for _ in iter(lambda:'32'in r,False)}
    );s.r=r;print({print(end={'2':'+','3':'-','4':'<','5':'>','6':'.','7':',','8':'[','9':']'}[i])for i in r if i not in['0','1']}and'')
def decode(n):
  l,a,o=len(s:=str(int(n))),_dependancies['defaultdict'](int),str();i=p=a[int()];c=8;t=0# turing machine for instruction reading
  while p<l:#halting state
    # update func scope
    def _2():a[i]+=1;a[i]%=1<<+c;return i,c,o,t#looped increment
    def _3():a[i]-=1;a[i]%=1<<+c;return i,c,o,t#looped decrement
    _4,_5=lambda:(+i+ 1,c,o,t),lambda:(+i- 1,c,o,t)#cell shift
    _6=lambda:(i,c,print(end=chr(a[i]))or o+chr(a[i]),t)#push char to stdout
    def _7():a[i]=ord(__import__('sys').stdin.read(1));return i,c,o,t#pull char from stdin
    _8,_9=lambda:(i,c,o,t+(not bool(a[i]))),lambda:(i,c,o,t-bool(a[i]))#conditional looping
    _0,_1=lambda:(i,c+1%32,o,t),lambda:(i,c-1%32,o,t)#cell size shift
    i,c,o,t=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9][int(s[p])]()if not t else(# interpret digit if t is in 0 state
      i,c,o,t -(t >+ int()and s[p]=='9')+(t <- int()and s[p]=='8')# find 'matching' bracket
    );p -= 2 *+ (t <- int()) -1#move pointer
    if l <+ p <- int():break#forced halt
  return type('invisible_list',(list,),{'__repr__':lambda s:''})([ord(k)for k in o])#don't echo machine-friendly return.
def encrypt(seed,m,sec=99999):
  """seed: an integer, m: encoded integer, sec: order of encryption integer"""
  mess=str(generate(seed,sec=sec));l,r,a=len(mess),_dependancies['randint'],[]
  for c in str(m):
    n=r(0,l)
    while mess[n]!=c:n+=1
    a+=[n]
  return a
def send(name:str, seed:int, message:str, *, sec:int):
  with open(name+'.py','w')as file:file.write('a='+str(encrypt(seed, int(quick_encode(message)), sec=sec)))
def get(name:str, seed:int, *, sec:int):decode(decrypt(seed, __import__(name).a, sec=sec))
def main():
  @print
  @decode
  @lambda f:decrypt(334467,f,sec=99999)
  @lambda f:print(f)or f
  @lambda f:encrypt(334467,f,sec=99999)
  @lambda c:quick_encode(c._)
  class o:_="Hello World!"
