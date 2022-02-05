calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units}" \
               f" {name_of_units} "


def validade_and_executed():
    try:  # Ira tentar executar o programa exceto quando der "ValueErro"
        user_input_number = int(num_of_days_element)  # Converte para int
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)  # Calcular
            # usando os dados fornecidos
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You enter a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separeted"
                       " and I will convert it in hours\n")  # Pede o usuário
    # para inserir um valor ,o "\n" adiciona uma nova linha
    for num_of_days_element in set(user_input.split(", ")):  # Para cada numero
        # fornecido pelo usuário valide e execute, "split(",")" transforma a
        # string em lista, considerando os números separados por virgula
        # "set" filtra os valores duplicados na lista
        validade_and_executed()
