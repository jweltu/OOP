from .livros import Livro
from .usuarios import Usuario
from .emprestimos import Emprestimo


def main():
    user1 = Usuario("Megurine Luka", 1)
    livro1 = Livro("O caçador de pipas", "Khaled Hosseini", 9780605024274)

    if livro1.status:
        livro1.status = False
        print(f"Você solicitou o emprestimo do livro {livro1.titulo} com sucesso.")
    
    else:
        print(f"O livro {livro1.titulo} não se encontra dísponível no momento.")
    
    print(f"---INFORMAÇÕES DO LIVRO--- \n\nNome do livro: {livro1.titulo} \nautor: {livro1.autor} \nisbn: {livro1.isbn}")
    print(f"---INFORMAÇÕES DO USUÁRIO--- \n\nNome: {user1.nome} \nid: {user1.idUser}")
