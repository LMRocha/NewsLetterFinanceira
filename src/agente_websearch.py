import os
from datetime import datetime
from time import localtime, strftime
from zoneinfo import ZoneInfo
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.ollama import Ollama
from dotenv import load_dotenv
from tool_envio_email import envia_email_tool
load_dotenv()

agent = Agent(
    model =Ollama(id="qwen3.5"),
    tools=[TavilyTools(), envia_email_tool],
    debug_mode=True
)

def carrega_arquivo_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# agent.print_response("Use as ferramentas para pesquisar as melhores oportunidades de investimentos para hoje, dia 27 de Abril de 2026")

if __name__ == "__main__":
    dt_brt = datetime.now(ZoneInfo("America/Sao_Paulo"))
    send_flag = False
    if dt_brt.hour == 10 and dt_brt.minute < 15 and send_flag == False:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        prompt_path = os.path.join(script_dir, os.pardir, "prompts", "prompt.md")
        prompt = carrega_arquivo_prompt(prompt_path)
        prompt_data = f'DATA: {dt_brt.strftime("%d/%m/%Y")}\n {prompt}'
        agent.run(prompt_data)
        senmd_flag = True
    else:
        print(f"Fora da janela 10:00–10:14 BRT. Horário atual em Brasília: {dt_brt.strftime('%H:%M')}.")