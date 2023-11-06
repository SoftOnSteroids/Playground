"""
Different ways to calculate Fibonacci
"""
## This is easy to read and needs memoization to be efficient
import sys
import unittest
sys.setrecursionlimit(10**6)

def calc_fibonacci_iterable(n: int, memo:dict={}) -> int:
    if len(memo) == 0:
        memo = {0:0, 1:1}
    try:
        return memo[n]
    except:
        memo[n] = calc_fibonacci_iterable(n-1, memo) + calc_fibonacci_iterable(n-2, memo)
        return memo[n]
    
# This is a faster way and more eficient
def calc_fibonacci(n: int) -> int:
    """
    Calculate fibonacci of a given number: int
    returns: int or None
    """
    if n==0 or n==1:
        return n
    prev = 0
    answer = 1
    for _ in range(n-1):
        next = answer
        answer += prev
        prev = next
    return answer

def calculate_fibo() -> None:
    num = input("Ingrese un número entero positivo: ").strip()
    try:
        assert num.isdecimal(), "Debe ingresar un número entero positivo"
        num = int(num)
    except AssertionError as e:
        print(e)
        return calculate_fibo()
    f = calc_fibonacci
    # f = calc_fibonacci_iterable
    print (f"Fibonacci de {num} calculado con f: {f.__name__} es: {f(num)}")

class TestFibonacci(unittest.TestCase):
    def __init__(self, fibo_f, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fibonacci = fibo_f
  
    def test_fibonacci_zero(self):
        self.assertEqual(self.fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(self.fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)
        self.assertEqual(self.fibonacci(4), 3)
        self.assertEqual(self.fibonacci(5), 5)

    def test_fibonacci_large_numbers(self):
        self.assertEqual(self.fibonacci(100), 354224848179261915075, "Should be 354224848179261915075")
        self.assertEqual(self.fibonacci(15), 610)
        self.assertEqual(self.fibonacci(20), 6765)
  
    def runTest(self) -> None:
        self.test_fibonacci_zero()
        self.test_fibonacci_one()
        self.test_fibonacci_small_numbers()
        self.test_fibonacci_large_numbers()

  # print(f"fibonacci(100): {fibonacci(100)}")
if __name__ == "__main__":
    # print(calc_fibonacci_iterable(19411))
    # calculate_fibo()

    suite = unittest.TestSuite()
    suite.addTest(TestFibonacci(fibo_f=calc_fibonacci))
    suite.addTest(TestFibonacci(fibo_f=calc_fibonacci_iterable))
    unittest.TextTestRunner(verbosity=2).run(suite)