import sys
import json
import os
from llm_client import IncidentLLM

# lê o conteúdo do arquivo de log
def read_log(file_path: str) -> str:
    if not os.path.exists(file_path):
        return ""

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()

# define a severidade com base em palavras-chave
def detect_severity(log_content: str) -> str:
    content = log_content.lower()

    if any(word in content for word in ["fatal", "panic", "exception"]):
        return "critica"
    if any(word in content for word in ["error", "failed"]):
        return "alta"
    if "warning" in content:
        return "media"

    return "baixa"

# coordena a leitura do log e a análise pela ia
def analyze_incident(file_path: str) -> dict:
    log_content = read_log(file_path)

    if not log_content.strip():
        return {"error": "Arquivo vazio ou não encontrado"}

    # calcula a severidade do incidente
    severity = detect_severity(log_content)

    # inicializa o cliente de ia
    llm = IncidentLLM()
    ai_result = llm.analyze_log(log_content)

    # resposta final padronizada
    return {
        "severity": severity,
        "summary": ai_result["summary"],
        "possible_cause": ai_result["possible_cause"],
        "recommended_action": ai_result["recommended_action"]
    }

# ponto de entrada do script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python incident_agent.py logs/erro.log")
        sys.exit(1)

    result = analyze_incident(sys.argv[1])
    print(json.dumps(result, indent=4, ensure_ascii=False))
