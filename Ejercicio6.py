''' str = "X-DSPAM-Confidence: 0.8475"
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating number.
-------------------------------------------------------------------------------------------
Use buscar y cortar cadenas para extraer la parte de la cadena después del carácter de dos puntos y luego use la función flotante para convertir la cadena extraída en un número flotante.
'''
def main(): 
  print("Ejercicio 6")
  str = "X-DSPAM-Confidence: 0.8475"
  ipos = str.find(":")
  #print(ipos)
  piece = str[ipos+2:]
  #print(piece)
  #print(piece+42.0)
  value = float(piece)
  print(value)
  print(type(value))
  #print(value+42.0)
  
if __name__ == "__main__":
    main()
