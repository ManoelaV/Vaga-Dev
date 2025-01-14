def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida


string_original = input("Informe uma string: ")


string_invertida = inverter_string(string_original)


print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")