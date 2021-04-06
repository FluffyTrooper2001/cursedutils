__name__='__main__'
__package__="cursedutils"
from.pep_ripoffs import _pep3150_example
from.iostreams import cout
cout << _pep3150_example(
    input('Using code that renders pep 3150 useless, the following will be "given" to a suite of code.\nPlease enter an integer for a>'),
    input('now, b>'),
    eval('lambda x,y:'+input('finally, enter a function of x, y:'))
)
