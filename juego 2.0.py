# Inicio
print("La Búsqueda del Tesoro Perdido")
print("Eres un joven aventurero llamado Alex que ha escuchado rumores sobre un tesoro escondido en una isla remota. La leyenda dice que el tesoro fue escondido por un famoso pirata hace muchos años y que está protegido por acertijos y desafíos.")
print("Después de un largo viaje en barco, Alex finalmente llega a la isla. La isla está cubierta de vegetación exuberante y tiene una atmósfera misteriosa. Alex sabe que el tesoro está en algún lugar de la isla, pero no tiene idea de por dónde empezar a buscar.")

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
        print("Sigues explorando la cueva y encuentras un pasadizo secreto.")
        print("El pasadizo te lleva a una cámara oculta donde encuentras un mapa antiguo.")
        print("El mapa muestra la ubicación del tesoro. ¡Has ganado!")
        print("Con el mapa en mano, Alex regresa a casa y planea su próxima aventura.")
        print("¡FIN!")

    else:
        print("Opción no válida. El oso te atrapa. ¡GAME OVER!")

elif decision == "CENTRO":
    print("Subes la montaña rocosa con dificultad.")
    print("Llegas a una bifurcación. ¿Qué camino tomas?")
    print("IZQUIERDA o DERECHA")
    decision2 = input("> ").upper()

    if decision2 == "IZQUIERDA":
        print("Encuentras una cascada. ¿Intentas cruzarla o la rodeas?")
        print("CRUZAR o RODEAR")
        decision3 = input("> ").upper()

        if decision3 == "CRUZAR":
            print("La corriente te arrastra y te caes por un precipicio. ¡GAME OVER!")

        elif decision3 == "RODEAR":
            print("Rodeas la cascada y encuentras un camino oculto.")
            print("El camino te lleva a un claro donde encuentras una brújula mágica.")
            print("La brújula te guía hasta el tesoro. ¡Has ganado!")
            print("Con la brújula y el tesoro, Alex regresa a casa y se convierte en un famoso explorador.")
            print("¡FIN!")

        else:
            print("Opción no válida. Te pierdes en la montaña. ¡GAME OVER!")

    elif decision2 == "DERECHA":
        print("Llegas a la cima de la montaña, pero no encuentras nada.")
        print("Decides regresar a la playa y probar otro camino. ¡Te has rendido!")
        print("Alex regresa a casa decepcionado, pero aprende una valiosa lección sobre la perseverancia.")
        print("¡FIN!")

    else:
        print("Opción no válida. Te caes por un precipicio. ¡GAME OVER!")

elif decision == "DERECHA":
    print("Te adentras en el bosque oscuro.")
    print("Te encuentras con un lobo hambriento. ¿Qué haces?")
    print("LUCHAR o ESCAPAR")
    decision2 = input("> ").upper()

    if decision2 == "LUCHAR":
        print("Luchas contra el lobo y lo vences. ¡Has demostrado tu valentía!")
        print("Sigues adentrándote en el bosque y encuentras una cabaña abandonada.")
        print("Dentro de la cabaña, encuentras un diario antiguo.")
        print("El diario contiene pistas sobre la ubicación del tesoro. ¡Has ganado!")
        print("Con las pistas del diario, Alex encuentra el tesoro y regresa a casa como un héroe.")
        print("¡FIN!")

    elif decision2 == "ESCAPAR":
        print("Escapas del lobo y encuentras un camino seguro.")
        print("El camino te lleva de vuelta a la playa. ¡Has sobrevivido, pero no has encontrado el tesoro!")
        print("Alex decide intentarlo de nuevo al día siguiente, aprendiendo de sus errores.")
        print("¡FIN!")

    else:
        print("Opción no válida. El lobo te atrapa. ¡GAME OVER!")

else:
    print("Opción no válida. No sabes adónde ir. ¡GAME OVER!")