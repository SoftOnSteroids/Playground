def permuta(start, end=""):
    '''
    Crea un programa que sea capaz de generar e imprimir todas las 
    permutaciones disponibles formadas por las letras de una palabra.
    - Las palabras generadas no tienen por qué existir.
    - Deben usarse todas las letras en cada permutación.
    - Ejemplo: sol, slo, ols, osl, los, lso
    https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2336%20-%20PERMUTACIONES%20%5BMedia%5D/ejercicio.md
    '''
    if len(start) == 0: return [end]
    words= []
    for i in range(len(start)):
        words = words + permuta(start[:i]+start[i+1:], end+start[i:i+1])
    return words

def multiplica(a, b):
  '''
  Multiplica dos nros utilizando sólo el símbolo de suma.
  Considera valores negativos y 0.
  '''
  if a == 0 or b == 0:
    return 0
  r = 0
  for _ in range(abs(a)):
    r += b
  return -r if a < 0 else r

def max_min(arr:list[int]) -> list[int]:
  '''
  Return [max, min] without using python built-in functions
  and iterating the list only once.
  '''
  min = max = arr[0]
  count = 0
  for n in arr:
    count += 1
    max = n if n > max else max
    min = n if n < min else min
  return [max, min, count]

# Tests for max_min function
def test_max_min():
  assert max_min([3,5,7,0,-1,4,-5,10]) == [10, -5, 8]
  assert max_min([3,5,7,2,10]) == [10, 2, 5]
  assert max_min([3,5,7,0,-1,4,-5,10]) == [10, -5, 8]
  assert max_min([-2,0,23] ) == [23, -2, 3]

if __name__ == "__main__":
  print(permuta("abcd"))
  print(multiplica(-2, 20))
  print(max_min([3,5,7,0,-1,4,-5,10]))
  print(max_min([3,5,7,2,10]))
  test_max_min()