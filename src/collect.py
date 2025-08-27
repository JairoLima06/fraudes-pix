import requests
import pandas as pd

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("../data/pix_data.csv", index=False)
    print("✅ Dados salvos em data/pix_data.csv")
else:
    print("❌ Erro ao coletar dados")
