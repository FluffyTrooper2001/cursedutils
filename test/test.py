import cursedutils

__all__=['cursed','iostreams','wrappers','ctx','main','death']
try:
  for sub in __all__:
    assert sub in dir(cursedutils)
except AssertionError:print(sub, 'failed')

from cursedutils.iostreams import*
from cursedutils.wrappers import *
from cursedutils.death import    *
from cursedutils.cursed import   *

try:
  for c in str(123345647389):
    switch: int(c)
    @case[1]
    def do():
        #include<iostreams>
        int.n.m
        cout < "python pretending to be c++" << "Enter a number:"
        cin >> n
        cout << "And another:"
        cin >> m
        cout < "Your new numbers are:"< 10*n+m <<' and '< 10*n*(m-2) < "H"
    @case[2]
    def do():
        try:raise_error()
        except __import__('_locale').Error: cout < 'death.py part 1: check'
        else: cout < "ERROR: death.py not murderous enough"
        cout < "e"
    case[3](print,'l')
    case[4](print,'o')
    @case[5]
    def do():cout << "Current directory: " <- cd and cout<" "
    @case[6]
    def do():cout << "Contents of cd: " <- ls and cout<"W"
    @case[7]
    def do():
        +File("kill.py") <"from cursedutils.death import kill_python"<<"kill_python()"<<''
        try:err = os.system("py -m kill")
        except: cout < "Crashed too hard for an exit code"
        else: assert cout << "Exit Code: " <= err
        assert not -File("kill.py")
        cout<'r'
    @case[8]
    def do():
        cout<chr(10*10)
    @otherwise
    def do():'!'>cout
except:cout<'FAILED'

