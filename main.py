# Ponto de entrada
import json
from src.llm_client import LLMClient
from src.techniques import zero_shot, few_shot, chain_of_thought, role_prompting
from src.tasks import tarefas
from src.evaluator import contar_tokens, medir_acuracia, testar_temperatura
from src.report import gerar_tabela, grafico_acuracia, grafico_custo, grafico_temperatura, recomendar

def carregar_json(path):
    with open(path, 'r', encoding= 'utf-8') as f:
        return json.load(f)
    
def main():
    print('='*40, 'Iniciando Prompt-TOOLKIT - Domínio: Saúde','='*40,'\n')

    llm = LLMClient()
    inputs = carregar_json('data/inputs.json')
    examples = carregar_json('data/examples.json')
    system_prompts = carregar_json('prompts/system_prompts.json')
    resultados = []

    for nome_tarefa, tarefa in tarefas.items():
        print(f'\nTarefa: {nome_tarefa}')
        casos = inputs[nome_tarefa]
        exemplos = examples[nome_tarefa]
        persona = system_prompts[tarefa['persona']]['instrucao']

        for caso in casos:
            input_texto = caso['input']
            esperado = caso['esperado']

            tecnicas = {
                'zero_shot': zero_shot(tarefa, input_texto),
                'few_shot': few_shot(tarefa, input_texto, exemplos),
                'chain_of_thought': chain_of_thought(tarefa, input_texto, tarefa['passos_cot']),
                'role_prompting': role_prompting(tarefa, input_texto, persona)
            }
            for nome_tecnica, prompt in tecnicas.items():
                system = ''
                if nome_tecnica == 'role_prompting':
                    prompt, system = prompt
                
                tokens_prompt = contar_tokens(prompt)
                
                print(f'  {nome_tecnica}...', end='')
                resultado = llm.chat(prompt=prompt, system=system)

                if 'erro' in resultado:
                    print(f'\n{resultado['erro']}')
                    continue

                acuracia = medir_acuracia(resultado['resposta'], esperado)
                tokens_total = resultado['tokens_prompt'] + resultado['tokens_resposta']

                print(f'Acurácia: {acuracia:.0%}')

                resultados.append({
                    'tarefa': nome_tarefa,
                    'tecnica': nome_tecnica,
                    'input': input_texto,
                    'resposta': resultado['resposta'],
                    'esperado': str(esperado),
                    'acuracia': acuracia,
                    'tokens_total': tokens_total,
                    'tokens_prompt_tiktoken': tokens_prompt,
                    'tempo_ms': resultado['tempo_ms']
                })
    
    print('\n Gerando Relatório...')
    gerar_tabela(resultados)
    grafico_acuracia(resultados)
    grafico_custo(resultados)
    
    print('\nTestando a temperatura do Melhor Prompt...')
    melhor_prompt = zero_shot(list(tarefas.values())[0], list(inputs.values())[0][0]['input'])
    resultados_temp = testar_temperatura(melhor_prompt, [0.1, 0.5, 1.0], llm)
    grafico_temperatura(resultados_temp)

    recomendar(resultados)
    print('\nToolKit Finalizado! Resultado em output/')

if __name__ == '__main__':
    main()
