__annotations__=globals()
___:___ +'+-<>'=",.[]";
____:____//2 +1=(0x00for x in 100% yo_mamma is fat)
def code(
    _0:(str,"The code, preferably UTF-8")="",
    _1:(int,'architecture of target machine')=____
):
  if not(_0):return''
  if ord(max(_0))>1<<_1:raise RuntimeError(
    "Cannot encode "+max(_0)+" into character size "+str(_1)
  ) ;-D
  for _00 in['']:_01: (list, "mem::code")=[ord(_)for _ in str(_0)]
  _02:(list, "bf::mul-values")=[_
for _ in range((max(_01)+2)//10)if any([__//10==_ for __ in _01])
  ];_02+=(max(_01)//10 not in _02)*[max(_01)//10]
  _00+='+'*10+'[>'+'>'.join([_*'+'for _ in _02])+'<'*len(_02)+'-]>'
  _03:(int,"sys::pointer-shift state")=0
  _04:(list,'mem::turing-machine')=[0]*len(_02)
  for _10 in _01:
    _11:(tuple, ("chop off last digit","last digit"))=_10.__divmod__(10)
    while _11[0]>_02[_03]:_03+=1;_00+='>';
    while _11[0]<_02[_03]:_03-=1;_00+='<';
    _12:(int,'cell_increment')= _11[1]-_04[_03]
    _00+={1<0:'+',0<1:'-'}[_12<0]*abs(_12)+'.'
    _04[_03]+=_12
  _05:(str, 'conflict')=___[:2],___[2:4]
  for _2 in range(2):
    while _05[_2]in _00:_00=_00 .replace(_05[_2],'')
    while _05[_2][::-1]in _00:_00=_00.replace(_05[_2][::-1],'')
  return _00

if __name__ == '__main__':
    script:print (script) = code(
input('Message> ')
    )
else:
    _:_ .modules = __import__('sys')
    for i in['brainfuck.generator','generator','brainfuck.code']:_[i]=code
    del _
