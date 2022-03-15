print("welcome to the Lbs & Kg converter")

wt = float(input("What is the Weight?: "))

unit = input("(K)g or (L)bs: ")

kg_lbs = wt*2.20462

lbs_kg = wt*.453592

if unit.upper() == "K":
    print("Lbs:", kg_lbs)
elif unit.upper() == "L":
    print("Kgs:", lbs_kg)

print("done")

