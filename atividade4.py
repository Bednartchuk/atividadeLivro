class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor1 = Autor("J.K. Rowling", "31 de julho de 1965")
autor2 = Autor("George Orwell", "25 de junho de 1903")

livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1)
livro2 = Livro("1984", autor2)

print(f"Livro: {livro1.titulo}, Autor: {livro1.autor.nome}, Data de Nascimento do Autor: {livro1.autor.data_nascimento}")
print(f"Livro: {livro2.titulo}, Autor: {livro2.autor.nome}, Data de Nascimento do Autor: {livro2.autor.data_nascimento}")
