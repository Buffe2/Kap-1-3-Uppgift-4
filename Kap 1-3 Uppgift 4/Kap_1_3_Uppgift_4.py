x = input("Hur mycket kostar kladesplagget i kronor?")
x1 = float(x)
y = input("Hur mycket rabatt har du i heltal?")
y1 = int(y)
pris=x1*(1-y1/100)
print("Grattis du far en rabatt pa", y, "%") 
print("Ditt plagg kostar nu", pris,"kronor")

