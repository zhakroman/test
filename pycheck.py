### 1

# 
# python 2.7:
#  
#   xrange - возвращает xrange-object, который является итерируемым объектом, 
#   реализующим стратегию lazy evaluation для неизменяемой последовательности
#   целых чисел в заданном диапазоне с шагом k, тем самым эффективно использует 
#   память, возвращая значения по требованию, в отличие от range, которая возвращает 
#   сразу всю последовательность в виде списка:
# 
#   from pympler import asf
#   obj = xrange(1, 100), range(1, 100)
#   map(asf.asizeof, obj) # [48, 4168] <=> ['iterable with LE', 'list']
#

### 2 

# The generator of the Fibonacci numbers
# @param  {N|int}: number 
# @return {Object|generator}

def fibonacci_generator(n):
    if n < 0:
        raise ValueError('n >= 0 but got %i' % n)
    previous, current = 0, 1
    for i in range(0, n):
        yield current
        current, previous = current + previous, current

import unittest
import types

class TestFibonacciGenerator(unittest.TestCase):

    def setUp(self):
        # alias
        self.f = fibonacci_generator
        # real seq: Fn = Fn-1 + Fn-2
        self.arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

    def test_err(self):
        values = self.f(-5)
        # to get an err before yielding - can be added extra wrap
        self.assertRaises(ValueError, next, values)

    def test_seq(self):
        self.assertSequenceEqual(list(self.f(15)), self.arr[:15])
        # if n = 0: return empty. 0 can be omitted
        self.assertSequenceEqual(list(self.f(0)), [])

    def test_type(self):
        # is generator
        self.assertIsInstance(self.f(5), types.GeneratorType)

if __name__ == '__main__':
    unittest.main()
