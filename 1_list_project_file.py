import os
import json

def analisar_arquivos(origem, destino, extensao):
    # Verifica se o diretório de origem existe
    if not os.path.isdir(origem):
        print(f'O diretório de origem "{origem}" não existe.')
        return
    
    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Lista para armazenar os dados dos arquivos
    arquivos_encontrados = []

    # Lista todos os arquivos e diretórios dentro do diretório de origem e subdiretórios
    for pasta_atual, _, arquivos in os.walk(origem):
        for arquivo in arquivos:
            # Verifica se o arquivo possui a extensão especificada
            if arquivo.endswith(extensao):
                # Cria o caminho completo do arquivo encontrado
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                # Adiciona os dados do arquivo à lista de arquivos encontrados
                arquivos_encontrados.append({
                    "arquivo": arquivo,
                    "diretorio": caminho_arquivo
                })

    # Cria o arquivo JSON no diretório de destino
    with open(os.path.join(destino, 'list_project_file.json'), 'w') as arquivo_json:
        # Escreve os dados da lista de arquivos encontrados no arquivo JSON
        json.dump(arquivos_encontrados, arquivo_json, indent=4)

# Exemplo de uso do método
origem = '/home/mxs/workspace/java-tron'
destino = '/home/mxs/workspace'
extensao = '.java'

analisar_arquivos(origem, destino, extensao)