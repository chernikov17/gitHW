from gcd import extended_gcd as exgcd
from egcd import egcd

def test(a,b):
    rez = exgcd(a,b)
    rez_t = egcd(a,b)

    assert rez == rez_t

test(10,20)
test(23523,1535)
test(2151546436,23534237)