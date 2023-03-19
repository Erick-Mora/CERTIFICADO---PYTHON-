''' Write a program to read through a file and print the contents of the file (line by line) all in uppercase. Executing the program will look as follows.
'''
def main():
    print("Ejercicio 7")
    fh = open('mbox-short.txt')

    for lx in fh: 
       ly = lx.rstrip()
       print(ly.upper())
if __name__ == "__main__":
    main()