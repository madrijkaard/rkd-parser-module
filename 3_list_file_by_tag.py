import os
import json

def criar_json(origem, destino):
    # Lê o arquivo JSON de origem
    with open(origem, 'r') as file:
        dados = json.load(file)

    # Dicionário para armazenar as dependências e os arquivos correspondentes
    dependencias_arquivos = {}

    # Itera sobre os dados do arquivo JSON de origem
    for item in dados:
        arquivo = item["arquivo"]
        dependencias = item["dependencia"]

        # Itera sobre as dependências do arquivo atual
        for dependencia in dependencias:
            # Se a dependência ainda não estiver no dicionário, adiciona com uma lista vazia
            if dependencia not in dependencias_arquivos:
                dependencias_arquivos[dependencia] = []

            # Adiciona o arquivo atual à lista de arquivos da dependência
            dependencias_arquivos[dependencia].append(arquivo)

    # Lista para armazenar os dados no formato desejado
    json_formatado = []

    # Converte o dicionário em uma lista de dicionários no formato desejado
    for dependencia, arquivos in dependencias_arquivos.items():
        json_formatado.append({"dependencia": dependencia, "arquivo": arquivos})

    # Verifica se o diretório de destino existe, se não, cria-o
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Caminho completo para o arquivo de destino
    arquivo_destino = os.path.join(destino, 'list_file_by_tag.json')

    # Escreve os dados formatados no arquivo de destino
    with open(arquivo_destino, 'w') as file:
        # Escreve os dados no arquivo de destino
        json.dump(json_formatado, file, indent=4)

# Exemplo de uso
origem = "/home/mxs/workspace/list_dependency_by_tag.json"
destino = "/home/mxs/workspace/"
criar_json(origem, destino)
