from Requisito_1 import *

if __name__ == "__main__":
    while True:
        print("=------------------------=")
        print("=- Menu do App -=")
        print("=------------------------=")
        
        print("\n")
        
        usuario = str(input("=- Digite o seu usuario: "))
        senha = int(input("=- Digite a sua senha: "))
        break
    
    conta = {usuario : senha}
    app = App(conta)
    
    opcao = -1
    
    while True:
        print("=------------------------=")
        print("=- Menu Principal-=")
        print("=------------------------=")
        print("\n")
        print("=- 1 - Mostrar Vagas Disponiveis -=")
        print("=- 2 - Pegar Vaga -=")
        print("\n")
        print("=------------------------=")
        
        opcao = input("=- Digite a sua opcao: ")
        
        
        match (opcao):
            case 1:
                app.show_vagasDisponiveis()
                break
    
        
        