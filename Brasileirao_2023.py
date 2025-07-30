import json

# Caminho do arquivo JSON
caminho = r'/content/brasileirao-2023.json'

# Tenta carregar os dados do arquivo
try:
    with open(caminho, 'r', encoding='utf8') as arq:
        dados = json.load(arq)
except:
    print("Não foi possível carregar o arquivo. Verifique o caminho e a existência do arquivo.")
    exit()

# Coletando técnicos de todos os jogos
todos_tecnicos = []
for jogos in dados.values():
    for match in jogos:
        # verifica se a estrutura está correta
        tecnico_home = match.get('coach', {}).get('home')
        tecnico_away = match.get('coach', {}).get('away')
        if tecnico_home:
            todos_tecnicos.append(tecnico_home)
        if tecnico_away:
            todos_tecnicos.append(tecnico_away)

# Contando quantas vezes cada técnico apareceu
contagem_tecnicos = {}
for tecnico in todos_tecnicos:
    if tecnico in contagem_tecnicos:
        contagem_tecnicos[tecnico] += 1
    else:
        contagem_tecnicos[tecnico] = 1

print(contagem_tecnicos)

# Técnicos por time
tecnicos_por_time = {}

for jogos in dados.values():
    for match in jogos:
        for lado in ['home', 'away']:
            time = match.get('clubs', {}).get(lado)
            tecnico = match.get('coach', {}).get(lado)

            if time and tecnico:
                if time not in tecnicos_por_time:
                    tecnicos_por_time[time] = {}
                if tecnico in tecnicos_por_time[time]:
                    tecnicos_por_time[time][tecnico] += 1
                else:
                    tecnicos_por_time[time][tecnico] = 1

print(tecnicos_por_time)

# Encontrando técnico mais longevo por time
lista_times = []
for time, tecnicos in tecnicos_por_time.items():
    tecnico_longevo = max(tecnicos.items(), key=lambda x: x[1])
    lista_times.append((time, tecnico_longevo[0], tecnico_longevo[1]))

print(lista_times)

# Ordenando times pela longevidade do técnico
lista_times.sort(key=lambda x: x[2], reverse=True)

# Exibindo resultados
print("Técnicos por time e o mais longevo:")
texto=''
for time, tecnico, jogos in lista_times:
    print(f"\n Time: {time}")
    print(" Técnicos que atuaram:")
    for t, q in sorted(tecnicos_por_time[time].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {t}: {q} {'jogo' if q == 1 else 'jogos'}")
    print(f" Técnico mais longevo: {tecnico} ({jogos} jogos)")

# Ordenando técnicos por número de jogos
ordenados = sorted(contagem_tecnicos.items(), key=lambda x: x[1], reverse=True)
print()
print('TREINADORES MAIS LONGEVOS (geral):\n')
for tecnico, qtd in ordenados:
    print(f"{tecnico}: {qtd} jogos")