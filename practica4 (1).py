usuario = int(input("Determine el primer numero "))
usuario2 = int(input("Determine el segundo numero "))
usuario3 = int(input("Determine el tercero numero "))
# Determinar el mayor de los tres numeros
if usuario >= usuario2 and usuario >= usuario3:
    mayor = usuario
elif usuario2 >= usuario1 and usuario2 >= usuario3:
    mayor = usuario2
else:
    mayor = usuario3
    
# Determinar el maenor de los tres numeros
if usuario <= usuario2 and usuario <= usuario3:
    menor = usuario2
elif usuario2 <= usuario and usuario2 <= usuario3:
    menor = usuario2
else:
    menor = usuario3
print(f"el mayor de los tres numeros es: {mayor}")
print(f"el menor de los tres numeros es: {menor}")