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

def gerar_excel(resultados):
    df = pd.DataFrame(resultados)
    os.makedirs("output", exist_ok=True)

    # Média de acurácia por tarefa e técnica
    pivot_acuracia = df.groupby(["tarefa", "tecnica"])["acuracia"].mean().unstack()
    pivot_acuracia = pivot_acuracia.applymap(lambda x: f"{x:.0%}")

    # Média de tokens por tarefa e técnica
    pivot_tokens = df.groupby(["tarefa", "tecnica"])["tokens_total"].mean().unstack()
    pivot_tokens = pivot_tokens.applymap(lambda x: f"{x:.0f}")

    # Média de tempo por tarefa e técnica
    pivot_tempo = df.groupby(["tarefa", "tecnica"])["tempo_ms"].mean().unstack()
    pivot_tempo = pivot_tempo.applymap(lambda x: f"{x:.0f}ms")

    with pd.ExcelWriter("output/resultados.xlsx", engine="openpyxl") as writer:
        pivot_acuracia.to_excel(writer, sheet_name="Acuracia")
        pivot_tokens.to_excel(writer, sheet_name="Tokens")
        pivot_tempo.to_excel(writer, sheet_name="Tempo")
        df.to_excel(writer, sheet_name="Dados Completos", index=False)

    print("✅ Excel salvo em output/resultados.xlsx!")