user_weight =int(input("weight:"))
weight_unit = input("(L)bs or (K)g: ").lower()

if weight_unit == 'l':
    weight_kg = user_weight * 0.453592
    print(f"you are {weight_kg} kilos")
else:
    weight_lb = user_weight * 2.20462
    print((f"you are {weight_lb} pounds"))