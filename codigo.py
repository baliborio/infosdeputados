import requests
import csv

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=56&ordem=ASC&ordenarPor=nome'
pagina = 1  # Começando da primeira página
deputados = []

while True:
    response = requests.get(url, params={'pagina': pagina})
    if response.status_code == 200:
        dados = response.json()
        if dados['dados']:  # Verificar se há dados na página
            for deputado in dados['dados']:
                nome = deputado['nome']
                ide = deputado['id']
                foto = deputado['urlFoto']
                partido = deputado['siglaPartido']
                UF = deputado['siglaUf']
                dades = [nome, ide, foto, partido, UF]
                deputados.append(dades)
                print(dades)
            pagina += 1
        else:
            break  # Se não houver mais dados, saia do loop
    else:
        print("Erro ao acessar a API da Câmara dos Deputados.")
        break

# Escrever os dados em um arquivo CSV
with open('deputados562.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['nome', 'id', 'foto', 'partido', 'UF'])  # Escrever o cabeçalho

    for linha in deputados:
        writer.writerow(linha)
