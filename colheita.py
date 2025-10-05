from utils import validar_float
from banco import inserir_dados
from datetime import datetime

def calcular_perdas(prod_estimada, prod_real, valor_tonelada):
    """Calcula a perda com base na produtividade estimada vs. real."""
    perda_toneladas = prod_estimada - prod_real
    perda_percentual = (perda_toneladas / prod_estimada) * 100
    prejuizo = perda_toneladas * valor_tonelada
    return round(perda_percentual, 2), round(prejuizo, 2)

def registrar_colheita():
    """Registra uma nova colheita, verificando se houve perda ou ganho."""
    tipo = input("Tipo de colheita (manual/mecanica): ").strip().lower()
    if tipo not in ["manual", "mecanica"]:
        print("Tipo inválido!")
        return

    prod_estimada = validar_float("Produtividade estimada (t/ha): ")
    prod_real = validar_float("Produtividade real (t/ha): ")

    # --- INÍCIO DA NOVA LÓGICA: VERIFICAÇÃO DE GANHO ---
    if prod_real > prod_estimada:
        ganho_percentual = ((prod_real - prod_estimada) / prod_estimada) * 100
        print("\n--- Análise de Resultado ---")
        print("Ótima notícia! O resultado foi um GANHO, não uma perda.")
        print(f"A produtividade real superou a estimada em {round(ganho_percentual, 2)}%.")
        print("Com as métricas atuais, você não precisa se preocupar com perdas.")
        print("Este registro não será salvo como uma perda.")
        return # Encerra a função e volta ao menu principal
    # --- FIM DA NOVA LÓGICA ---

    valor_tonelada = validar_float("Valor por tonelada (R$): ")

    # Se o código chegou até aqui, significa que prod_real <= prod_estimada, ou seja, é uma perda.
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
    print(f"\nColheita registrada! Perda: {perda_percentual}% | Prejuízo: R$ {prejuizo}")