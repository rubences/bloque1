import math

def calcular_seno(x):
    return math.sin(x)

# Ejemplo de uso
x = 1.0  # Puedes cambiar este valor por cualquier otro
resultado = calcular_seno(x)
print(f"El seno de {x} es {resultado}")


def verificar_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "No eres mayor de edad."

def main():
    edad = int(input("Introduce tu edad: "))
    resultado = verificar_edad(edad)
    print(resultado)

if __name__ == "__main__":
    main()