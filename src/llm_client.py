# Conexão com Ollama API
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

class LLm_Client:
    def __init__(self):
        self.host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        self.model = os.getenv('OLLAMA_MODEL', 'gpt-oss:120b')
    
    def chat(self, prompt, system='', temp=0.7, max_token=1000):
        url = f'{self.host}/api/chat'

        messages = []
        if system:
            messages.append({'role': 'system', 'content': system})
        messages.append({'role': 'user', 'content': prompt})

        payload = {
            'model': self.model,
            'messages': messages,
            'temperature': temp,
            'max_tokens': max_token,
            'stream': False
        }

        try:
            inicio = time.time()
            response = requests.post(url, json=payload, timeout=120)
            tempo_ms = int((time.time() - inicio) * 1000)

            data = response.json()

            return{
                'resposta': data['message']['content'],
                'tokens_prompt': data.get('promp_eval_count', 0),
                'tokens_resposta': data.get('eval_count', 0),
                'tempo_ms': tempo_ms
            }
        
        except requests.exceptions.Timeout:
            print('erro: Timeout - requisição do modelo demorou mais que 120s')
        except requests.exceptions.ConnectionError:
            print('erro: Ollama não está rodando - inicie com "ollama serve"')
        except Exception as e:
            print(f'Erro: {e}')
            return{'erro': str(e)}