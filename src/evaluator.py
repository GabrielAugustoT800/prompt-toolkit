# Medir qualidade(acurácia), tokens, consistência, temperatura

import tiktoken
from collections import Counter

def contar_tokens(texto, modelo='gpt-4'):
    enc = tiktoken.encoding_for_model(modelo)
    return len(enc.encode(texto))

def medir_acuracia(resposta, esperado):
    resposta = resposta.strip().lower()

    if isinstance(esperado, dict):
        acertos = 0
        for valor in esperado.values():
            if str(valor).lower() in resposta:
                acertos += 1
        return round(acertos / len(esperado), 2)
    
    esperado = str(esperado).strip().lower()

    if resposta == esperado:
        return 1.0
    
    keywords = esperado.split()
    acertos = sum(1 for k in keywords if k in resposta)
    return round(acertos / len(keywords), 2)

def medir_consistencia(respostas):
    if not respostas:
        return 0.0
    
    respostas_norm = [r.strip().lower() for r in respostas]
    mais_comum = Counter(respostas_norm).most_common(1)[0][1]
    return round(mais_comum / len(respostas_norm), 2)

def testar_temperatura(prompt, temps, llm_client, system=''):
    resultados = []

    for temp in temps:
        respostas = []
        for _ in range(3):
            resultado = llm_client.chat(
                prompt = prompt,
                system = system,
                temp = temp
            )
            if 'erro' not in resultado:
                respostas.append(resultado['resposta'])
    
        consistencia = medir_consistencia(respostas)
        resultados.append({
            'temperatura': temp,
            'consistencia': consistencia,
            'respostas': respostas
        })
    return resultados

