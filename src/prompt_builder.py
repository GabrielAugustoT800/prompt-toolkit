# Montar prompts por anatomia

def montar_prompts(instrucao, contexto='', input_dados='', formato_output=''):
    if not instrucao:
        raise ValueError('Instrução não pode ser vazia!')
    if not input_dados:
        raise ValueError('Input de dados não pode ser vazio!')
    
    partes = []
    partes.append(f'Instrução: {instrucao}')

    if contexto:
        partes.append(f'Contexto: {contexto}')
    
    partes.append(f'Input: {input_dados}')
    if formato_output:
        partes.append(f'Formato de Output: {formato_output}')

    return '\n\n'.join(partes)

def adicionar_exemplos(prompt,exemplos):
    if not exemplos:
        return prompt
    
    linhas = ['\n\nExemplos:']
    for ex in exemplos:
        linhas.append(f'Input: "{ex['input']}" -> Output: "{ex['output']}"')

    return prompt + '\n'.join(linhas)

def adicionar_cot(prompt, passos):
    if not passos:
        return prompt
    linhas = ['\n\nAnálise passo a passo']
    for i, passo in enumerate(passos, 1):
        linhas.append(f'{i}. {passo}')

    return prompt + '\n'.join(linhas)