# Inicio
print("La Búsqueda del Tesoro Perdido")  
print("Eres un joven aventurero llamado Alex que ha escuchado rumores sobre un tesoro escondido en una isla remota. La leyenda dice que el tesoro fue escondido por un famoso pirata hace muchos años y que está protegido por acertijos y desafíos.")  # Se muestra directamente
print("Después de un largo viaje en barco, Alex finalmente llega a la isla. La isla está cubierta de vegetación exuberante y tiene una atmósfera misteriosa. Alex sabe que el tesoro está en algún lugar de la isla, pero no tiene idea de por dónde empezar a buscar.")  # Se muestra directamente

# Nivel 1
print("Alex se encuentra en la playa, donde hay tres caminos posibles:")
print("IZQUIERDA: lleva a una cueva misteriosa.")
print("CENTRO: conduce a una montaña rocosa.")
print("DERECHA: lleva a un bosque oscuro y denso.")
print("¿Qué camino elige Alex?")

decision = input("> ").upper()  

if decision == "IZQUIERDA":
    print("Te encuentras en una cueva misteriosa.")
    print("Oyes un crujido detrás de ti. ¿Qué haces?")
    print("ESPERAR o HUIR")
    decision2 = input("> ").upper()  

    if decision2 == "ESPERAR":
        print("Te quedas a ver que sucede!!")
        print("Un oso grizzly aparece y te ataca. ¡GAME OVER!")

    elif decision2 == "HUIR":
        print("Logras escapar del oso. ¡Has sobrevivido!")
        print("Pero te rindes y vuelves a casa")

    else:
        print("Opción no válida. El oso te atrapa. ¡GAME OVER!")

elif decision == "CENTRO": 
    print("Subes la montaña rocosa con dificultad.")
    print("Llegas a un cruce. ¿Qué camino tomas?")
    print("IZQUIERDA o DERECHA")
    decision2 = input("> ").upper()

    if decision2 == "IZQUIERDA":
        print("Encuentras una cascada. ¿Intentas cruzarla o la rodeas?")
        print("CRUZAR o RODEAR")
        decision3 = input("> ").upper()
        

    elif decision2 == "DERECHA":
        print("Llegas a la cima de la montaña. ¡Has encontrado el tesoro!")
        print("GANASTE!")
        print("FIN DEL JUEGO.")
    else:
        print("Opción no válida. Te caes por un precipicio. ¡GAME OVER!")

elif decision == "DERECHA": 
    print("Te adentras en el bosque oscuro.")
    print("Te encuentras con un lobo hambriento. ¿Qué haces?")
    print("LUCHAR o ESCAPAR")
    decision2 = input("> ").upper()

    if decision2 == "LUCHAR":
        print("Luchas contra el lobo y lo vences. ¡Has demostrado tu valentía!")

    elif decision2 == "ESCAPAR":
        print("Escapas del lobo y encuentras un camino seguro.")

    else:
        print("Opción no válida. El lobo te atrapa. ¡GAME OVER!")

else:
    print("Opción no válida. No sabes adónde ir. ¡GAME OVER!")

