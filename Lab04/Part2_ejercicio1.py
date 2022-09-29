# Contador de números.

Total = 0 
Contador = 0
while True:
    try:
        input_str = input ( "Ingrese un número: ")
        if (input_str == "fin" ):
            break
        else:
            Total = Total + int(input_str)
            Contador = Contador + 1
            Promedio = Total / Contador 
    except:
        print( "Valor no válido" )
        continue
    print("Total:", Total)
    print("Contador", Contador)
    print("Promedio", Promedio)
