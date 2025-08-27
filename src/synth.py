import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

n = 500
usuarios = ["user_" + str(i) for i in range(1, 21)]
tipos = ["transferencia", "compra", "saque"]

dados = []
for i in range(n):
    tx = {
        "id": i + 1,
        "usuario": random.choice(usuarios),
        "valor": round(random.uniform(1, 5000), 2),
        "tipo": random.choice(tipos),
        "data": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
        "suspeita": random.choice([0, 1]) if random.random() < 0.15 else 0
    }
    dados.append(tx)

df = pd.DataFrame(dados)
df.to_csv("../data/pix_sintetico.csv", index=False)
print("✅ Dados falsos salvos em data/pix_sintetico.csv")
