my_set = {"January", "February", "March"}  # Usando "set" só podemos acessar
# elementos via loop, os elementos não possuem ordem definida como em "list"
for element in my_set:
    print(element)
my_set.add("April")  # Adiciona
print(my_set)
my_set.remove("January")  # Remove
print(my_set)
module_test = 10
