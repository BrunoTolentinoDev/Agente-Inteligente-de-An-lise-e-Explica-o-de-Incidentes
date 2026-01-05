# Agente Inteligente de Analise e Explição de Incidentes

Este projeto consiste em um assistente inteligente desenvolvido em Python para interpretar logs e mensagens de erro de sistemas. O foco não é o bloqueio de processos, mas sim a tradução técnica de incidentes para ajudar desenvolvedores a resolverem problemas mais rápido.

A ideia principal é oferecer uma camada de inteligência que resume falhas complexas, identifica a gravidade do problema e sugere caminhos para a correção, simulando a análise inicial feita por um engenheiro de suporte ou DevOps.

---

## Estrutura do Projeto

Organização das pastas e arquivos:

- logs/
  - erro_servidor.log
  - falha_banco_dados.log
  - conexao_api.log
- agente_analise.py -> código principal com a lógica da IA
- config.py -> configurações de conexão e regras básicas

---

## Funcionalidades do Agente

O agente realiza quatro tarefas essenciais:

1. Analise de Gravidade
   Identifica se o erro é apenas um aviso (warning) ou algo que derrubou o sistema.

2. Resumo de Incidentes
   Transforma logs extensos e confusos em uma explicação simples do que realmente aconteceu.

3. Diagnóstico de Causas
   Aponta o provável motivo do erro, como falta de memória, erro de sintaxe ou queda de conexão.

4. Sugestão de Correção
   Indica quais comandos ou ajustes devem ser feitos para solucionar o incidente.

---

## Como Usar o Analisador

Para rodar o agente e analisar um arquivo de log, utilize os comandos abaixo:

1. Analisar um erro de servidor:
   python agente_analise.py logs/erro_servidor.log

2. Analisar uma falha de banco de dados:
   python agente_analise.py logs/falha_banco_dados.log

---

## Diferencial do Projeto

Ao contrário de scripts comuns que buscam apenas palavras-chave, este projeto utiliza IA para entender o contexto do erro. Isso reduz o tempo de diagnóstico e evita que a equipe perca tempo tentando decifrar mensagens de erro genéricas.
