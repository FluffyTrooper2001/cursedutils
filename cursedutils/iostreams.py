import sys,os
class Str(str):__repr__=lambda s:"";__invert__=__pos__=__neg__=lambda s:s.__str__();__int__=lambda s:int(s);__str__=str
class File:
 """File object with intuitive, command-prompt-like syntactic sugar, without io blocking."""
 name=''
 # dunders
 __init__  =lambda s,f='':s.__setattr__('name',f.__str__())or s.__setattr__('__p',0)or setattr(s,'__r',False)
 __neg__   =lambda s:[os.remove(s.name),s.reconfigure('',seekable=False,closed=True)]and s
 __pos__   =lambda s:[open(s.name,'w').close()or s,s.reconfigure('w+',seekable=True)][0]
 __lt__    =lambda s,o:[s.write(str(o))]and s # [write]
 __lshift__=lambda s,o:[s.write([(h:=s.tell()),s.read()][1]+['\n',s.seek(h)][0]+o)]and s # [read, write]
 __gt__    =lambda s,o:[o.write(s.read())]and o # [read, write]
 __rshift__=lambda s,o:[o.write(o.read()+'\n'+s.read())]and o # [read, write]
 __le__    =lambda s,t:[(b:=s.read(t[0])+t[1]),(a:=s.read()),s.seek(0),s.write(b+a)]and s # [read, seek, write]
 __eq__    =lambda s,p:s.name==p.name# or s.read()==p.read() #<review>
 __ge__    =lambda s,t:t[1]<=(t[0],str(s)) # [__str__]
 __and__   =lambda s,o:s and o# []
 __or__    =lambda s,o:s or o # []
 __str__   =lambda s:s.read() # [read]
 __repr__  =lambda s:f'File({os.path.realpath(s.name)})' # [__init__]
 __int__   =lambda s:len([(f:=open(s.name)).read(),f.close()][0]) # [__init__]
 __bool__  =lambda s:os.path.exists(s.name) # [__init__] # file-like-methods
 def read(s,n =- 1):
  if not s.readable:return NotImplemented
  with open(s.name,'r') as f:f.seek(s.__p);n=n if n>0 else n and int(s);f.read(n);s.__p=f.tell()
 write=lambda self,s='':[(f:=open(self.name,'w')).write(str(s)),f.close()][0]if self.writable else NotImplemented # [__init__]
 readable,writable,seekable,closed=True,True,True,False # []
 seek=lambda s,p,m=0:setattr(s,'__p',p if not m else s.__p+p if m<0 else int(s)-p)if s.seekable else NotImplemented # [__int__]
 reconfigure=lambda s,d='r+',**k:[setattr(s,n,v)for n,v in({'readable':'r'in d or'+'in d,'writable':'w'in d or'+'in d or'a'in d,'seekable':True,'__r':'b'in d}|k).items()]
 # idk
 _CHUNK_SIZE,write_through=8192,False 
 raw=lambda s:setattr(s,'__r',True) # [__r]
 flush=lambda*a,**k:None # []
 close,open=lambda s:setattr(s,'closed',True),lambda s:setattr(s,'closed',False)
 fileno=lambda s:[(f:=open(s.name,'r')).fileno(),f.close()][0] # [__init__]
 buffer=type("None",(object,),{'__doc__':"Does not need a buffer"})() # []
@lambda f:f()
class std:
 """Initialises with stdout, stdin, stderr with default values at the sys settings
    std(*files) will make and return a new object, closing the previous handles if they're not accessable by sys
    -std        will input one line from stdin
    +std        will input one word from stdin
    ~std        will close all non-sys handles and return the __class__
    std << str  will write to stdout
    std <= str  will write error
    std >= f    will overwrite f with one line of input
    std >> f    will append one line of input to f
    std > (i,f) is equivalent to f < (i,-std)
    std < f     will pipe the contents of f to stdout
    std & str   will return  str if -std else ''
    std | str   will return -std if -std else str
    if std: f() will execute an expression if none of the handles are closed
    std == f    will compare two Terminal objects
    std ^  o    will exclusively compare one line of stdin and an object
    std %  o    is equivalent to -std % o
"""
 __init__  =lambda s,stdout=sys.stdout,stdin=sys.stdin,stderr=sys.stderr:[
  s.__setattr__('stdin',stdin if hasattr(stdin,'read')and stdin.readable()else open(str(stdin),'r')),
  s.__setattr__('stdout',stdout if hasattr(stdout,'write')and stdout.writable()else open(str(stdout),'w')),
  s.__setattr__('stderr',stderr if hasattr(stderr,'write')and stderr.writable()else open(str(stderr),'w'))
 ]and None;__call__=lambda s,*f:(~s)(*f);__neg__=lambda s:''.join(iter(lambda:s.stdin.read(1),'\n'));__pos__=lambda s:''.join(iter(lambda:s.stdin.read(1),' '))
 __lshift__=lambda s,o:[s.stdout.write(o.__str__())]and Str(o)
 __le__    =lambda s,o:[s.stderr.write(o.__str__())]and Str(o)
 __ge__    =lambda s,o:o<=-s;__rshift__=lambda s,o:o<<-s;__name__=str("std".__str__()).__str__()
 __gt__    =lambda s,o:o[1]<(o[0],-s)if hasattr(o,'__iter__')and isinstance(o[0],int)else o<-s;__getitem__=lambda s,o:getattr(s,o)
 __lt__    =lambda s,o:[s.stdout.write((c:=(f:=open(o.name,'r')).read())),f.close()]and Str(c)if hasattr(o,'f')else s<<-o
 __bool__  =lambda s:not any([s.stdout.closed(),s.stdin.closed(),s.stderr.closed()])
 __eq__    =lambda a,b:isinstance(b,a.__class__)and a.stdout==b.stdout and a.stdin==b.stdin and a.stderr==b.stderr;__ne__=lambda a,b:not a==b
 __invert__=lambda s  :[s.stdout not in[sys.stdout,sys.__stdout__]or s.stdout.close(),
  s.stdin not in[sys.stdout,sys.__stdout__,sys.stderr,sys.__stderr__]or s.stdout.close(),
  s.stderr not in[sys.stderr,sys.__stderr__,sys.stdout,sys.__stdout__]or s.stderr.close()]and s.__class__
 __and__   =lambda s,o:-s and o;__or__=lambda s,o:-s or o;__xor__   =lambda s,o:not o and -s or o;__mod__=lambda s,o:-s%o
 __repr__  =lambda s  :str(f"{s.__class__.__name__}({repr(s.stdout)},{repr(s.stdin)},{repr(s.stderr)})".__str__())
from time import sleep as _sleep
@lambda c:c()
class wait:
 __add__=__and__=lambda s,o:-s and+o
 __sub__=lambda s,o:-s and-s
 __neg__=lambda s:_sleep(1)
 __pos__=lambda s:_sleep(2)
 __invert__=lambda s:_sleep(0.1)
 __call__=__lshift__=__rshift__=__lt__=__gt__=__ge__=__le__=__eq__=__ne__=__mod__=__or__=__xor__=__matmul__=lambda s,o=1:_sleep(o)
@lambda f:f()
class delete:__lshift__=__rshift__=__le__=__lt__=__gt__=__ge__=__eq__=__ne__=__call__=lambda s,o:~o or s
@lambda f:f("\b"*4+"exit << EXITCODE",'\b'*6)
class exit(__import__('_sitebuiltins').Quitter):
 __repr__=__pos__=__call__=__lshift__=__rshift__=__le__=__lt__=__gt__=__ge__=__eq__=__ne__=lambda s,o=0:__import__('_sitebuiltins').Quitter(*"ab")(o)
 __invert__=lambda s:s(-1);__neg__=lambda s:s(1)
 __or__=lambda s,o:hasattr(o,'__call__')and[o()and+s]or o or s(o);__and__=lambda s,o:hasattr(o,'__call__')and[o()or+s]or(o and s(o))
quit=exit
@lambda c:c()
class cd:
 os=os;__call__=lambda s,n=None:n is None and os.getcwd()or os.chdir(n)or os.getcwd()
 __neg__=__invert__=lambda s:os.getcwd();__pos__=lambda s:os.path.realpath(-s)
 __gt__=__ge__=lambda s,o:o<=os.getcwd();__rshift__=lambda s,o:o<<os.getcwd()
 __lt__=lambda s,o:s<<[(f:=open(o.name)).read(),f.close()][0]; __repr__=lambda s:~s
 __le__=__lshift__=lambda s,d:os.chdir(d.__str__())or-s;__ne__=lambda a,b:not a==b
 __eq__=lambda s,d:os.path.realpath(os.getcwd())==os.path.realpath(d)
@lambda c:c()
class ls:
 __call__=lambda s,d="":os.listdir(d or~cd.__class__())+['.','..']
 __lt__=__le__=__lshift__=lambda s,d:s(d);__ge__=lambda s,f:f<=s();__rshift__=lambda s,f:f<<s;__gt__=lambda s,f:f<s
 __eq__=lambda a,b:a is b;__ne__=lambda a,b: a is not b
 __neg__=lambda s:os.listdir()+['.','..'];__pos__=lambda s:os.listdir('/')+['.'];__invert__=lambda s:s(~cd)
 __repr__=lambda s:'\n'.join([f'DIRECTORY IN {~cd.__class__()}:','.','..',*os.listdir(~cd.__class__())])+'\n'
cd.__dir__=lambda s:ls(-s)
__help__=dict(__call__="""help << topic for more detailed help\n
File(filename : str)   :: opens iostream channel to file with name filename
ls(dir : OPTIONAL str) :: lists directory contents
cd(dir : OPTIONAL str) :: sets or displays current working directory
delete(filename : str) :: deletes a file
exit(code : OPTIONAL str) exits with optional exit code or exit code 0
""",       File=   """File(filename) <= str :: overwrite file
File(filename) << str :: append to file
File(filename) < (int, str) :: insert str at int in file
-File(filename), ~File(filename) :: read file
+File(filename) :: wipe file
repr(File(filename)) :: read file (at terminal :: File(filename))
str(File(filename)) :: read file
bool(File(filename)) :: returns True if file exists and is not empty
File(filename) >= File(other) :: pipe contents to other file
File(filename) >> File(other) :: append contents to other file
File(filename) > (int, File(other)) :: insert contents in other file at int
""",       cd =   """-cd, ~cd, repr(cd), str(cd) :: return cd
+cd :: return absolute path
cd <<, <=, < dir : str :: set directory
cd >, >>, >= *args :: see : help>File : for more information
""",       ls =   """-ls, ~ls, repr(ls), str(ls) :: list directory
+ls :: list root directory
ls <<, <= str :: set directory
ls < File(filename) :: pipe file contents to change directory
ls >, >>, >= *args :: see help>File for more information
""",       delete="""delete <binop> File(filename) :: deletes file
""",       exit  ="""exit <binop> ec, exit(ec) :: exits with exit code ec
+exit, exit(), repr(exit) :: exits with exit code 0
-exit :: exits with error status
~exit :: exits with termination status
""",       std=std.__class__.__doc__)
@lambda c:c()
class help:__call__=__lshift__=__lt__=__le__=__gt__=__ge__=__rshift__=lambda s,n="":__help__[n or'__call__'];__invert__=__neg__=__pos__=__repr__=__str__=lambda s:s();__getattr__=lambda s,a:s(a);__setattr__=lambda a,b,c:c<<a(b)
int=type("statement",(int,),dict(__getattr__=lambda s,o:globals().update({o:type("Int",(globals()['__builtins__'].int,),dict(named_as=lambda self, name:setattr(self,"__name__",name)or self))(0).named_as(o)})or s,__call__=lambda s,*a:type("",(),{'__enter__':lambda s:a,'__exit__':lambda s,*b:True})()))()
cout=type('.',(),{'__repr__':lambda s:"\n","__lshift__":lambda s,o:print(o,end='')or s,'__lt__':print,'__le__':lambda s,o:print(end=o)or o,'__rrshift__':lambda s,o:s<<o})()
cin=type('..',(),{'__rshift__':lambda s,o:globals().update({o.__name__:o.__class__(input()).named_as(o.__name__)})})()

