# prompt-toolkit
CP02 - Prompt Toolkit FIAP

# Prompt Toolkit — Domínio: Saúde

Toolkit Python que aplica automaticamente 4 técnicas de prompting
(Zero-Shot, Few-Shot, Chain-of-Thought e Role Prompting) a tarefas
do domínio de saúde, compara resultados e recomenda a melhor abordagem.

## 👥 Grupo
- PulseGuard — 
-- Integrantes --
- Gabriel Augusto da Silva -
- Leonardo Kenji Kubo Barboza -
- Lucas Gabriel Alvarenga e Meireles -
- Lucas Koiti Uyeno de Souza -
- Lucas Morio Ikeda -

## 🛠 Stack
- Python 3.10+
- Ollama API (local/gratuito)
- tiktoken, pandas, matplotlib

## 📋 Pré-requisitos
- Python 3.10+
- Ollama instalado e rodando
- Modelo gpt-oss:120b baixado

## ⚙️ Instalação

1. Clone o repositório:
git clone https://github.com/GabrielAugustoT800/prompt-toolkit.git
cd prompt-toolkit

2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

3. Instale as dependências:
pip install -r requirements.txt

4. Configure o ambiente:
cp .env.example .env

## 🚀 Executando

Certifique-se que o Ollama está rodando:
ollama serve

Em outro terminal, execute o toolkit:
python main.py

## 📁 Estrutura
prompt-toolkit/
├── main.py
├── src/
│   ├── llm_client.py
│   ├── prompt_builder.py
│   ├── techniques.py
│   ├── tasks.py
│   ├── evaluator.py
│   └── report.py
├── data/
│   ├── inputs.json
│   └── examples.json
├── prompts/
│   ├── system_prompts.json
│   └── templates.json
└── output/
    ├── resultados.csv
    └── graficos/

## 📊 Tarefas Implementadas
- Classificação de urgência médica
- Extração de dados do paciente
- Sumarização de prontuário

## 🏆 Técnicas Implementadas
- Zero-Shot
- Few-Shot
- Chain-of-Thought
- Role Prompting