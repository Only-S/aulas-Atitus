import time

class PostagemMensagem:
    def __init__(self, usuario, mensagem):
        self._usuario = usuario
        self._mensagem = mensagem
        self._hora_postagem = time.time()
        self._curtidas = 0
        self._comentarios = []

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        raise ValueError("Não é possível alterar o usuário")

    @property
    def mensagem(self):
        return self._mensagem

    @mensagem.setter
    def mensagem(self, valor):
        self._mensagem = valor
        self._hora_postagem = time.time() # Quando a postagem é alterada, a hora da postagem também deve mudar

    @property
    def hora_postagem(self):
        return self._hora_postagem

    @hora_postagem.setter
    def hora_postagem(self, valor):
        raise ValueError("Não é possível alterar a hora da postagem")

    @property
    def curtidas(self):
        return self._curtidas

    @curtidas.setter
    def curtidas(self, valor):
        raise ValueError("Não é possível alterar o número de curtidas")

    # Outros métodos da classe
    def curtir(self):
        self._curtidas += 1

    def descurtir(self):
        if self._curtidas > 0:
            self._curtidas -= 1

    def add_comentario(self, texto):
        self._comentarios.append(texto)

    def _tempo_to_str(self, tempo):
        atual = time.time() # Obtém a hora atual
        segundos = atual - tempo
        minutos = segundos // 60
        if minutos > 1:
            return f"{int(minutos)} minutos atrás"
        elif minutos == 1:
            return f"{int(minutos)} minuto atrás"
        else:
            return f"{int(segundos)} segundos atrás"

    def display(self):
        # Imprime a postagem
        print(self._usuario, "diz:")
        print(f'"{self._mensagem}"')
        print(self._tempo_to_str(self._hora_postagem))

        # Imprime a quantidade de likes
        if self._curtidas > 0:
            print(f"{self._curtidas} pessoas curtiram isso")
        else:
            print()

        # Imprime os comentários
        if len(self._comentarios) == 0:
            print("\tSem comentários.")
        else:
            print(f"\t{len(self._comentarios)} comentários")
            for comentario in self._comentarios:
                print(f"\t{comentario}\n")

class PostagemFoto:
    def __init__(self, usuario, imagem, legenda):
        self._usuario = usuario
        self._imagem = imagem
        self._legenda = legenda
        self._hora_postagem = time.time()
        self._curtidas = 0
        self._comentarios = []

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        raise ValueError("Não é possível alterar o usuário")

    @property
    def imagem(self):
        return self._imagem

    @imagem.setter
    def imagem(self, valor):
        self._imagem = valor
        self._hora_postagem = time.time() # Quando a postagem é alterada, a hora da postagem também deve mudar

    @property
    def legenda(self):
        return self._legenda

    @legenda.setter
    def legenda(self, valor):
        self._legenda = valor
        self._hora_postagem = time.time()  # Quando a postagem é alterada, a hora da postagem também deve mudar

    @property
    def hora_postagem(self):
        return self._hora_postagem

    @hora_postagem.setter
    def hora_postagem(self, valor):
        raise ValueError("Não é possível alterar a hora da postagem")

    @property
    def curtidas(self):
        return self._curtidas

    @curtidas.setter
    def curtidas(self, valor):
        raise ValueError("Não é possível alterar o número de curtidas")

    # Outros métodos da classe
    def curtir(self):
        self._curtidas += 1

    def descurtir(self):
        if self._curtidas > 0:
            self._curtidas -= 1

    def add_comentario(self, texto):
        self._comentarios.append(texto)

    def _tempo_to_str(self, tempo):
        atual = time.time() # Obtém a hora atual
        segundos = atual - tempo
        minutos = segundos // 60
        if minutos > 1:
            return f"{int(minutos)} minutos atrás"
        elif minutos == 1:
            return f"{int(minutos)} minuto atrás"
        else:
            return f"{int(segundos)} segundos atrás"

    def display(self):
        # Imprime a postagem
        print(self._usuario, "fotografou:")
        print(f'[{self._imagem}]')
        print(self._legenda)
        print(self._tempo_to_str(self._hora_postagem))

        # Imprime a quantidade de likes
        if self._curtidas > 0:
            print(f"{self._curtidas} pessoas curtiram isso")
        else:
            print()

        # Imprime os comentários
        if len(self._comentarios) == 0:
            print("\tSem comentários.")
        else:
            print(f"\t{len(self._comentarios)} comentários")
            for comentario in self._comentarios:
                print(f"\t{comentario}\n")


class PostagemMusica:
    def __init__(self, usuario, musica):
        self._usuario = usuario
        self._musica = musica
        self._hora_postagem = time.time()
        self._curtidas = 0
        self._comentarios = []

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        raise ValueError("Não é possível alterar o usuário")

    @property
    def musica(self):
        return self._mensagem

    @musica.setter
    def musica(self, valor):
        self._musica = valor
        self._hora_postagem = time.time() # Quando a postagem é alterada, a hora da postagem também deve mudar

    @property
    def hora_postagem(self):
        return self._hora_postagem

    @hora_postagem.setter
    def hora_postagem(self, valor):
        raise ValueError("Não é possível alterar a hora da postagem")

    @property
    def curtidas(self):
        return self._curtidas

    @curtidas.setter
    def curtidas(self, valor):
        raise ValueError("Não é possível alterar o número de curtidas")

    # Outros métodos da classe
    def curtir(self):
        self._curtidas += 1

    def descurtir(self):
        if self._curtidas > 0:
            self._curtidas -= 1

    def add_comentario(self, texto):
        self._comentarios.append(texto)

    def _tempo_to_str(self, tempo):
        atual = time.time() # Obtém a hora atual
        segundos = atual - tempo
        minutos = segundos // 60
        if minutos > 1:
            return f"{int(minutos)} minutos atrás"
        elif minutos == 1:
            return f"{int(minutos)} minuto atrás"
        else:
            return f"{int(segundos)} segundos atrás"

    def display(self):
        # Imprime a postagem
        print(self._usuario, "diz:")
        print(f'"{self._musica}"')
        print(self._tempo_to_str(self._hora_postagem))

        # Imprime a quantidade de likes
        if self._curtidas > 0:
            print(f"{self._curtidas} pessoas curtiram isso")
        else:
            print()

        # Imprime os comentários
        if len(self._comentarios) == 0:
            print("\tSem comentários.")
        else:
            print(f"\t{len(self._comentarios)} comentários")
            for comentario in self._comentarios:
                print(f"\t{comentario}\n")

class Feed:
    def __init__(self):
        self._mensagens = []
        self._fotos = []
        self._musicas = []

    def add_postagem_mensagem(self, mensagem: PostagemMensagem):
        self._mensagens.append(mensagem)

    def add_postagem_foto(self, foto: PostagemFoto):
        self._fotos.append(foto)

    def add_postagem_musica(self, musica: PostagemMusica):
        self._musicas.append(musica)

    def mostra_postagens(self):
        for mensagem in self._mensagens:
            mensagem.display()
            print("-" * 40)

        for foto in self._fotos:
            foto.display()
            print("-" * 40)

        for musica in self._musicas:
            musica.display()
            print("-" * 40)

# Programa Principal

# Crie duas postagens de mensagem e uma postagem de imagem
postmen1 = PostagemMensagem("Renazinho123","Eu quero que vá todo mundo pro krl")
postim1 = PostagemFoto("Kl0v1nnnn", "D:\Meus Documentos\Documentos\aulas-atitus\AulasBackendPython\2º Semestre\Aula5\IMG_0450", "Divaaaaaaaaaaaaa")
postmen2 = PostagemMensagem("CinthiaAmber", "Só por uma resenhazinha")
postmus1 = PostagemMusica("Krebert24", "Campos de Morangos")

# Crie um feed e adicione as postagens
facemeta = Feed()
postmen1.curtir()
postmen1.curtir()
postmen1.curtir()
postmen1.descurtir()
postmen1.add_comentario("Vc é um vagabundo mano!")
postim1.curtir()
postim1.add_comentario("Ela é uma Deusa brow *-*")
postim1.curtir()
postim1.descurtir()
postim1.add_comentario("Derretia fácil")
postmen2.curtir()
facemeta.add_postagem_foto(postim1)
facemeta.add_postagem_mensagem(postmen1)
facemeta.add_postagem_mensagem(postmen2)
postmus1.descurtir()
postmus1.curtir()
postmus1.curtir()
postmus1.curtir()
postmus1.curtir()
facemeta.add_postagem_musica(postmus1)

# Chame o método que mostra as mensagens
facemeta.mostra_postagens()
