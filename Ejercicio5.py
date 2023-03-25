""" Rewrite your pay computation with time-and-a-half for overtime and create a fuction called computepay which two parameters (hours and rate). 
"""

def main():
    print("Ejercicio 5 - Función y parámetros ")

    def computepay(hours,rate): 
        print("In computepay", hours, rate)
        if hours > 40 :
            reg = rate * hours
            otp = (hours - 40.0) * (rate*0.5)
            pay = reg + otp
        else:
            pay = hours * rate
        return pay

    sh = input("Enter Hours: ")
    sr = input("Enter Rate: ")
    fh = float(sh)
    fr = float(sr)

    xp = computepay(fh,fr)
    print("Pay ",xp)
  
if __name__ == "__main__":
    main()