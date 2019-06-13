# -*- coding: latin-1 -*-
from gurobipy import *

class Produto:
    def __init__(self, produto):
        self.produto = produto
        self.quantidade = []
        self.preco = 0
        self.minimo = 0.0
        self.maximo = GRB.INFINITY
    def nome_produto(self):
        return self.produto
    def set_quantidade(self, quantidade):
        self.quantidade.append(quantidade)
    def set_preco(self, preco):
        self.preco = preco
    def get_preco(self):
        return self.preco
    def get_quantidade(self, index):
        return self.quantidade[index]
    def set_minino(self, min):
        self.minimo = min
    def set_maximo(self, max):
        self.maximo = max
    def get_minimo(self):
        return self.minimo
    def get_maximo(self):
        return self.maximo

def mixproducao(num_produtos, num_recursos, produtos, disp_rec):
    m = Model("mixproducao")
    variaveis = []
    obj_funcao = LinExpr()
    for i in range(0, num_produtos):
        variaveis.append(m.addVar(produtos[i].get_minimo(), produtos[i].get_maximo(), 0.0, GRB.CONTINUOUS , produtos[i].nome_produto(), None))
    i = 0
    for v in variaveis:
        obj_funcao += (v * produtos[i].get_preco())
        i += 1
    m.setObjective(obj_funcao, GRB.MAXIMIZE)
    
    for y in range(0, num_recursos):
        obj_restricao = LinExpr()
        i = 0
        for v in variaveis:
            obj_restricao += (v * produtos[i].get_quantidade(y))
            i += 1
        m.addConstr(obj_restricao, GRB.LESS_EQUAL, disp_rec[y], "c" + str(y))
    
    m.optimize()
    
    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

def main():
   num_produtos = input("Digite o numero de produtos: ")
   num_recursos = input("Digite o numero de recursos: ")
   produtos = []
   nome_rec = []
   preco_prod = []
   disp_rec = []

   for i in range(0, num_produtos):
       produtos.append(Produto(raw_input("Qual o nome do produto "  +str(i+1) + ": ")))
   for i in range(0, num_recursos):
       nome_rec.append(raw_input("Qual o nome do recurso "  +str(i+1) + ": ")) 
   for i in range(0, num_produtos):
       produtos[i].set_preco(input("Quanto é recebido pelo produto " + (produtos[i].nome_produto()) + ": "))          
   for i in range(0, num_recursos):
       disp_rec.append(input("Quanto de " + nome_rec[i] + " está dísponínel: ")) 
   for i in range(0, num_produtos):
       for y in range(0, num_recursos):
              produtos[i].set_quantidade(input("Quanto de " + nome_rec[y] + " é usado em " + produtos[i].nome_produto() + " :"))
   
   escolha_minima = raw_input("Os produtos terao producao minima?")
   escolha_maxima = raw_input("Os produtos terao producao maxima?")

   if(escolha_minima == "sim"):
       for i in range(0, num_produtos):
           produtos[i].set_minino(input("Qual o minimo de producao para " + (produtos[i].nome_produto()) + ": "))

   if(escolha_maxima == "sim"):
       for i in range(0, num_produtos):
           maximo = input("Qual o maximo de producao para " + (produtos[i].nome_produto()) + ": ")
           if(maximo >= 0 ):
               produtos[i].set_maximo(maximo)

   mixproducao(num_produtos, num_recursos, produtos, disp_rec)

if __name__ == "__main__":
    main()