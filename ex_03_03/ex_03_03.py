score = input("Enter Score: ")
try:
    fsc = float(score)
except:
    print("Error, please enter numeric input")

if 0.0 <= fsc >= 1.0 :
    print("Error, please enter score from 0.0 to 1.0")
    quit()
else :
    if fsc >= 0.9 :
        print("A")
    elif fsc >= 0.8 :
        print("B")
    elif fsc >= 0.7 :
        print("C")
    elif fsc >= 0.6 :
        print("D")
    elif fsc >= 0.5 :
        print("F")
