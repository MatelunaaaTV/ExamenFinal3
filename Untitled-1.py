import random
PatenteV = 0
PatenteVBuscar = 0
patente = 0
letras = 0    
numeros = 0

try:

    while True:
        print("------------------------")
        print("Bienvenido a AutoSeguro")
        print("------------------------")
        print("Elija una opcion")
        print("1. Grabar")
        print("2. Buscar")
        print("3. Imprimir Certificados")
        print("4. Salir")
        opMenu = int(input(""))

        if opMenu == 1:
            print("Porfavor digite tipo de vehiculo")
            TipoV = input("")
            print("Porfavor digite la patente")
            PatenteV = input("")
            print("Porfavor digite la marca")
            MarcaV = input("")
            
            while True:
                print("Digite el precio del vehiculo")
                PrecioV = int(input(""))
                if PrecioV < 5000000:
                    print("No es valido el precio del mismo, porfavor vuelva a digitar")
                else:
                    break    
  
            print("Digite las multas que tiene el vehiculo, con su monto y fecha correspondiente")
            MultasV = input("")
            print("Digite nombre del dueño")
            NombreD = input("")
            
        
        if opMenu == 2:
            print("Digite patente de vehiculo")
            PatenteVBuscar = input("")
            if PatenteVBuscar == PatenteV:
                print("Buscando...")
                print("Tipo de vehiculo:",TipoV)
                print("Patente:",PatenteV)
                print("Marca:", MarcaV)
                print("Valor:", PrecioV)
                print("Multas:" ,MultasV)
                print("Nombre del dueño:", NombreD)
            else:
                print("Esta patente no figura en nuestra base de datos")
        
            
        if opMenu == 3:
            print("Imprimiendo certificado...")
            certificado = random.randint(1500, 3500)
            print("$",certificado, "es lo que debe pagar por su certificado")


        if opMenu == 4:
            print("Saliendo del programa")
            print("El autor de este sistema es: Benjamin Mateluna")
            print("Version: 1.0")
            break 

        if opMenu <= 0 or opMenu >= 5:
            print("Porfavor digite una opcion valida")


except ValueError:
    print("Por favor digite una opcion valida")