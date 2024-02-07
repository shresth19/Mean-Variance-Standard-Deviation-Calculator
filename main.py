import numpy as np

def calculate(input):
  if len(input) != 9:
    raise ValueError("List must contain nine numbers.")

  a = np.array(input).reshape(3,3)
  print(a)
  print(a.mean(axis=0), a.mean(axis=1), a.mean())

  cal = dict()
  cal['mean'] = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()]
  cal['variance'] = [a.var(axis=0).tolist(), a.var(axis=1)]
  cal['standard deviation'] = [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std()]
  cal['max'] = [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max()]
  cal['min'] = [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min()]
  cal['sum'] = [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum()]
  return cal

print(calculate([0,1,2,3,4,5,6,7,8]))



