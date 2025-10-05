from utils import validar_float
from banco import inserir_dados
from datetime import datetime

def calcular_perdas(prod_estimada, prod_real, valor_tonelada):
    perda_percentual = ((prod_estimada - prod_real) / prod_estimada) * 100
    prejuizo = (perda_percentual / 100) * valor_tonelada * prod_real
    return round(perda_percentual, 2), round(prejuizo, 2)

def registrar_colheita():
    tipo = input("Tipo de colheita (manual/mecanica): ").strip().lower()
    if tipo not in ["manual", "mecanica"]:
        print("Tipo inválido!")
        return

    prod_estimada = validar_float("Produtividade estimada (t/ha): ")
    prod_real = validar_float("Produtividade real (t/ha): ")
    valor_tonelada = validar_float("Valor por tonelada (R$): ")

    perda_percentual, prejuizo = calcular_perdas(prod_estimada, prod_real, valor_tonelada)

    dados = {
        "tipo": tipo,
        "prod_estimada": prod_estimada,
        "prod_real": prod_real,
        "valor_tonelada": valor_tonelada,
        "perda_percentual": perda_percentual,
        "prejuizo": prejuizo,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    inserir_dados(dados)
    print(f"Colheita registrada! Perda: {perda_percentual}% | Prejuízo: R$ {prejuizo}")
