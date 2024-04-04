import json
import os

def buscar_e_editar_json(origem, destino, marcador):
    # Abrir e carregar o arquivo JSON de origem
    with open(origem, 'r') as file:
        data = json.load(file)
    
    # Inicializar um dicionário para armazenar as dependências por arquivo
    resultados = {}
    
    # Iterar sobre cada item no array do JSON de origem
    for item in data:
        diretorio = item["diretorio"]
        
        # Verificar se o diretório existe
        if os.path.exists(diretorio):
            # Ler o arquivo do diretório
            with open(diretorio, 'r') as arquivo:
                linhas = arquivo.readlines()
                # Verificar cada linha do arquivo em busca do marcador
                for linha in linhas:
                    if marcador in linha:
                        # Se o marcador for encontrado, adicionar ao resultado
                        nome_arquivo = os.path.basename(diretorio)
                        if nome_arquivo not in resultados:
                            resultados[nome_arquivo] = []
                        resultados[nome_arquivo].append(linha.strip())

    # Formatar os resultados como uma lista de dicionários
    resultado_final = [{"arquivo": arquivo, "dependencia": dependencias} for arquivo, dependencias in resultados.items()]

    # Criar o JSON de destino
    destino_json = os.path.join(destino, "list_dependency_by_tag.json")
    with open(destino_json, 'w') as file:
        json.dump(resultado_final, file, indent=4)

# Exemplo de uso:
buscar_e_editar_json("/home/mxs/workspace/list_project_file.json", "/home/mxs/workspace/", "import")