'''
Exercise 4 
Rewrite your pay program using try and except so that your program handles non - numeric input gracefully by printing a message and exiting the program. 
'''
def main():
    #Opción 1 
    print("Ejercicio Con try y exept \n")
    sh = input("Enter hours: ")
    sr = input("Enter rate: ")
    try:
        fh = float(sh)
        fr = float(sr)
    except:
        print("Error, please enter numeric input")
        quit()
    if(fh>40):
        #print("Overtime")
        reg = fh * fr
        otp = (fh-40) * (fr * .5)
        xp = reg + otp
    else:
        #print("Regular")
        xp = fh * fr
    print("Pay:", xp)

    print("\n")
    #Opción 2
    print("===== Estacionamiento =====")
    numero_horas = input("Ingrese el número de horas: ")
    precio_hora = input("Ingrese el precio por hora: ")

    try:
        horas = float(numero_horas)
        precio = float(precio_hora)
    except:
        print("Error, lo que ingresó es un caracter.... porfavor ingrese un número  ")
        quit()

    if horas > 40:
        multiplicacion = precio * horas
        comision = (horas - 40.0) * (precio * 0.5)
        costo_estacionamiento = multiplicacion + comision
    else:
        costo_estacionamiento = horas * precio
    print("El costo del estacionamiento es: ", costo_estacionamiento)

if __name__ == "__main__":
    main()

