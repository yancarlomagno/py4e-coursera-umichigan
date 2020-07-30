def computepay(h,r) :
    try:
        fh = float(h)
        fr = float(r)
    except:
        print("Error, please enter numeric input")
        quit()

    if fh <= 40 :
        xp = fh * fr
    else :
        xp = (40 * fr) + ((fh - 40) * (fr * 1.5))

    return xp

h = input("Enter Hours:")
r = input("Enter Rate:")

p = computepay(h,r)
print("Pay",p)
