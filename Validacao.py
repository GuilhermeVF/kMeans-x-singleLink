
def s_i (a,b):
  return (b - a)/max(a,b)
  
def a_i (cluster, dist_matriz, pos):
  total = 0
  
  for i in range(len(cluster)):
    if i != pos:
      total = total + dist_matriz[cluster[i]][pos]
      
  return total/len(cluster) 


def b_i(cluster, dist_matriz, elemento):
  total = 0
  
  for i in range(len(cluster)):
      total = total + dist_matriz[cluster[i]][elemento]
      
  return total/len(cluster)

def remove_duplicate_cluster(cluster, grupos):
  for i in range(len(grupos)):
    if grupos[i] == cluster:
      grupos.pop(i)
      return grupos
      break

  
def cluster_mais_prox(cluster, clusters, dist_matriz):
  menor_dist = []

  '''print(len(clusters))
  print(len(clusters[0]))
  print(len(clusters))'''

  for i in range(len(clusters)):
    menor_dist.append(99999)
  
  #print(menor_dist)
  for i in range(len(clusters)):
    if clusters[i] != cluster :
      for j in range(len(clusters[i])):
        for k in range(len(cluster)):
          #print(dist_matriz[clusters[i][j]][cluster[k]])
          if dist_matriz[clusters[i][j]][cluster[k]] < menor_dist[i]:
            menor_dist[i] = dist_matriz[clusters[i][j]][cluster[k]]
  	    
  menor = float('INF')    
  for i in range(len(menor_dist)):
     if menor_dist[i] < menor:
     	menor = menor_dist[i]
     	pos = i
  
  #print(pos)
  return pos     
     
def SWC(dist_matriz, clusters):
  total = 0
  for i in range(len(clusters)):
     pos = cluster_mais_prox(clusters[i], clusters, dist_matriz)
     for j in range(len(clusters[i])):
       a = a_i(clusters[i], dist_matriz, j)
       b = b_i(clusters[pos], dist_matriz, clusters[i][j])
       total = total + s_i(a,b)
  
  return total / len(dist_matriz)
