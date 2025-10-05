import json
from banco import listar_dados

def gerar_relatorio():
    dados = listar_dados()
    if not dados:
        print("Nenhum dado encontrado.")
        return

    # Exportar para JSON
    with open("relatorio.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    # Exportar para TXT
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        for linha in dados:
            f.write(str(linha) + "\n")

    print("Relatórios gerados: relatorio.json e relatorio.txt")
