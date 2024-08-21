import datetime # serve para expecificar a data e hora.

    # Função para adicionar um aluno no sistema da academia.
def adicionar_aluno(membros, nome, idade, plano):
    aluno = {  # membros é uma lista que armazena todos os aluno cadastrados.
        'nome': nome,              
        'idade': idade,
        'plano': plano,
        'data_inscricao': datetime.date.today() # para obter a data atual do cadastramento do aluno.
    }
    membros.append(aluno) #para adicionar o aluno ao sistema da academia
    print(f"Aluno {nome} adicionado com sucesso.")

    # Função para listar todos os alunos já cadastrados no sistema da academia.
def listar_alunos(membros):
    if not membros:#vai verificar se essa condição é falsa
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in membros: #verificar se estar em sequencia
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Plano: {aluno['plano']}, Data de Inscrição: {aluno['data_inscricao']}")

    # Função para calcular o valor total arrecadado.
def calcular_total_arrecadado(membros, valor_plano):
    total = len(membros) * valor_plano
    return total

    # Função para atualizar o plano de um aluno da academia.
def atualizar_plano(membros, nome, novo_plano):
    for aluno in membros:#vereficar se estar em sequencia
        if aluno['nome'] == nome:
            aluno['plano'] = novo_plano
            print(f"Plano do aluno {nome} atualizado para {novo_plano}.")
            return #usado dentro de funções para devolver um valor ao código que chamou a função.
    print(f"Aluno {nome} não encontrado.")

    # Função para exibir o menu de opções.
def menu():
    print("Sistema de cadastramento")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Calcular Total Arrecadado")
    print("4. Atualizar Plano do aluno")
    print("5. Sair")

    # Função principal para gerenciar a interação com o usuário.
def main():
    membros = [] # para armazenar os dados dos alunos cadastrados no sistema da academia.
    valor_plano = 200  # Valor fixo do plano.

    while True: # serve para criar um loop infinito com o usuario.
        menu()
        escolha = input("Escolha uma opção: ")
    # O 'elif' usado serve para que todas as verificações seja verdadeira ou falsas, vai depender do que tiver no 'if'.
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

        else: # É utilizado para executar caso o 'if' seja falso.
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    main()    
    # O código dentro desse bloco sera executado apenas quando o script é executado diretamente, e não quando é importado como um módulo em outro script. Isso é útil para organizar o código e garantir que certas partes sejam executadas apenas no contexto de execução direta.

