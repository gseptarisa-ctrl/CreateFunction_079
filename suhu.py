def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return value * 9/5 + 32  # Convert Celsius ke Fahrenheit
    elif unit.upper() == 'F':
        return (value - 32) * 5/9  # Convert Fahrenheit ke Celsius
    else:
        print("Tidak ada unit! Masukan unit 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

print ("==== Program Konversi Suhu ====")

input_suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu (C untuk Celsius/F untuk Fahrenheit): ")
konversi = convert_temperature(input_suhu, unit)
if unit.upper() == 'C':
    print(f"{input_suhu}°C = {konversi:.2f}°F")
elif unit.upper() == 'F':
    print(f"{input_suhu}°F = {konversi:.2f}°C")
else:
    print("satuan tidak dikenal.") 