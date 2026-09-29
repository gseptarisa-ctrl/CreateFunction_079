def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return value * 9/5 + 32  # Convert Celsius ke Fahrenheit
    elif unit.upper() == 'F':
        return (value - 32) * 5/9  # Convert Fahrenheit ke Celsius
    else:
        print("Tidak ada unit! Masukan unit 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

