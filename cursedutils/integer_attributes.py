hack = lambda victim:__import__('ctypes').py_object.from_address(id(victim)+8)
class obj:
    def __repr__(self):
        return'<|'+hex(id(self))+'|>'
class derp(hack(int).value):
    gulag = [hack(int).value]
    __del__ = lambda s:setattr(hack(s),'value',s.gulag[0])
    _DATA = __import__('collections').defaultdict(obj)
hack(__builtins__.int).value = derp
@__import__('fishhook').hook_cls(int)
class Int:
    @property
    def attr(self):
        return int._DATA[self]
    def _update(self,value):
        int._DATA[self] = value
    def __call__(self,*a):
        if not a:return self.attr
        else:self._update(*a);return self
    def __iter__(self):return[__builtins__.int(c)for c in str(self)].__iter__()


a = 420
a(69)and[print(i.attr)for i in 1234567890]and print(a.attr)