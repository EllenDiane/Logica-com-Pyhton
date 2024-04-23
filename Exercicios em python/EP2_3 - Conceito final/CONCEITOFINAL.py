n1 = float(input())
n2 = float(input())
n3 = float(input())
p1 = float(input())
p2 = float(input())

t = (n1 + n2 + n3) / 3
nf =  (t*0.2) + (p1*0.4) + (p2*0.4)

print("{:.2f}".format(nf))

if 9 <= nf <= 10:
    print("A")
elif 7.5 <= nf < 9:
    print("B")
elif 6 <= nf < 7.5:
    print("C")
elif 5 <= nf < 6:
    print("D")
elif nf < 5:
    print("F")
    