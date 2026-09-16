import pickle


def salvar_dados(objeto, caminho_arquivo):
    """Salva um objeto Python em arquivo, de forma não volátil (pickle)."""
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(objeto, arquivo)


def carregar_dados(caminho_arquivo):
    """Carrega um objeto salvo anteriormente com salvar_dados()."""
    with open(caminho_arquivo, "rb") as arquivo:
        return pickle.load(arquivo)
