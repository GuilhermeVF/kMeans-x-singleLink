import kMeans
import Distancias
import Validacao
import SingleLink
import ReadCSV

#---------------------------- Leitura Dados -----------------------------
print('Ola bem vindo')
print('-----------------------------------------------------')

path = input("Insira o caminho do arquivo CSV: ")
df = ReadCSV.read(path)

print(df)
print('')

n_groups = int(input("Insira o número de grupos desejados: "))

dist_matriz = Distancias.dist_all(df)

#----------------------------- K-Means -----------------------------------
grupos_kmeans = kMeans.kMeans(df, n_groups)

#----------------------------- SingleLink --------------------------------
grupos_singleLink = SingleLink.singleLink(dist_matriz, n_groups)

print('Grupos formados pelo k-means: ', grupos_kmeans)

print('')

print('Grupos formados pelo singleLink', grupos_singleLink)

#----------------------------- Validacao ---------------------------------
swc_kmeans = Validacao.SWC(dist_matriz, grupos_kmeans)
swc_singleLink = Validacao.SWC(dist_matriz, grupos_singleLink)

print('-------------------------------------------------')
print(' ')
print('SWC Kmeans: ', swc_kmeans)
print('SWC Single Link: ', swc_singleLink)


if swc_kmeans < swc_singleLink:
  print('Kmeans obteve um melhor resultado !!!')
elif swc_kmeans > swc_singleLink:
  print('Single Link obteve um melhor resultado !!!')
elif swc_kmeans == swc_singleLink:
  print('Os algoritmos empataram')
