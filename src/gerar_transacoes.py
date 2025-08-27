import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_conta():
    return f"{random.randint(10000000, 99999999)}-{random.randint(0,9)}"

def gerar_chave():
    tipos = ["CPF", "CNPJ", "Email", "Telefone"]
    return random.choice(tipos)

def gerar_valor(fraude=False):
    if fraude:
        return round(random.uniform(5000, 20000), 2)  # valores altos
    else:
        return round(random.uniform(10, 2000), 2)     # valores normais

def gerar_data():
    hoje = datetime.now()
    dias_atras = random.randint(0, 30)
    horas = random.randint(0, 23)
    minutos = random.randint(0, 59)
    segundos = random.randint(0, 59)
    return hoje - timedelta(days=dias_atras, hours=horas, minutes=minutos, seconds=segundos)


transacoes = []

num_transacoes = 1000         # total de transações
percentual_fraude = 0.05      # 5% fraudulentas

for i in range(num_transacoes):
    fraude = random.random() < percentual_fraude
    transacao = {
        "id": i+1,
        "conta_origem": gerar_conta(),
        "conta_destino": gerar_conta(),
        "chave_pix": gerar_chave(),
        "valor": gerar_valor(fraude),
        "data_hora": gerar_data(),
        "fraude": fraude
    }
    transacoes.append(transacao)


df = pd.DataFrame(transacoes)
df.to_csv("data/raw/dados_pix.csv", index=False)
print("CSV criado com sucesso!")
