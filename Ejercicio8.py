def main():
    print("Ejercicio 8")
    han = open('mbox-short.txt')

    for line in han: 
       line = line.rstrip()
       wds = line.split()
       # guardian in a compound statement
       if len(wds) < 3 or wds[0] != 'From':
          continue
       print(wds[2]) 
if __name__ == "__main__":
    main()