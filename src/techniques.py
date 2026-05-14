# 4 técnicas: ZS, FS, CoT, Role

from src.prompt_builder import montar_prompts, adicionar_exemplos, adicionar_cot

def zero_shot(tarefa, input):
    prompt = montar_prompts(
        instrucao = tarefa['instrucao'],
        input_dados = input,
        formato_output = tarefa['formato_output']
    )
    return prompt

def few_shot(tarefa, input, exemplo):
    prompt = montar_prompts(
        instrucao = tarefa['instrucao'],
        input_dados = input,
        formato_output = tarefa['formato_output']
    )
    return adicionar_exemplos(prompt, exemplo)

def chain_of_thought(tarefa, input, passos):
    prompt = montar_prompts(
        instrucao = tarefa['instrucao'],
        input_dados = input,
        formato_output = tarefa['formato_output']
    )
    return adicionar_cot(prompt, passos)

def role_prompting(tarefa, input, persona):
    prompt = montar_prompts(
        instrucao = tarefa['instrucao'],
        input_dados = input,
        formato_output = tarefa['formato_output'] 
    )
    return prompt, persona