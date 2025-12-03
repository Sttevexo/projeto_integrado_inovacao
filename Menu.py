from bd_mock import (
    inserir_paciente,
    listar_pacientes,
    estatisticas_pacientes,
    buscar_pacientes_por_nome
)


def menu():

    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Cadastrar")
        print("2 - Estatística")
        print("3 - Buscar paciente")
        print("4 - Listar")
        print("5 - Sair")

        opcion = input("Escolha uma opção válida: ")

        if not opcion.isdigit():
            print("Entrada inválida: Escolha um número entre 1 e 5!")
            continue

        opcion = int(opcion)

        if opcion == 1:
            cadastro()
        elif opcion == 2:
            estatistica()
        elif opcion == 3:
            buscar()
        elif opcion == 4:
            listar()
        elif opcion == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Digite um número entre 1 e 5!")


def cadastro():
    while True:
        print("\n==== CADASTRO ====")
        nome = input("Digite o nome do paciente: ")

        idade = input("Digite a idade do paciente: ")
        if not idade.isdigit():
            print("Idade inválida! Digite apenas números.")
            continue
        idade = int(idade)

        telefone = input("Digite o telefone do paciente: ")

        inserir_paciente(nome, idade, telefone)
        print("Cadastro realizado com sucesso!")

        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
        if continuar != "s":
            break


def estatistica():
    total, media, mais_novo, mais_velho = estatisticas_pacientes()

    if total == 0:
        print("Nenhum paciente cadastrado.")
        return

    print("\n==== ESTATÍSTICAS ====")
    print(f"Total de pacientes: {total}")
    print(f"Média de idade: {media:.2f}")

    print(f"Mais novo: Nome={mais_novo[0]}, Idade={mais_novo[1]}, Telefone={mais_novo[2]}")
    print(f"Mais velho: Nome={mais_velho[0]}, Idade={mais_velho[1]}, Telefone={mais_velho[2]}")


def listar():
    pacientes = listar_pacientes()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print("\n==== LISTA DE PACIENTES ====")
    for nome, idade, telefone in pacientes:
        print(f"Nome: {nome} | Idade: {idade} | Telefone: {telefone}")


def buscar():
    nome = input("Digite o nome para busca: ")
    resultados = buscar_pacientes_por_nome(nome)

    if not resultados:
        print("Nenhum paciente encontrado.")
        return

    print("\n==== RESULTADOS DA BUSCA ====")
    for nome, idade, telefone in resultados:
        print(f"Nome: {nome} | Idade: {idade} | Telefone: {telefone}")


if __name__ == "__main__":
    menu()
