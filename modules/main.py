from helper import validade_and_executed, user_input_message  # import specific
# function, for many functions use import + module (import helper)

# import helper as h used to rename a mudules
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")  # Transforming in list
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0],
                                 "unit": days_and_units[1]}
    validade_and_executed(days_and_units_dictionary)
