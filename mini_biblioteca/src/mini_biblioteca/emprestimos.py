from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, status: bool=True):
        self.livro = livro
        self.usuario = usuario
        self.status = status
        