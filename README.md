# Newsletter Automática

Projeto de automação que utiliza um agente de IA para gerar conteúdo e enviar uma newsletter por email.

## Estrutura do projeto

- `src/agente_websearch.py` - script principal que carrega o prompt e executa o agente de pesquisa.
- `src/tool_envio_email.py` - ferramenta de envio de email usando `smtplib` e variáveis de ambiente para credenciais.
- `prompts/prompt.md` - prompt de instrução usado pelo agente para gerar o conteúdo financeiro.
- `requirements.txt` - dependências do projeto.

## Como funciona

1. O agente é criado em `src/agente_websearch.py` usando:
   - `agno.Agent`
   - modelo `Ollama(id="qwen3.5")`
   - `TavilyTools()` e a ferramenta de envio de email `envia_email_tool`
2. O prompt é carregado de `prompts/prompt.md` e enviado ao agente.
3. O agente realiza a pesquisa e, se configurado, envia o conteúdo por email.
4. O script principal verifica a janela de execução entre `10:00` e `10:14` BRT antes de rodar.

## Requisitos

- Python 3.11+ (recomendado)
- `requirements.txt` com as bibliotecas necessárias

Instalação:

```bash
pip install -r requirements.txt
```

> Observação: o módulo `email` faz parte da biblioteca padrão do Python.

## Configuração do ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
EMAIL_ADDRESS=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
DESTINATARIOS=destino1@example.com,destino2@example.com
```

## Execução

Rode o script principal:

```bash
python src/agente_websearch.py
```

O script somente tenta enviar a newsletter se o horário local em Brasília estiver entre `10:00` e `10:14`.

## Personalização

- Edite `prompts/prompt.md` para ajustar o briefing dado ao agente.
- Ajuste o modelo ou as ferramentas em `src/agente_websearch.py` conforme necessário.

## Avisos

- Verifique as configurações de SMTP do Gmail e habilite senha de app se estiver usando autenticação de dois fatores.
- Use as credenciais com cuidado e evite compartilhar o `.env` publicamente.
