'''
Exercise 3
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours. 
'''

def main(): 
    print("Exercise 3 - Estructuras condicionales")
    sh = input("Enter Hours: ")
    sr = input("Enter Rate: ")
    fh = float(sh)
    fr = float(sr)
  
    print(fh, fr)
    if fh > 40 : 
        print("Overtime")
        reg = fr * fh
        otp = (fh - 40.0) * (fr*0.5)
        print(reg, otp )
        xp = reg + otp
        print(xp)
    else: 
        print("Regular")
        xp = fh * fr
        print("Pay: ",xp)

if __name__ == "__main__":
    main()










'''
print("Ejercicio 3 - Estructuras condicionales")
    print("======Estacionamiento=======")
    numero_horas = input("Ingrese el número de horas: ")
    precio_hora = input("Ingrese el precio por hora: ")
    conversion_horas = float(numero_horas)
    conversion_precio = float(precio_hora)

    if conversion_horas > 40:
        multiplicacion = conversion_precio * conversion_horas
        multa = (conversion_horas - 40.0) * (conversion_precio * 0.5)
        costo_estacionamiento = multiplicacion + multa
    else:
        costo_estacionamiento = conversion_horas * conversion_precio
    print("El costo del estacionamiento es: ", costo_estacionamiento)
'''