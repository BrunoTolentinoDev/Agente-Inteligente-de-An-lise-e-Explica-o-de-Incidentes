import os
import cohere
from dotenv import load_dotenv

# carrega as variáveis de ambiente do .env
load_dotenv()

class IncidentLLM:
    def __init__(self):
        # obtém a chave da api da cohere
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("COHERE_API_KEY não configurada no .env")

        # inicializa o cliente da cohere
        self.client = cohere.Client(api_key)

        # modelo padrão usado para análise
        self.model = "command-r-plus"

    def analyze_log(self, log_content: str) -> dict:
        # prompt enviado para o modelo com instruções claras
        prompt = f"""
Você é um engenheiro de software experiente em DevOps e SRE.

Analise o log abaixo e responda em português com:
1. Um resumo claro do problema
2. A possível causa técnica
3. Uma ação recomendada

LOG:
{log_content}
"""

        # chamada da api para análise do log
        response = self.client.chat(
            model=self.model,
            message=prompt
        )

        # resposta padronizada para consumo do agente
        return {
            "summary": response.text.strip(),
            "possible_cause": "Análise automatizada por IA",
            "recommended_action": "Seguir as orientações descritas no resumo"
        }
