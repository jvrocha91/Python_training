class Livro():
    def __init__(self, titulo, autor, id_livro):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
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

    def add_livro(self,titulo, autor, id_livro):
        if id_livro in self.lista_livros:
            print("ID ja usado, tente novamente")
        else:
            novo_livro = Livro(titulo, autor, id_livro)
            self.lista_livros.append(novo_livro)
            print(f"Livro '{titulo}' adicionado com sucesso!")

    def remover_livro(self,livro):
        if livro in self.lista_livros:
            self.lista_livros.remove(livro)

    def registrar_user(self,nome, user_id):
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

def main():
    # Criar instância da biblioteca
    biblioteca = Biblioteca()

    # Adicionar livros à biblioteca
    biblioteca.add_livro("1984", "George Orwell", 1)
    biblioteca.add_livro("Orgulho e Preconceito", "Jane Austen", 2)

    # Registrar usuários
    biblioteca.registrar_user("Alice", 100)
    biblioteca.registrar_user("Bob", 101)

    # Emprestar livros
    biblioteca.biblioteca_emprestar_livro(1, 100)
    biblioteca.biblioteca_emprestar_livro(2, 101)

    # Listar livros emprestados por um usuário
    usuario_alice = next(u for u in biblioteca.lista_usuarios if u.id_usuario == 100)
    print("Livros emprestados por Alice:", usuario_alice.listar_livros())

    # Devolver livros
    biblioteca.biblioteca_receber_livro(1, 100)
    print("Livros disponíveis após devolução por Alice:", usuario_alice.listar_livros())


if __name__ == "__main__":
    main()
