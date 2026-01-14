class Livro:
    def __init__(self, titulo: str, autor: str, isbn: int, status: bool=True):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = isbn
        self.status = status
    
    