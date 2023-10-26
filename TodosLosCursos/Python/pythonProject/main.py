# This is a sample Python script.
from Persona import Persona, Empleado
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Ciclor
def interar(num):
    for i in range(10):
        if i % 3 == 0:
            print(i)
    print('Ingresando el nuevo for')
    for i in range(3,10,2):
        print(i)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(fibonacci(11))
    interar(30)

    persona = Persona(nombre="vinicio",edad=15)
    empleado = Empleado(nombre="Leonardo",edad=22,salario=25.5)
    print(persona.nombre)
    print(empleado.nombre)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
