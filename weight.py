weigth=int(input("Weigth: "))
unit= input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted=weigth*0.45
    print(f"your are {converted} kilos")
else:
   converted=  weigth/0.45
   print(f"your are {converted} pounds")