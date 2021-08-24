"""
[] - Lists
{} - Dictionary
() - set
<> - tuple
"""
myCar = ["Tesla", "Roadster", "Rolls Royce"]
for car in myCar:
    print(car)
print("\n")
#print(myCar.count("Tesla"))

myWatch = ("Titan", "Rado", "Fastrack")
for watch in myWatch:
    print(watch)
print("\n")

myFavCar = {"Model" : 2002,
            "Color" : "Black",
            "Brand" : "Lambo"}

for Mycar in myFavCar.items():
    print(Mycar)