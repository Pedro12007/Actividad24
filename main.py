def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return n * factorial(n-1)

def suma(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return n + suma(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def letra_en_palabra(letra, palabra):
    if letra in palabra:
        pass

def potencia(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * potencia(base, exp-1)

while True:
    print('Menú:')
    print('1. Calcular el factorial')
    print('2. Suma de los primeros números N naturales')
    print('3. Calcular n-ésimo número de Fibonacci')
    print('4. Contar cuántas veces aparece una letra en una palabra')
    print('5. Invertir una cadena de texto')
    print('6. Calcular la potencia de un número')
    print('7. Salir')

    option = input('Ingrese la opción que desea: ')

    match option:
        case '1':
            try:
                n = int(input('Ingrese el número para factorial: '))
                print(f'Factorial: {factorial(n)}')
            except ValueError:
                print('Dato ingresado inválido.')
            except Exception as e:
                print('Un error ha ocurrido.', e)

        case '2':
            try:
                n = int(input('Ingrese el número para suma: '))
                print(f'Suma: {suma(n)}')
            except ValueError:
                print('Dato ingresado inválido.')
            except Exception as e:
                print('Un error ha ocurrido.', e)

        case '3':
            try:
                n = int(input('Ingrese el n-ésimo de Fibonacci: '))
                print(f'n-ésimo de Fibonacci #{n}: {fibonacci(n)}')
            except ValueError:
                print('Dato ingresado inválido.')
            except Exception as e:
                print('Un error ha ocurrido.', e)

        case '4':
            pass

        case '5':
            pass

        case '6':
            try:
                base = int(input('Ingrese la base: '))
                exponente = int(input('Ingrese el exponente del número: '))
                print(f'Potencia base: {base}; exponente: {exponente} = {potencia(base, exponente)}')
            except ValueError:
                print('Dato ingresado inválido.')
            except Exception as e:
                print('Un error ha ocurrido.', e)

        case '7':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida.\n')