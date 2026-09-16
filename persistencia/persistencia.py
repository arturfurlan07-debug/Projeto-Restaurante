import pickle


def salvar_dados(objeto, caminho_arquivo):
    """Salva qualquer objeto Python de forma não volátil usando pickle."""
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(objeto, arquivo)


def carregar_dados(caminho_arquivo):
    """Carrega um objeto previamente salvo com `salvar_dados`."""
    with open(caminho_arquivo, "rb") as arquivo:
        return pickle.load(arquivo)
