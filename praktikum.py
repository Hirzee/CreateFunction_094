#Number 1
suhu = float(input("Add a Temperature: "))
satuan = input("Add a Unit (C/F): ")

def converts_temperature(val, unit):
    if unit == 'C' or unit == 'c':
        return (val * 9/5) + 32
    elif unit == 'F' or unit == 'f':
        return (val - 32) * 5/9
    else:
        return "Invalid unit"

if satuan == 'C' or satuan == 'c':
    print("Temperature in Fahrenheit: ", converts_temperature(suhu, satuan))
elif satuan == 'F' or satuan == 'f':
    print("Temperature in Celsius: ", converts_temperature(suhu, satuan))

