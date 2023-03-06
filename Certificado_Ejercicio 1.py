'''
Exercise 1 
Write a program that uses input to prompt a user for their name and then welcomes them. 
'''

def main():
  #Ingresar el nombre primera forma: 
  name = input('Enter your name:' )
  print("Hello ",name)

  #Ingresar el nombre segunda forma: 
  print("Ingresa tu nombre: ")
  nombre = input()
  print("Hola ", nombre)
  
if __name__ == "__main__": 
    main()