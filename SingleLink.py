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

def pos_menor_dist (dist_matriz):
  menor = float('INF')
  for i in range(len(dist_matriz)):
    for j in range(i):
      if dist_matriz[i][j] < menor and i != j:
        menor = dist_matriz[i][j]
        pos = (i,j)
  return pos

def arruma_valores(dist_matriz, pos):
  pos1, pos2 = pos

  for i in range(len(dist_matriz)):
    if i != min(pos1,pos2):
      #print(min(dist_matriz[i][min(pos1,pos2)], dist_matriz[i][max(pos1,pos2)]))
      dist_matriz[i][min(pos1,pos2)] = min(dist_matriz[i][min(pos1,pos2)], dist_matriz[i][max(pos1,pos2)])
      dist_matriz[min(pos1,pos2)][i] = min(dist_matriz[i][min(pos1,pos2)], dist_matriz[i][max(pos1,pos2)])

  return dist_matriz

def verifica_pos(lista, elemento):
  pos = -1

  for i in range(len(lista)):
    for j in range(len(lista[i])):
      if lista[i][j] == elemento[0]:
        pos = i

  return pos

def verifica_valores(lista, pos):
  val1 = lista[pos[0]]
  val2 = lista[pos[1]]

  return val1, val2

def add_grupo(grupos, pos):
  
  val1, val2 = verifica_valores(grupos, pos)
  i = verifica_pos(grupos, min(val1, val2))
  k = verifica_pos(grupos, max(val1, val2))
  #print(i,k)

  for j in range(len(grupos[max(i,k)])):
    grupos[min(i,k)].append(grupos[max(i,k)][j])

  del grupos[max(i,k)]

  return grupos

def debug (matriz):
  for k in range(len(matriz)):
    count = 0
    for c in range(len(matriz)):
      if matriz[k][c] == 0:
        count = count + 1
    print(count)    
    if count > 1:
      print("ERRORR -----------------------############")
      return k,c
  return -1
    
def singleLink(dist_matriz, n_groups):
  grupos = []

  for i in range(len(dist_matriz)):
    grupos.append([i])

  #print(grupos)
  #print(dist_matriz)
  count = 0
  while len(dist_matriz) > 1 and len(grupos) > n_groups:
    pos = pos_menor_dist(dist_matriz)
    dist_matriz = arruma_valores(dist_matriz, pos)
    dist_matriz = np.delete(dist_matriz, max(pos), 0)
    dist_matriz = np.delete(dist_matriz, max(pos), 1)

    grupos = add_grupo(grupos, pos)

  return grupos

