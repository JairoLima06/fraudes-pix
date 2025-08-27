import requests
import pandas as pd
import os

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"
params = {
    "formato": "json",
    "dataInicial": "27/08/2015",
    "dataFinal": "27/08/2025"
}

def coletar_dados():
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if not data:
            print("⚠️ Nenhum dado retornado")
            return

        df = pd.DataFrame(data)
        os.makedirs("data/raw", exist_ok=True)
        output_path = "data/raw/dados_bcb.csv"
        df.to_csv(output_path, index=False, encoding="utf-8")

        print(f"✅ Dados salvos em {output_path} | {len(df)} registros")

    except Exception as e:
        print("❌ Erro ao coletar dados:", str(e))


if __name__ == "__main__":
    coletar_dados()
