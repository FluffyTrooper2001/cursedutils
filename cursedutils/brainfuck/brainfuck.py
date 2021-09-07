import collections
def brainfuck(code: str):
    a, size =collections.defaultdict(int), 8
    state = pointer = position = 0

    def add(i):
        a[i] += 1
        a[i] %= 1 << size
        return i, 0

    def sub(i):
        a[i] -= 1
        a[i] %= 1 << size
        return i, 0

    def left(i):
        return i - 1, 0

    def rite(i):
        return i + 1, 0

    def push(i):
        print(end=chr(a[i]))
        return i, 0

    def pull(i):
        from sys import stdin
        _input = stdin.read
        a[i] = _input(1)
        return i, 0

    def loop(i):
        return i, +(not (a[i]))

    def close(i):
        return i, -(bool(a[i]))

    for char in iter(lambda: code[position]if position in range(len(code))else'', ''):
        instructions = {
            '+': add,
            '-': sub,
            '<': left,
            '>': rite,
            '.': push,
            ',': pull,
            '[': loop,
            ']': close
        }
        instruction = instructions.get(char, lambda i:(i,0))

        if state:
            state += (char=='[') - (char==']')
        else:
            pointer, state = instruction(pointer)

        position += 1 - 2 * (state < 0)

        if len(code) <= position < 0:
            break
    return len(code)==position


__name__ == '__main__' == brainfuck(
    "++++++++++[>+++>+++++++>++++++++>++++++++++>+++++++++++<<<<<-]>>++.-->>+.++++++"
    "+..-------->+.-<<<<++.-->>+++++++.------->>+.+++.----<++++++++.--------.<<<+++."
);print()

C='+-<>.,[]'
def l(s,b,q=input):
 l=q==input
 if not l:q=lambda i=1:q.pop(i-1)
 a,o,e=collections.defaultdict(int),'',256;i=p=t=0
 for c in iter(lambda:b[p],o):
  def _0(i,_):a[i]=(1+a[i])%e;return i,_,0
  def _1(i,_):a[i]-=1;a[i]%=e;return i,_,0
  def _2(i,o):o+=chr(a[i]);return i,o,0
  def _3(i,_):a[i]+=ord(q(1))%e;return i,_,0
  f=[_0,_1,lambda i,_:(i+1,_,0),lambda i,_:(i-1,_,0),_2,_3,lambda i,o:(i,o,not a[i]),lambda i,o:(i,o,-bool(a[i])),lambda*_:(*_,0)][C.find(c)]
  t+=t and(c=='[')-(c==']')
  else:i,o,t=f(i,o)
  try:p+=1-2*(t<0);b[p]
  except IndexError:break
 return o
@lambda c:c()
class brainfuck:__call__=__format__=l
__name__=='__main__'==print(f"{brainfuck:++++++++++[>+++>+++++++>++++++++>++++++++++>+++++++++++<<<<<-]>>++.-->>+.+++++++..-------->+This is a comment.-<<<<++.-->>+++++++.------->>+.+++.----<++++++++.--------.<<<+++.}")
