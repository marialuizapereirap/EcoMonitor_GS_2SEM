# EcoMonitor — Central de Monitoramento Ambiental

**Disciplina:** Computational Thinking for Engineering  
**Curso:** Engenharia de Computação — FIAP  
**Turma:** 1ECA

## Integrantes

- Jenyfer Alarcon Cruz – RM: 573668
- Julia Oliveira de Souza – RM: 574118
- Maria Luiza Pereira – RM: 573151

## Sobre o projeto

O EcoMonitor é um sistema desenvolvido em Python para simular o monitoramento ambiental de uma praça pública urbana destinada à convivência da comunidade, ao lazer e à recreação.

Seu objetivo é receber e armazenar dados informados pelo usuário, analisar as condições ambientais simuladas, identificar valores que ultrapassem os critérios de referência, emitir alertas e gerar um relatório com estatísticas das leituras.

## Parâmetros monitorados

- **Temperatura do ar:** °C — faixa didática definida pelo grupo entre 18 °C e 30 °C.
- **Material particulado PM2,5:** µg/m³ — limite de 50 µg/m³ para média simulada de 24 horas.
- **Ruído:** dB — limite de 65 dB para o período diurno, considerando a classificação hipotética adotada para o cenário.

As fontes, justificativas e limitações dos critérios estão detalhadas no arquivo `pesquisa_limites_e_justificativas.pdf`.

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

py ecomonitor.py

O programa solicita a quantidade de leituras, recebe os três parâmetros, apresenta os resultados e gera um relatório TXT. Ao final, permite iniciar uma nova sequência de monitoramento.

## Demonstração em vídeo

O vídeo apresenta o funcionamento do EcoMonitor, incluindo a execução do programa, a análise das leituras, a emissão de alertas, os cálculos estatísticos e a geração do relatório.

**Assista à demonstração:** https://youtu.be/EcfUgifC9fE

## Arquivos do projeto

- `ecomonitor.py` — código-fonte do sistema.
- `README.md` — apresentação e instruções do projeto.
- `pesquisa_limites_e_justificativas.pdf` — pesquisa técnica, fontes e justificativas dos parâmetros.
- `relatorio_exemplo.txt` — exemplo de relatório gerado pelo programa.

## Observação

O EcoMonitor utiliza valores informados pelo usuário para fins de simulação acadêmica. Os resultados não representam medições ambientais reais, laudo técnico ou avaliação ambiental oficial.

A média aritmética do ruído é apenas uma estatística descritiva simplificada e não corresponde ao LAeq,T.