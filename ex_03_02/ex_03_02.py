sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
        print("Error, please enter numeric input")
        quit()
        
if fh <= 40 :
    xp = fh * fr
else :
    xp = (40 * fr) + ((fh - 40) * (fr * 1.5))

print("Pay",xp)
