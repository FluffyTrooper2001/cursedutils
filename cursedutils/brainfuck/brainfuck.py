chars = '+-<>.,[]'

def brainfuck(code,input=input):
    from collections import defaultdict as d
    l=input==__builtins__.input
    if not l:input=lambda i=1:input.pop(i-1)
    a,o=d(int),''
    i=p=t=0
    for c in iter(lambda:code[p],''):
        def __0(i,_):
            a[i]+=1
            a[i]%=256
            return i,_,0
        def __1(i,_):
            a[i]-=1
            a[i]%=256
            return i,_,0
        def __2(i,o):
            o+=chr(a[i])
            return i,o,0
        def __3(i,_):
            a[i]+=ord(input(1))%256
            return i,_,0
        f = [__0,__1,
             lambda i,_:(i+1,_,0),
             lambda i,_:(i-1,_,0),
             __2,__3,
             lambda i,o:(i,o,int(not a[i])),
             lambda i,o:(i,o,---bool(a[i])),
             lambda*_:(*_,0)][chars.find(c)]
        if t:
            t+=(c=='[')-(c==']')
        else:
            i,o,t=f(i,o)
        p+=1-2*(t<0)
        try:code[p]
        except IndexError:break
    return o,int(p!=len(code))

status = brainfuck('++++++++++[>+++>+++++++>++++++++>++++++++++>+++++++++++<<<<<-]>>++.-->>+.+++++++..-------->+This is a comment.-<<<<++.-->>+++++++.------->>+.+++.----<++++++++.--------.<<<+++.')
error = status[1] or print(status[0])
