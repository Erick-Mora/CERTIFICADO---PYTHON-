''' Exercise 2
Write a program to prompt the user for hours and rate per hour to compute gross pay.
'''
def main():
  #Manera 1:
  xh = input("Enter Hours: ")
  xr = input("Enter Rate: ")
  xp = float(xh) * float(xr)
  print("Howdy Pay: ",xp )
  print("\n")

  #Manera 2: 
  print("========= Estacionamiento ========= ")
  numero_horas = input("Ingrese el número de horas: ")
  precio_hora = input("Ingrese el precio por hora: ")
  conversion = float(numero_horas) * float(precio_hora)
  print("El total de su tarifa es:" , conversion ," pesos MX")
  print("\n")

if __name__ == "__main__": 
    main()