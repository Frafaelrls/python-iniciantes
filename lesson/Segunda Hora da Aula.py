def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24}" \
               f" {conversion_unit} "
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 *60}" \
               f" {conversion_unit}"
    else:
        return "Unsupported units"


def validade_and_executed():
    try:  # Ira tentar executar o programa exceto quando der "ValueErro"
        user_input_number = int(days_and_units_dictionary["days"])  # acesso ao
        # número de dias no dicionário usa-se a palavra chave e não a posição
        # que está o do dado
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,
                                             days_and_units_dictionary["unit"])
            # Calcula usando os dados fornecidos
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You enter a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter the number of days and the conversion "
                       "unit (hours or minutes), separated by a colon. "
                       "Example: 15:hours\n")
    # Pede o usuário para inserir um valor ,o "\n" adiciona uma nova linha
    days_and_units = user_input.split(":")  # Transforma em uma lista
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0],
                                 "unit": days_and_units[1]}
    validade_and_executed()
