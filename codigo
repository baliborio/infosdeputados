import requests
import csv

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=57&ordem=ASC&ordenarPor=nome'
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    deputados = []
    for deputado in dados['dados']:
        nome = deputado['nome']
        ide = deputado['id']
        foto = deputado['urlFoto']
        partido = deputado['siglaPartido']
        UF = deputado['siglaUf']
        dades = [nome, ide, foto, partido, UF]
        deputados.append(dades)
        print(dades)
    
    # Escrever os dados em um arquivo CSV
    with open('deputados57.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['nome', 'id', 'foto', 'partido', 'UF'])  # Escrever o cabeçalho

        for linha in deputados:
            writer.writerow(linha)
else:
    print("Erro ao acessar a API da Câmara dos Deputados.")
