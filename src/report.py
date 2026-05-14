# Gerar tabelas e gráficos comparativos

import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)
    os.makedirs('output', exist_ok = True)
    df.to_csv('output/resultados.csv', index = False)
    print('\nTabela Comparativa de Resultados:')
    print(df.to_string(index = False))
    return df

def grafico_acuracia(resultados):
    df = pd.DataFrame(resultados)
    os.makedirs('output/graficos', exist_ok = True)

    grupo = df.groupby(['tarefa', 'tecnica'])['acuracia'].mean().unstack()
    grupo.plot(kind='bar', figsize = (10, 5))
    plt.title('Acurácia Por Tarefa e Técnica')
    plt.xlabel('Tarefa')
    plt.ylabel('Técnica')
    plt.xticks(rotation = 45)
    plt.legend(title = 'Técnica')
    plt.tight_layout()
    plt.savefig('output/graficos/acuracia.png')
    plt.close()
    print('Gráfico de acurácia salvo com sucesso!')

def grafico_custo(resultados):
    df = pd.DataFrame(resultados)
    os.makedirs('output/graficos', exist_ok = True)

    grupo = df.groupby(['tarefa', 'tecnica'])['tokens_total'].mean().unstack()
    grupo.plot(kind='bar', figsize=(10, 5))
    plt.title('Custo em Tokens por Tarefa e Técnica')
    plt.xlabel('Tarefa')
    plt.ylabel('Tokens Médios')
    plt.xticks(rotation = 45)
    plt.legend(title = 'Técnica')
    plt.tight_layout()
    plt.savefig("output/graficos/custo_tokens.png")
    plt.close()
    print('Gráfico de custo slavo com sucesso!')

def grafico_temperatura(resultados_temp):
    os.makedirs('output/graficos', exist_ok=True)

    temps = [r['temperatura'] for r in resultados_temp]
    consistencias = [r['consistencia'] for r in resultados_temp]

    plt.figure(figsize=(10, 5))
    plt.plot(temps, consistencias, marker='o', color='steelblue')
    plt.title('Consistência por Temperatura')
    plt.xlabel('Temperatura')
    plt.ylabel('Consistência')
    plt.tight_layout()
    plt.savefig('output/graficos/temperatura.png')
    plt.close()
    print('Gráfico de temperatura salvo com sucesso!')

def recomendar(resultados):
    df = pd.DataFrame(resultados)
    print('Recomendação por Tarefa:')

    for tarefa in df['tarefa'].unique():
        df_tarefa = df[df['tarefa'] == tarefa]
        melhor = df_tarefa.groupby('tecnica')['acuracia'].mean().idxmax()
        acuracia = df_tarefa.groupby('tecnica')["acuracia"].mean().max()
        print(f' {tarefa}: Melhor técnica -> {melhor} (Acurácia média: {acuracia:.0%})')