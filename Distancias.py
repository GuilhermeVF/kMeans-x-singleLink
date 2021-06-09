import math
import numpy as np

def dist_euclidiana(obj1,obj2):
  dist = 0

  if len(obj1) != len(obj2):
    return None;

  for i in range(len(obj1)):
    dist = dist + math.pow((obj1[i]-obj2[i]),2)

  dist = math.sqrt(dist) 
  return dist

def dist_all(df):
  
  size = len(df.values)
  dist_matriz = np.zeros((size,size))

  for i in range(size):
    for j in range(size):
      dist_matriz[i][j] = dist_euclidiana(df.values[i],df.values[j])

  return dist_matriz
