# Tarefas do domínio
tarefas ={
    'classificacao_urgencia': {
        'nome': 'classificacao_urgencia',
        'tipo': 'classificacao',
        'instrucao': 'Classifique a urgência do caso médico como EMERGÊNCIA, URGENTE, POUCO URGENTE, NÃO URGENTE',
        'formato_output': 'Responda APENAS com a classificação',
        'exemplos_fewshot': [
            {'input': 'Paciente com dor no peito e falta de ar', 'output': 'EMERGÊNCIA'},
            {'input': 'Criança com febre de 38,5 há 2 dias', 'output':'URGENTE'},
            {'input': 'Paciente com dor de cabeça leve ocasional', 'output': 'POUCO URGENTE'},
        ],
        'passos_cot': [
            'Identifique os sintomas descritos',
            'Avalie o risco de vida imediato',
            'Considere a gravidade e tempo de evolução',
            'Classifique conforme protocolo de triagem',
        ],
        'persona': 'medico_triagem'
    },

    "extracao_dados_paciente": {
        "nome": "extracao_dados_paciente",
        "tipo": "extracao",
        "instrucao": "Extraia os dados estruturados do relato médico em formato JSON",
        "formato_output": "Responda APENAS com o JSON: {sintoma, duracao, intensidade}",
        "exemplos_fewshot": [
            {"input": "Dor de cabeça forte há 3 dias", "output": '{"sintoma": "dor de cabeça", "duracao": "3 dias", "intensidade": "forte"}'},
            {"input": "Febre baixa desde ontem", "output": '{"sintoma": "febre", "duracao": "1 dia", "intensidade": "baixa"}'},
        ],
        "passos_cot": [
            "Identifique o sintoma principal",
            "Identifique a duração mencionada",
            "Identifique a intensidade descrita",
            "Monte o JSON com os dados extraídos",
        ],
        "persona": "enfermeiro_triagem"
    },

    
    'sumarizacao_prontuario': {
        'nome': 'sumarizacao_prontuario',
        'tipo': 'sumarizacao',
        'instrucao': 'Resuma o prontuário médico em bullet points objetivos para o médico plantonista',
        'formato_output': 'Responda com bullet points, 5 linhas',
        'exemplos_fewshot': [
            {'input': 'Paciente João, 45 anos, hipertenso, chegou com dor torácica há 2h, PA 180/110, FC 98', 'output': '• Homem, 45 anos, hipertenso\n• Dor torácica há 2h\n•PA elevada - 180/110\n• FC: 98bpm\n• Avaliar síndrome coronariana'}
        ],
        'passos_cot': [
            'Identifique dados do paciente (idade, sexo, histórico)',
            'Identifique queixa principal e tempo de evolução',
            'Identifique sinais relevantes',
            'Liste os pontos mais críticos para o plantonista'
        ],
        'persona': 'medico_triagem'
    }
}