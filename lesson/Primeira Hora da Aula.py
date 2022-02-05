# inicio no dia 03/01/2022 as 11:30
#
#
# Quais são as variáveis e suas declarações
#
#
print("200 its a great number")  # Escrever em tela, deve-se usar as "" para que a escrita de textos seja permitida, em caso de números não é necessário
print("200 its a great number")  # Variáveis (variable) que contenham texto serão declaradas como string(str) significado em pt "Corda"
print(-2)  # Variáveis (variable) que contenham apenas números inteiros possitivos ou negativos serão declaradas como interg(int) - significado em pt "Interio"
print(22.99)  # Variáveis (variable) que contenham numeros positivos e negativos com um ou mais decimais devem ser declaradas como floating ponit number(float) - significado em pt "Número de ponto flutuante"
#
#
# Calculo aritiméticos
#
#
print(20*24*60)  # Cálculo aritimético básico para verificar quantos minutos temos em 20 dias
print("21 days are " + str(21*24*60) + " minutes")  # Forma de combinação de texto com números usando "String concatenation", nesse modo deve-se colocar um espaço no final e inicio das frases para que uma string fique com espaçamento entre elas
print(f"21 days are {21*24*60} minutes")  # Segunda forma de combinação de texto com números, usa-se o formatting(f) para informar que o que está em colchete faz parte de outra string
#
#
# Cálculo aritiméticos com uso de variáveis (variable)
#
#
# Em python existe algumas palavras que não podem ser usadas como nome de variáveis por serem predefinidas em alguma função ou syntax sendo elas:
#                           and, as, assert, break, lesson, continue, def, del, elif, else except, finally, false,
#                           for, from, global, if, import, in, is lambda, nonlocal, None, not, or, pass, raise,
#                           return, True, try with, while, yield
#
#
calculation_to_units = (24*60*60) # em python não é necessário declarar o tipo de variável que será usada, é feito o reconhecimento dinâmico de qual é necessária para o funcionámento, quando declarar uma variável usar nomes intuitivos e separar as palavras com underscorse(_)
name_of_units = "seconds"
print(f"20 days are {20*calculation_to_units} {name_of_units}")
#
#
# Criando Funções
#
#
# As funções tem como objetivos evitar a repetição da mesma lógica em um programa
calculation_to_units = (24*60*60)
name_of_units = "seconds"  # Após a declaração das variáveis deve-se colocar duas linhas em branco antes de declarar as funções


def days_to_units():  # Deve-se definir uma função usando define(def) e adicionar um nome descritivo
    print(f"20 days are {20*calculation_to_units} {name_of_units}") # A lógica de funcionamento deve permanecer "dentro" da função, usando tabulação
    print("All Good!")


days_to_units()  # Após declarado as funções devem ser chamadas para que possam funcionar corretamente
#
#
# Criando parâmetros e argumentos para as funções
#
#
calculation_to_hours = 24
name_of_unit = "Hours"


def days_to_units(num_of_days, custom_message):  # Definir usando variáveis entre parêntese para cada nova variável separar por virgula
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} "
          f"{name_of_unit}")
    print(custom_message)


days_to_units(35, "All good")  # Os parâmetros usados devem ficar entre os parêntese
#
#
# Scope(alcance) de variáveis em funções
#
#
calculation_to_hours = 24 # Variáveis globais, podem ser acessadas por todas as funções do código
name_of_unit = "hours"  # Global scope serão declaradas fora da função podendo estar em arquivos diferentes


def day_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours}"
          f"{name_of_unit}")  # Local scope estão disponíveis apenas dentro da função em que foram declaradas
    print(custom_message)


def scop_test(num_of_days, custom_message):  # Variáveis de input fornecidas quando chamamos a função
    int_var = "Internal Variable "  #variável declarada internamente, pode ser acessada apenas pela função "scop_test"
    print(calculation_to_hours)  # Variável global, pode ser acessada por todas as funções
    print(num_of_days)  # Variável passada por parâmetro
    print(custom_message)  # Variável passada por parâmetro
    print(int_var)


scop_test(40, "Scope test")
days_to_units(35, "Scope de variáveis em funções")
