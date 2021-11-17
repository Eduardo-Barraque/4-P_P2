class Produto:
    def __init__( self, id:int, nome:str, imagem:str, oldprice:int, price:int, description:str,):
        self.__nome = nome
        self.__id = id
        self.__imagem = imagem
        self.__oldprice = oldprice
        self.__price = price
        self.__description = description
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def imagem(self):
        return self.__imagem
    @imagem.setter
    def imagem(self, value):
        self.__imagem = value

    @property
    def oldprice(self):
        return self.__oldprice
    @oldprice.setter
    def oldprice(self, value):
        self.__oldprice = value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        self.__description = value