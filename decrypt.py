import os
from cryptography.fernet import Fernet

# Carregar a chave para descriptografia
def carregar_chave():
    return open("chave.key", "rb").read()

# Descriptografar um arquivo
def descriptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as arquivo_cripto:
        dados_criptografados = arquivo_cripto.read()

    dados_descriptografados = fernet.decrypt(dados_criptografados)

    nome_original = nome_arquivo.replace(".locked", "")

    with open(nome_original, "wb") as arquivo_original:
        arquivo_original.write(dados_descriptografados)

    os.remove(nome_arquivo)  # Remove o arquivo criptografado

chave = carregar_chave()

# Arquivo para descriptografar
arquivo_alvo = "teste.txt.locked"
descriptografar_arquivo(arquivo_alvo, chave)

print(f"Arquivo {arquivo_alvo} foi descriptografado!")
