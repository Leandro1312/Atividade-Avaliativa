import datetime 
   
def adicionar_aluno(membros, nome, idade, plano):
    aluno = {  
        'nome': nome,              
        'idade': idade,
        'plano': plano,
        'data_inscricao': datetime.date.today() 
    }
    membros.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso.")

    
def listar_alunos(membros):
    if not membros:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in membros: 
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Plano: {aluno['plano']}, Data de Inscrição: {aluno['data_inscricao']}")

    
def calcular_total_arrecadado(membros, valor_plano):
    total = len(membros) * valor_plano
    return total

def atualizar_plano(membros, nome, novo_plano):
    for aluno in membros:
        if aluno['nome'] == nome:
            aluno['plano'] = novo_plano
            print(f"Plano do aluno {nome} atualizado para {novo_plano}.")
            return 
    print(f"Aluno {nome} não encontrado.")

    
def menu():
    print("Sistema de cadastramento")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Calcular Total Arrecadado")
    print("4. Atualizar Plano do aluno")
    print("5. Sair")

    
def main():
    membros = [] 
    valor_plano = 100
    

    while True: 
        menu()
        escolha = input("Escolha uma opção: ")
    
        if escolha == '1':
            nome = input("Nome do aluno: ")
            idade = int(input("Idade do aluno: "))
            plano = input("Plano do aluno: ")
            adicionar_aluno(membros, nome, idade, plano)

        elif escolha == '2':
            listar_alunos(membros)

        elif escolha == '3':
            total = calcular_total_arrecadado(membros, valor_plano)
            print(f"Total arrecadado: R${total}")

        elif escolha == '4':
            nome = input("Nome do aluno: ")
            novo_plano = input("Novo plano: ")
            atualizar_plano(membros, nome, novo_plano)

        elif escolha == '5':
            print("Saindo do sistema...")
            break

        else: 
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    main()  