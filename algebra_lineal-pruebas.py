import numpy as np
from numpy._typing import NDArray

def combinacion_lineal(escalares: list, vectores: list[NDArray]):
  v_comb = np.zeros(len(vectores[0]))
  for e, v in zip(escalares, vectores):
    v_comb = v_comb + np.array(e * v)
  print(v_comb)

def get_coefs_afin(quant:int, size:int, validate_sum:bool=False):
  coefs = []
  for _ in range(quant):
    rnd = np.random.random(2)
    rnd = np.linspace(min(rnd), max(rnd), size-1)
    coefs.append(np.append(rnd, 1 - sum(rnd)))

  if validate_sum:
    for i in range(quant):
      print(sum(coefs[i]))
  
  return coefs
def prod_escalar(vector1, vector2):
  # if type(vector1) != np.ndarray:
  vector1 = np.array(vector1)
  vector2 = np.array(vector2)
  print(vector1.dot(vector2))
  return sum(vector1 * vector2)

if __name__ == "__main__":
  combinacion_lineal([1,-1,1/2], vectores=[np.array([2,2,2]) for _ in range(3)])
  combinacion_lineal([1,-1,1/2], vectores=[np.array([2,2,2]) for _ in range(3)])
  print(get_coefs_afin(3, 3))
  print(prod_escalar([1,4,2], [5,3,2]))