# Ejercicio 2

máximo = 0
mínimo = 0
primer_número = True
while True:
    try:
        input_str = input("Ingrese un número: ")
        if (input_str == "fin"):
            break
        else:
            if (primer_número):
                máximo = int(input_str)
                mínimo = int(input_str)
                primer_número = False
            else:
                if(int(input_str) > máximo): máximo = int(input_str)
                if (int(input_str) < mínimo): mínimo = int(input_str)
    except:
        print("Valor no es válido")
        continue
    print("Máximo:", máximo)
    print("Mínimo:", mínimo)
