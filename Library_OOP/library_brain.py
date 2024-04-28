class Livro():
    def __init__(self, titulo, id_livro):
        self.titulo = titulo
        self.id_livro = id_livro
        self.autor = autor
        self.disponibilidade = True

    def emprestar_livro(self):
        pass

    def retornar_livro(self):
        pass

class Usuario():
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []

    def usuario_pegar_livro(self):
        pass
    def usuario_devolver_livro(self):
        pass
    def listar_livros(self):
        pass

class Biblioteca():
    def __init__(self):
        self.lista_livros = []
        self.lista_usuarios = []

    def add_livro(self):
        pass

    def remover_livro(self):
        pass

    def registar_user(self):
        pass

    def encontrar_livro(self):
        pass

    def biblioteca_emprestar_livro(self):
        pass

    def biblioteca_receber_livro(self):
        pass

