# -*- coding: latin-1 -*-

class Produto:
    def __init__(self, produto):
        self.produto = produto
        self.quantidade = []
    def nome_produto(self):
        return self.produto

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
       preco_prod.append(raw_input("Quanto é recebido pelo produto " + (produtos[i].nome_produto()) + ": "))          
   for i in range(0, num_recursos):
       disp_rec.append(raw_input("Quanto de " + nome_rec[i] + " está dísponínel: ")) 

if __name__ == "__main__":
    main()