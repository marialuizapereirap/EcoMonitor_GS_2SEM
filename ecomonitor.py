
# ============================================================
# EcoMonitor - Central de Monitoramento Ambiental
# Global Solution - Engenharia de Computacao
# ============================================================

# LIMITES E JUSTIFICATIVAS:
#
# TEMPERATURA:
# Foi definido pelo grupo o intervalo didatico de 18 a 30 °C
# para a simulacao de uma praca urbana hipotetica.
# O conforto termico depende tambem de fatores como umidade e vento.
# Fonte de consulta: INMET
# https://portal.inmet.gov.br/uploads/icones/Conforto_t%C3%A9rmico_inmet.pdf
#
# PM2.5:
# Foi adotado o limite de 50 µg/m³ para uma media de 24 horas,
# conforme o padrao PI-2 da Resolucao CONAMA 506/2024.
# Por isso, o valor informado no programa representa uma media
# simulada de 24 horas, e nao uma medicao instantanea.
# Fonte: CONAMA
# https://conama.mma.gov.br/?id=756&option=com_sisconama&view=atonormativo
#
# RUIDO:
# Foi adotado o limite de 65 dB para o periodo diurno,
# considerando uma area hipotetica de uso misto com predominancia
# de atividades culturais, de lazer e turismo.
# Referencia: ABNT NBR 10151:2019, Tabela 3.
# https://normadedesempenho.com.br/wp-content/uploads/2022/10/NBR-10151.pdf
#
# OBSERVACAO:
# A media aritmetica dos valores de ruido e uma estatistica
# descritiva simplificada. Ela nao representa o LAeq nem
# uma avaliacao de exposicao sonora.


# Limites utilizados na simulacao
TEMP_MIN = 18
TEMP_MAX = 30
PM25_MAX = 50
RUIDO_MAX = 65


# Funcao para calcular media, maior e menor valor
def calcular_estatisticas(valores):
    soma = 0

    for valor in valores:
        soma = soma + valor

    media = soma / len(valores)
    maior = max(valores)
    menor = min(valores)

    return media, maior, menor


# Funcao para analisar uma leitura e identificar alertas
def analisar_leitura(temperatura, pm25, ruido):
    alertas = []

    if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
        alertas.append("ALERTA: Temperatura fora do limite")

    if pm25 > PM25_MAX:
        alertas.append("ALERTA: PM2.5 acima do limite")

    if ruido > RUIDO_MAX:
        alertas.append("ALERTA: Ruido acima do limite")

    return alertas


# Funcao para receber valores numericos e validar entradas
def ler_numero(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < minimo:
                print("Valor abaixo do permitido. Tente novamente.")

            elif maximo is not None and valor > maximo:
                print("Valor acima do permitido. Tente novamente.")

            else:
                return valor

        except ValueError:
            print("Entrada invalida. Digite um numero.")


# Funcao para gerar o relatorio sem substituir arquivos anteriores
def gerar_relatorio(leituras, temperaturas, particulas, ruidos,
                    ocorrencias_temp, ocorrencias_pm25, ocorrencias_ruido,
                    leituras_criticas, percentual, classificacao):

    # Procura o proximo nome de arquivo disponivel
    numero_arquivo = 1

    while True:
        nome_arquivo = "relatorio_ecomonitor_" + str(numero_arquivo) + ".txt"

        try:
            with open(nome_arquivo, "r", encoding="utf-8"):
                numero_arquivo = numero_arquivo + 1

        except FileNotFoundError:
            break

    # Calcula as estatisticas dos tres parametros
    media_temp, maior_temp, menor_temp = calcular_estatisticas(temperaturas)
    media_pm25, maior_pm25, menor_pm25 = calcular_estatisticas(particulas)
    media_ruido, maior_ruido, menor_ruido = calcular_estatisticas(ruidos)

    # Escreve as informacoes no arquivo TXT
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write("========================================\n")
        arquivo.write("       RELATORIO ECOMONITOR\n")
        arquivo.write("========================================\n\n")

        arquivo.write("Ambiente monitorado: Praça urbana hipotética\n")
        arquivo.write("Quantidade de leituras: " + str(len(leituras)) + "\n\n")

        arquivo.write("LIMITES UTILIZADOS\n")
        arquivo.write("Temperatura: entre 18 e 30 °C\n")
        arquivo.write("PM2.5: ate 50 µg/m³ (media simulada de 24 horas)\n")
        arquivo.write("Ruido: ate 65 dB (periodo diurno)\n\n")

        arquivo.write("ESTATÍSTICAS - TEMPERATURA\n")
        arquivo.write(f"Média: {media_temp:.2f} °C\n")
        arquivo.write(f"Maior valor: {maior_temp:.2f} °C\n")
        arquivo.write(f"Menor valor: {menor_temp:.2f} °C\n\n")

        arquivo.write("ESTATÍSTICAS - PM2.5\n")
        arquivo.write(f"Média: {media_pm25:.2f} µg/m³\n")
        arquivo.write(f"Maior valor: {maior_pm25:.2f} µg/m³\n")
        arquivo.write(f"Menor valor: {menor_pm25:.2f} µg/m³\n\n")

        arquivo.write("ESTATÍSTICAS - RUIDO\n")
        arquivo.write(f"Média aritmética: {media_ruido:.2f} dB\n")
        arquivo.write(f"Maior valor: {maior_ruido:.2f} dB\n")
        arquivo.write(f"Menor valor: {menor_ruido:.2f} dB\n\n")

        arquivo.write("OCORRÊNCIAS POR PARAMETRO\n")
        arquivo.write("Temperatura fora do limite: " + str(ocorrencias_temp) + "\n")
        arquivo.write("PM2.5 acima do limite: " + str(ocorrencias_pm25) + "\n")
        arquivo.write("Ruido acima do limite: " + str(ocorrencias_ruido) + "\n\n")

        arquivo.write("RESULTADO GERAL\n")
        arquivo.write("Leituras com pelo menos uma ocorrencia: " + str(leituras_criticas) + "\n")
        arquivo.write(f"Percentual de leituras criticas: {percentual:.2f}%\n")
        arquivo.write(classificacao + "\n\n")

        arquivo.write("OBSERVACOES\n")
        arquivo.write("Este relatorio foi gerado a partir de uma simulacao academica.\n")
        arquivo.write("Os valores nao representam medicoes ambientais reais.\n")
        arquivo.write("O valor de PM2.5 representa uma media simulada de 24 horas.\n")
        arquivo.write("A media aritmetica do ruido e uma estatistica descritiva simplificada.\n")
        arquivo.write("Ela nao representa o LAeq nem uma avaliacao de exposicao sonora.\n")

    return nome_arquivo


# Funcao principal de monitoramento
def executar_monitoramento():

    # Listas para armazenar os valores de cada parametro
    temperaturas = []
    particulas = []
    ruidos = []

    # Lista de dicionarios para manter os dados de cada leitura associados
    leituras = []

    # Contadores de ocorrencias por parametro
    ocorrencias_temp = 0
    ocorrencias_pm25 = 0
    ocorrencias_ruido = 0

    # Contador de leituras criticas
    leituras_criticas = 0

    # Validacao da quantidade de leituras
    while True:
        try:
            quantidade = int(input("Quantas leituras deseja realizar? "))

            if quantidade <= 0:
                print("Digite uma quantidade maior que zero.")

            else:
                break

        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")

    # Repeticao para receber as leituras
    contador = 1

    while contador <= quantidade:

        print("\n--- Leitura", contador, "---")

        temperatura = ler_numero(
            "Digite a temperatura em °C: ", -100, 100
        )

        pm25 = ler_numero(
            "Digite a media simulada de PM2.5 em 24 horas (µg/m³): ", 0
        )

        ruido = ler_numero(
            "Digite o nivel de ruido em dB: ", 0
        )

        # Armazenamento dos valores nas listas
        temperaturas.append(temperatura)
        particulas.append(pm25)
        ruidos.append(ruido)

        # Armazenamento associado em um dicionario
        leitura = {
            "numero": contador,
            "temperatura": temperatura,
            "pm25": pm25,
            "ruido": ruido
        }

        leituras.append(leitura)

        # Analise dos parametros
        alertas = analisar_leitura(temperatura, pm25, ruido)

        print("\nResultado da leitura:")

        if len(alertas) > 0:

            for alerta in alertas:
                print(alerta)

            # Cada parametro e contado separadamente
            if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
                ocorrencias_temp = ocorrencias_temp + 1

            if pm25 > PM25_MAX:
                ocorrencias_pm25 = ocorrencias_pm25 + 1

            if ruido > RUIDO_MAX:
                ocorrencias_ruido = ocorrencias_ruido + 1

            # Uma leitura e contada apenas uma vez,
            # mesmo quando apresenta varios alertas
            leituras_criticas = leituras_criticas + 1

        else:
            print("Leitura dentro dos limites de referência estabelecidos")

        contador = contador + 1

    # Calculo das estatisticas
    media_temp, maior_temp, menor_temp = calcular_estatisticas(temperaturas)
    media_pm25, maior_pm25, menor_pm25 = calcular_estatisticas(particulas)
    media_ruido, maior_ruido, menor_ruido = calcular_estatisticas(ruidos)

    # Calculo do percentual de leituras criticas
    percentual = (leituras_criticas / quantidade) * 100

    # Classificacao geral conforme o criterio do professor
    if percentual > 30:
        classificacao = "Estado geral: condições ambientais de atenção, com frequência de ocorrências acima do critério estabelecido"

    else:
        classificacao = "Estado geral: frequência de ocorrências dentro do critério estabelecido para a simulação"

    # Apresentacao dos resultados no terminal
    print("\n========================================")
    print("       RESULTADO DO MONITORAMENTO")
    print("========================================")

    print("\nTEMPERATURA")
    print(f"Média: {media_temp:.2f}")
    print(f"Maior valor: {maior_temp:.2f}")
    print(f"Menor valor: {menor_temp:.2f}")

    print("\nPM2.5")
    print(f"Média: {media_pm25:.2f}")
    print(f"Maior valor: {maior_pm25:.2f}")
    print(f"Menor valor: {menor_pm25:.2f}")

    print("\nRUIDO")
    print(f"Média aritmética simplificada: {media_ruido:.2f}")
    print(f"Maior valor: {maior_ruido:.2f}")
    print(f"Menor valor: {menor_ruido:.2f}")

    print("\nOCORRÊNCIAS")
    print("Temperatura:", ocorrencias_temp)
    print("PM2.5:", ocorrencias_pm25)
    print("Ruido:", ocorrencias_ruido)
    print("Leituras criticas:", leituras_criticas)

    print(f"\nPercentual de leituras criticas: {percentual:.2f}%")
    print(classificacao)

    # Geracao do relatorio TXT
    nome_arquivo = gerar_relatorio(
        leituras,
        temperaturas,
        particulas,
        ruidos,
        ocorrencias_temp,
        ocorrencias_pm25,
        ocorrencias_ruido,
        leituras_criticas,
        percentual,
        classificacao
    )

    print("\nRelatório gerado:", nome_arquivo)


# Programa principal: permite iniciar novas sequencias
def iniciar_programa():

    while True:

        executar_monitoramento()

        while True:
            resposta = input(
                "\nDeseja iniciar uma nova sequencia? (S/N): "
            )

            if resposta == "S" or resposta == "s":
                break

            elif resposta == "N" or resposta == "n":
                print("\nMonitoramento encerrado.")
                return

            else:
                print("Resposta invalida. Digite S ou N.")


# Execucao do programa
iniciar_programa()
