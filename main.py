import json

def cadastrar_exercicio():
    novo_exercicio = {}
    novo_exercicio["nome"] = input("Nome do exercício: ")
    novo_exercicio["musculos"] = input("Músculos que o exercício trabalha (separados por vírgula): ").split(",")
    novo_exercicio["equipamentos"] = input("Equipamentos que o exercício usa (separados por vírgula): ").split(",")
    while True:
        try:
            novo_exercicio["serie"] = int(input("Quantas séries: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro para as séries.")
        
    while True:
        try:
            novo_exercicio["repeticoes"] = int(input("Repetições: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro para a repetições.")


    try:
        with open("app/exercicios.json", "r+") as arquivo:
            dados = json.load(arquivo)
            dados.append(novo_exercicio)
            arquivo.seek(0)
            json.dump(dados, arquivo, indent=4)
        print(f"{novo_exercicio['nome']} foi cadastrado com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo.")
        with open("app/exercicios.json", "w") as arquivo:
            json.dump([novo_exercicio], arquivo, indent=4)
    except json.decoder.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique o formato.")

def listar_exercicios():
    with open("app\exercicios.json", "r") as arquivo:
        dados = json.load(arquivo)
        for exercicio in dados:
            print(f"Nome: {exercicio['nome']}")

def buscar_exercicio(nome):
    try:
        with open("app/exercicios.json", "r") as arquivo:
            dados = json.load(arquivo)
            for exercicio in dados:
                if exercicio["nome"].lower() == nome.lower():
                    return print(
                        "Nome:", exercicio["nome"],
                        "\nMusculos:", ", ".join(exercicio["musculos"]),
                        "\nEquipamentos:", ", ".join(exercicio["equipamentos"]),
                        "\nSerie:", exercicio["serie"],
                        "\nRpeticoes:", exercicio["repeticoes"])
                    
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print(f"Erro ao buscar exercício: {e}")
    return None

def atualizar_exercicio(nome, campo, novo_valor):
    try:
        with open("app/exercicios.json", "r+") as arquivo:
            dados = json.load(arquivo)
            for exercicio in dados:
                if exercicio["nome"].lower() == nome.lower():
                    exercicio[campo.lower()] = novo_valor
                    break
            arquivo.seek(0)
            json.dump(dados, arquivo, indent=4)
            print(f"Exercício {nome} atualizado com sucesso.")
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print(f"Erro ao atualizar exercício: {e}")

def remover_exercicio(nome):
    try:
        with open("app/exercicios.json", "r", encoding='utf-8') as file:
            exercicios = json.load(file)

        indice = 0
        while indice < len(exercicios):
            exercicio = exercicios[indice]
            if nome == exercicio["nome"]:
                break
            else:
                indice += 1

        if indice < len(exercicios):
            exercicios.pop(indice)

            with open("app/exercicios.json", "w", encoding='utf-8') as file:
                json.dump(exercicios, file, indent=4)
            print(nome, "removido com sucesso")
            return True
        else:
            print(f"Exercício '{nome}' não encontrado.")
            return False

    except Exception as e:
        print(f"Erro ao excluir exercício: {e}")
        return False
def menu():
    print("      Menu Principal      " 
        "\n--------------------------"
        "\n| 1. Cadastra Exercício  |"
        "\n| 2. Buscar Exercício    |"
        "\n| 3. Listar Exercícios   |"
        "\n| 4. Atualizar Exercício |"
        "\n| 5. Excluir Exercício   |"
        "\n| x. Sair                |"
        "\n--------------------------")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        print("Você escolheu a opção 1!")
        cadastrar_exercicio()
    elif opcao == "2":
        print("Você escolheu a opção 2!")
        buscar_exercicio(input("Nome do exercício: "))
    elif opcao == "3":
        print("Você escolheu a opção 3!")
        listar_exercicios()
    elif opcao == "4":
        print("Você escolheu a opção 4!")
        atualizar_exercicio(input("Nome do exercício: "), input(''' 
Qual informação quer alterar entre: 
______________
|nome        |
|musculos    |
|equipamentos|
|serie       |
|repetições  |
|____________|

Digite qual campo quer alterar: '''),input("Digite a nova informação: ") )
    elif opcao == "5":
        print("Você escolheu a opção 5!")
        remover_exercicio(input("Nome do exercício: "))
    elif opcao == "x":
        print("Saindo...")
        return False
    else:
        print("Opção inválida!")

    return True

menu()
