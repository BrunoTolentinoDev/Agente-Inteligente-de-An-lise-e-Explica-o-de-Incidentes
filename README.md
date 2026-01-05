# Agente Inteligente de Analise e Explicação de Incidentes

Este projeto consiste em um assistente inteligente desenvolvido em Python para interpretar logs e mensagens de erro de sistemas. O foco e oferecer uma traducao tecnica de incidentes para ajudar desenvolvedores a entenderem falhas rapidamente atraves de IA.

A ideia principal e automatizar a leitura de arquivos de log, identificando a criticidade do erro e utilizando um modelo de linguagem para resumir o problema e sugerir acoes corretivas.

---

## Estrutura do Projeto

Organizacao dos arquivos no repositorio:

incident-agent/
├── logs/

│   └── erro.log

├── .env

├── incident_agent.py

├── llm_client.py

└── requirements.txt


---

## Criterios de Analise

O agente realiza tres etapas de validacao:

1. Deteccao de Severidade
   Faz uma varredura automatica no log em busca de palavras-chave para classificar o erro como:
   - Critica (Fatal, Panic, Exception)
   - Alta (Error, Failed)
   - Media (Warning)
   - Baixa (Outros casos)

2. Resumo com Inteligencia Artificial
   O conteudo do log e enviado para o modelo da Cohere, que gera uma explicacao clara do erro em portugues.

3. Plano de Acao
   O agente retorna recomendacoes tecnicas sobre o que deve ser verificado para resolver o incidente.

---

## Como Executar

1. Configure sua chave da API no arquivo .env:
   COHERE_API_KEY=seu_token_aqui

2. Instale as dependencias necessarias:
   pip install -r requirements.txt

3. Execute o agente passando o caminho do arquivo de log:
   python incident_agent.py logs/erro.log

---

## Formato da Resposta

O sistema retorna um JSON estruturado:

- severity: Nivel de urgencia do erro.
- summary: Resumo detalhado gerado pela IA.
- possible_cause: Origem provavel do problema.
- recommended_action: Passo a passo para correcao.

---

## Atualizacao do Projeto no GitHub

Para salvar novas alteracoes via CMD, utilize os comandos:

git add README.md
git commit -m "Adicionando estrutura de pastas no README"
git push origin main
