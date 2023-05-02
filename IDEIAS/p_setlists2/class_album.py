class Album:
    def __init__(self, nome, ano, artista, faixas):
        self.nome = nome
        self.ano = ano
        self.artista = artista
        self.faixas = faixas

    def exibirInformacoes(self):
        texto = f'''
        Nome: {self.nome}
        Ano: {self.ano}
        Artista: {self.artista}
        Faixas: {", ".join(self.faixas)}
        '''
        return texto
