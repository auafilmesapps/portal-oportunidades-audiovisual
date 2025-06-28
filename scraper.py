import os
from datetime import datetime
from supabase import create_client, Client

# Simulação de coleta - substitua por Playwright ou requests reais
def coletar_oportunidades():
    return [
        {
            "titulo": "Edital Cultural 2025",
            "descricao": "Apoio a produções audiovisuais regionais.",
            "url": "https://exemplo.gov.br/edital-cultural",
            "data_publicacao": "2025-06-15",
            "prazo_final": "2025-07-15",
            "palavras_chave": ["cultura", "audiovisual"],
            "categoria_id": None,
            "fonte_id": None,
        }
    ]

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def salvar_oportunidades(oportunidades):
    for oportunidade in oportunidades:
        supabase.table("oportunidades").insert(oportunidade).execute()

if __name__ == "__main__":
    dados = coletar_oportunidades()
    salvar_oportunidades(dados)
