import os
import json
from collections import defaultdict

def criar_json(origem, destino):
    # Criar um dicionário defaultdict que representará o JSON de destino
    json_destino = defaultdict(list)

    # Verificar se o diretório de destino existe, se não, criar
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Ler o arquivo JSON de origem
    with open(origem, 'r') as f:
        dados_origem = json.load(f)

    # Iterar sobre os itens do arquivo JSON de origem
    for item in dados_origem:
        diretorio_completo = item['diretorio']
        diretorio_pai = os.path.dirname(diretorio_completo)
        nome_arquivo = os.path.basename(diretorio_completo)

        # Adicionar a extensão do arquivo, se existir
        nome_arquivo_com_extensao = item.get('arquivo', '')
        if nome_arquivo_com_extensao:
            json_destino[diretorio_pai].append(nome_arquivo_com_extensao)

    # Converter o dicionário em uma lista de dicionários no formato desejado
    json_final = [{'diretorio': diretorio, 'arquivo': arquivos} for diretorio, arquivos in json_destino.items()]

    # Escrever o JSON de destino no arquivo de destino
    destino_json = os.path.join(destino, 'list_file_by_directory.json')
    with open(destino_json, 'w') as f:
        json.dump(json_final, f, indent=4)

# Exemplo de uso:
origem = "/home/mxs/workspace/list_project_file.json"
destino = "/home/mxs/workspace"
criar_json(origem, destino)
