class Livro():
    def __init__(self, titulo, id_livro):
        self.titulo = titulo
        self.id_livro = id_livro
        self.autor = autor
        self.disponibilidade = True

    def emprestar_livro(self):
        if self.disponibilidade:
            self.disponibilidade = False
            return True
        return False  # Retorna False se o livro não estiver disponível para empréstimo

    def retornar_livro(self):
        self.disponibilidade = True

class Usuario():
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []

    def usuario_pegar_livro(self,livro):
        if livro.emprestar_livro():
            self.livros_emprestados.append(livro)
            return True
        return False

    def usuario_devolver_livro(self,livro):
        if livro in self.livros_emprestados:
            livro.retornar_livro()
            self.livros_emprestados.remove(livro)
            return True
        return False

    def listar_livros(self):
        return [livro.titulo for livro in self.livros_emprestados]

class Biblioteca():
    def __init__(self):
        self.lista_livros = []
        self.lista_usuarios = []

    def add_livro(self,titulo, autor,livro_id):
        if livro_id in self.lista_livros:
            print("ID ja usado, tente novamente")
        else:
            novo_livro = Livro(titulo, autor, livro_id)
            self.lista_livros.append(novo_livro)
            print(f"Livro '{titulo}' adicionado com sucesso!")

    def remover_livro(self,livro):
        if livro in self.lista_livros:
            self.lista_livros.remove(livro)

    def registar_user(self,nome, user_id):
        if any(user.id == user_id for user in self.lista_usuarios):
            print("ID já usado, tente novamente.")
        else:
            novo_usuario = Usuario(nome, user_id)
            self.lista_usuarios.append(novo_usuario)
            print(f"Usuário '{nome}' registrado com sucesso!")

    def encontrar_livro(self,livro):
        if livro in self.lista_livros:
            return True
        return False #O livro não existe no catalogo

    def biblioteca_emprestar_livro(self, livro_id, user_id):
        livro = next((l for l in self.lista_livros if l.id == livro_id and l.disponibilidade), None)
        usuario = next((u for u in self.lista_usuarios if u.id == user_id), None)
        if livro and usuario:
            if livro.emprestar_livro():
                usuario.usuario_pegar_livro(livro)
                print("Livro emprestado com sucesso!")
            else:
                print("Livro não está disponível.")
        else:
            print("Livro ou usuário não encontrado.")

    def biblioteca_receber_livro(self, livro_id, user_id):
        livro = next((l for l in self.lista_livros if l.id == livro_id), None)
        usuario = next((u for u in self.lista_usuarios if u.id == user_id), None)
        if livro and usuario:
            if livro in usuario.livros_emprestados:
                livro.retornar_livro()
                usuario.usuario_devolver_livro(livro)
                print(f"Livro '{livro.titulo}' devolvido com sucesso!")
            else:
                print("Este usuário não emprestou este livro.")
        else:
            print("Livro ou usuário não encontrado.")
