import numpy as np
import math
import Distancias

#Calcula um objeto da base de dados, com todos os centroides, encontrando aquele que possui menor distancia, e retornando o grupo ao qual o objeto pertence
def menor_dist(centroids,obj):
  menor = float('INF')

  for i in range(len(centroids)):
    dist = Distancias.dist_euclidiana(centroids[i],obj)
    if  dist < menor:
      menor = dist
      group = i
  
  return group

#Recalcula os centroides, utilizando um vetor sum, para somar a posição de todos os objetos, e um vetor count para contar quantos objetos contribuiram para aquele valor
#de sum,servindo posteriormente para realizar a média dos dados, esse vetor contendo as médias ( novos centroides ) é retornado.
def recalc_centroids(centroids,df,groups):

  sum = np.zeros((len(centroids),len(df.values[0])))
  count = np.zeros(len(centroids))

  for i in range(len(df.values)):
    for j in range(len(df.values[0])):
      sum[groups[i]][j] = sum[groups[i]][j] + df.values[i][j]
    count[groups[i]] = count[groups[i]] + 1

  for i in range(len(count)):
    sum[i] = sum[i]/count[i]

  return sum

#Realiza 100 iterações, percorrendo todos os elementos e os colocando em grupos, apos isso, o algoritmo recalcula os centroides, até atingir 100 operações.
# Note que o vetor grupo, é um vetor, onde a posição do vetor corresponde ao id do objeto, e o seu valor corresponde ao grupo em que ele pertence.
def organiza_grupo(groups):
  new_groups = []
  for i in range(max(groups)+1):
    new_groups.append([])
  
  #print(max(groups))  
  #print(len(new_groups))
  for i in range(len(groups)):
    new_groups[groups[i]].append(i)
    
  return new_groups
  
def kMeans(df, n_groups):
    centroids_id = np.zeros(n_groups, dtype = np.int16)
    #print(centroids_id)

    for i in range(n_groups):
        centroids_id[i] = np.random.randint(1,len(df))

    centroids = np.zeros((n_groups,len(df.values[0])))
    #print(centroids)
    #print(len(centroids), len(centroids[0]))
    for i in range(n_groups):
        centroids[i] = df.values[centroids_id[i]]


    groups = np.zeros((len(df.values)),dtype = np.int16)

    for i in range(100):
        for j in range(len(df.values)):
            groups[j] = menor_dist(centroids,df.values[j])

        centroids = recalc_centroids(centroids,df,groups)

    groups = organiza_grupo(groups)
    return groups
