import json
from banco import listar_dados
from datetime import datetime

def gerar_relatorio():
    """
    Gera relatórios formatados (TXT e JSON) a partir dos dados de colheita do banco.
    O relatório TXT é humanamente legível e inclui um sumário.
    O relatório JSON é estruturado com chaves descritivas.
    """
    dados_brutos = listar_dados()
    if not dados_brutos:
        print("Nenhum dado de colheita encontrado para gerar relatórios.")
        return

    # --- Preparação dos dados e cálculos para o sumário ---
    registros_formatados_json = []
    prejuizo_total = 0
    soma_percentual_perda = 0
    contagem_manual = 0
    contagem_mecanica = 0
    
    # Mapeia os índices da tupla do banco para nomes de colunas claros
    colunas = [
        "ID", "Tipo de Colheita", "Prod. Estimada (t/ha)", "Prod. Real (t/ha)", 
        "Valor por Tonelada (R$)", "Perda Percentual (%)", "Prejuízo (R$)", "Data e Hora"
    ]

    for linha in dados_brutos:
        # Cria um dicionário para cada registro, facilitando a manipulação
        registro_dict = {
            colunas[0]: linha[0],
            colunas[1]: str(linha[1]).capitalize(),
            colunas[2]: f"{linha[2]:.2f}",
            colunas[3]: f"{linha[3]:.2f}",
            colunas[4]: f"R$ {linha[4]:,.2f}",
            colunas[5]: f"{linha[5]:.2f}%",
            colunas[6]: f"R$ {linha[6]:,.2f}",
            colunas[7]: linha[7]
        }
        registros_formatados_json.append(registro_dict)

        # Cálculos para o sumário do relatório TXT
        prejuizo_total += linha[6]
        soma_percentual_perda += linha[5]
        if linha[1].lower() == 'manual':
            contagem_manual += 1
        elif linha[1].lower() == 'mecanica':
            contagem_mecanica += 1
    
    perda_media = soma_percentual_perda / len(dados_brutos) if dados_brutos else 0

    # --- Geração do Relatório em JSON ---
    with open("relatorio.json", "w", encoding="utf-8") as f:
        # O JSON agora é uma lista de objetos com chaves descritivas
        json.dump(registros_formatados_json, f, ensure_ascii=False, indent=4)

    # --- Geração do Relatório em TXT ---
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("=========================================================\n")
        f.write("      RELATÓRIO DE MONITORAMENTO DE PERDAS NA COLHEITA\n")
        f.write("=========================================================\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

        f.write("------------------ REGISTROS INDIVIDUAIS ------------------\n\n")
        for reg in registros_formatados_json:
            f.write(f"{reg['Data e Hora']}\n")
            f.write(f"  - ID do Registro.........: {reg['ID']}\n")
            f.write(f"  - Tipo de Colheita.......: {reg['Tipo de Colheita']}\n")
            f.write(f"  - Prod. Estimada.........: {reg['Prod. Estimada (t/ha)']} t/ha\n")
            f.write(f"  - Prod. Real.............: {reg['Prod. Real (t/ha)']} t/ha\n")
            f.write(f"  - Valor por Tonelada.....: {reg['Valor por Tonelada (R$)']}\n")
            f.write(f"  - Percentual de Perda....: {reg['Perda Percentual (%)']}\n")
            f.write(f"  - PREJUÍZO FINANCEIRO....: {reg['Prejuízo (R$)']}\n")
            f.write("---------------------------------------------------------\n\n")

        f.write("===================== SUMÁRIO EXECUTIVO =====================\n\n")
        f.write(f"Total de Registros de Perda...: {len(dados_brutos)}\n")
        f.write(f"  - Colheitas Manuais........: {contagem_manual}\n")
        f.write(f"  - Colheitas Mecânicas......: {contagem_mecanica}\n\n")
        f.write(f"Média de Perda Percentual.....: {perda_media:.2f}%\n")
        f.write(f"PREJUÍZO TOTAL ACUMULADO......: R$ {prejuizo_total:,.2f}\n\n")
        f.write("=========================================================\n")

    print("\nRelatórios aprimorados foram gerados com sucesso: relatorio.json e relatorio.txt")