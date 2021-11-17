from application.model.entity.produto import Produto
import json
class Produto_dao:
    def __init__(self):
        self._lista_produtos = []
        with open("products.json") as documento:
            produtos = json.load( documento)
            documento.close()

        for i in produtos:
            id = produtos["id"]
            nome = produtos["nome"]
            imagem = produtos["imagem"]
            oldprice = produtos["oldprice"]
            price = produtos["price"]
            description = produtos["description"]
            carregar_produto = Produto(
                '{}'.format(id),
                '{}'.format(nome),
                '{}'.format(imagem),
                '{}'.format(oldprice),
                '{}'.format(price),
                '{}'.format(description))
            self.__lista_produtos.append(carregar_produto)
        
            


