from application.model.entity.produto import Produto
import json
class Produto_dao:
    def __init__(self):
        self.__produtos = []
        with open("products.json") as documento:
            produtos = json.load( documento)
            documento.close()

        for i in produtos:
            
            id = i['id']
            nome = i['name']
            imagem = i["image"]
            oldprice = i["oldPrice"]
            price = i["price"]
            description = i["description"]
            carregar_produto = Produto(
                '{}'.format(id),
                '{}'.format(nome),
                '{}'.format(imagem),
                '{}'.format(oldprice),
                '{}'.format(price),
                '{}'.format(description))
            self.__produtos.append(carregar_produto)


    def produtos_list(self):
        return self.__produtos


        
            


