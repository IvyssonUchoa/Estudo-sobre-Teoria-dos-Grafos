from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

paraiba = MeuGrafo()

paraiba.adicionaVertice('C')
paraiba.adicionaVertice('E')
paraiba.adicionaVertice('P')
paraiba.adicionaVertice('T')
paraiba.adicionaVertice('M')
paraiba.adicionaVertice('Z')
paraiba.adicionaVertice('J')
paraiba.adicionaVertice('W')


paraiba.adicionaAresta('a1', 'J', 'C')
paraiba.adicionaAresta('a2', 'C', 'E')
paraiba.adicionaAresta('a3', 'C', 'E')
paraiba.adicionaAresta('a4', 'P', 'C')
paraiba.adicionaAresta('a5', 'P', 'C')
paraiba.adicionaAresta('a6', 'T', 'C')
paraiba.adicionaAresta('a7', 'M', 'C')
paraiba.adicionaAresta('a8', 'M', 'T')
paraiba.adicionaAresta('a9', 'T', 'Z')

print(paraiba.vertices_nao_adjacentes())

"""print(paraiba.grau('C')) #retornar 7
print(paraiba.grau('O')) #retornar erro, vertice não existe
print(paraiba.grau('W')) #retornar 0"""

"""for a in paraiba.A: #percorre o conjunto de arestas
     print(a) # Imprime o rótulo da aresta
     print(paraiba.A[a]) #Imprime o objeto aresta do indice a
     print(paraiba.A[a].getPeso())
     print(paraiba.A[a].getV1())
     print(paraiba.A[a].getV2())"""

"""for v in paraiba.N:
     print(v)"""

"""
l = set()
l.add() #adciona elementos
"""
