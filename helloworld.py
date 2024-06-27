print("hello world")

x = 40075
y = 40076
if x < y:
    print("Der Umfang des Äquators beträgt 40.075 km")
elif x > y:
    print("bye world")
# elif ist eine Kombination aus else und if
# es überprüft weitere Optionen, bevor es else ausführt, oder auch nicht
#in diesem Fall wird weder elif noch else ausgeführt, da die if Bedingung stimmt.
else:
    print("no option")
# else wird hier nicht ausgegeben, da die if Bedingung stimmt

#whileschleife
z = 1 
while z < 51:
    print(z)
    z = z + 5
    # z wird immer um 5 vergröpert, mit dem neuen Wehrt wird weiter gerechnet
print("End")

#vorschleife
a = ['Becky', 'Lilly', 'Snowy']
for c in a:
    print(c)
print("Those three cutie cats of mine")

b = [10, 20, 30]
for d in b:
    if d >= 15:
        print("Woho")
print("done")
# auch möglich mit mehreren if - Bedingungen.
# in diesem Fall überprüft es beide Blöcke und gibt das jeweilige Ergebnis aus
# eine Schleife, egal wie viele Bedingungen darin stehen, wird immer von oben nach unten komplett ausgeführt

r = 10
while r >= 0:
    print(r)
    r = r - 1
print("This is the end")
