from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um set com os pares de vértices não adjacentes
        '''
        l = set()
        for v1 in self.N:
            for v2 in self.N:
                duplaV1 = "{}-{}".format(v1, v2)
                duplaV2 = "{}-{}".format(v2, v1)

                if (duplaV1 not in l) and (duplaV2 not in l):
                    chave = False

                    for a in self.A:
                        if v1 != v2:
                            if v1 == self.A[a].getV1() and v2 == self.A[a].getV2():
                                chave = True
                            elif v1 == self.A[a].getV2() and v2 == self.A[a].getV1():
                                chave = True

                    if (chave == False) and (v1 != v2):
                        l.add("{}-{}".format(v1, v2))
        return l


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V in self.N:
            grau_vertice = 0

            for a in self.A:

                if self.A[a].getV1() == V:
                    grau_vertice += 1
                if self.A[a].getV2() == V:
                    grau_vertice += 1
            return grau_vertice

        else:
            raise VerticeInvalidoException

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a1 in self.A:
            for a2 in self.A:
                if self.A[a1] != self.A[a2]:
                    if (self.A[a1].getV1() == self.A[a2].getV1()) and (self.A[a1].getV2() == self.A[a2].getV2()):
                        return True
                    elif (self.A[a1].getV1() == self.A[a2].getV2()) and (self.A[a1].getV2() == self.A[a2].getV1()):
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        l = set()
        for a in self.A:
            if V == self.A[a].getV1() or V == self.A[a].getV2():
                l.add(a)
        return l

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if(self.vertices_nao_adjacentes() == set()) and (self.ha_laco() == False) and (self.ha_paralelas() == False):
            return True
        else:
            return False

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass
