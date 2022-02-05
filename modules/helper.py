def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24}" \
               f" {conversion_unit} "
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 *60}" \
               f" {conversion_unit}"
    else:
        return "Unsupported units"


def validade_and_executed(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,
                                             days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You enter a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program")


user_input_message = "Hey user, enter number of days and conversion unit!\n"
