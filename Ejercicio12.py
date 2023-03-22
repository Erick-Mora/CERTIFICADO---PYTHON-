import urllib.request, urllib.parse, urllib.error

def main():
  print("Ejercicio 12")
  fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
  
  counts = dict()
  for line in fhand:
    words = line.decode().split()
    for word in words: 
        counts[word] = counts.get(word,0) + 1
  print(counts)    
  
if __name__ == "__main__":
  main()

'''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand: 
  print(line.decode().strip())
'''