from colheita import registrar_colheita
from relatorios import gerar_relatorio
import banco

def menu():
    while True:
        print("\n=== Sistema de Monitoramento de Perdas na Colheita de Cana ===")
        print("1 - Registrar nova colheita")
        print("2 - Gerar relatório")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_colheita()
        elif opcao == "2":
            gerar_relatorio()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    banco.criar_tabela()
    menu()
