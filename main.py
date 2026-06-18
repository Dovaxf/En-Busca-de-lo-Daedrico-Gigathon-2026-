#EN BUSCA DE LO DAÉDRICO

play = "1"

while play == "1":

    play = "0"

    #imports
    import random
    import turtle

    print("\nEN BUSCA DE LO DAÉDRICO\nby\nDamián Armona Suárez (El_Dovaxf)")

    #Mundo

    dagger_x = 90
    dagger_y = -90
    inn1_x = 30
    inn1_y = 50
    inn2_x = -60
    inn2_y = -80
    sanctuary_x = 30
    sanctuary_y = -70
    imperial_camp_x = -40
    imperial_camp_y = 60
    swamp_x = 80
    swamp_y = -70

    turtle.clearscreen()
    lapiz = turtle.Turtle()
    lapiz.speed(5)
    lapiz.penup()
    lapiz.goto(-100, -100)
    lapiz.pendown()

    for lapiz_lim in range(4):
        lapiz.forward(200)
        lapiz.left(90)

    lapiz.penup()
    lapiz.home()
    lapiz.pendown()

    #Nombre de la expedición
    name_expedition = "EN BUSCA DE LO DAÉDRICO"

    #Jugador
    name = input("\nIntroduzca un nombre para su personaje: ")
    if True:
        for variable_temporal in name:
            while variable_temporal.isdigit():
                name = input("\nIntroduzca un nombre válido\n(no se permiten números): ")
                if True:
                    for variable_temporal in name:
                        if not variable_temporal.isdigit():
                            break
    energy = 0
    player_x = 0
    player_y = 0
    action = 0
    shifts = 0
    dragon_decision = 0
    dead_dragon_counter = 0
    glory = 0
    clue_found = False
    sanctuary_found = False
    inn1_found = False
    inn2_found = False
    imperial_camp_found = False
    swamp_found = False
    victory = False
    final = 0

    print("\nA continuación elegirás con que cantidad de energía deseas iniciar tu partida (100, 50 o 25 puntos de energía).\nRecuerda que si tu energía llega a 0 regresarás al reino y terminará tu partida.")

    while energy != 25 or energy != 50 or energy != 100:
        try:
            energy = int(input("\n¿Con cuánta energía quieres comenzar?(Solo se admite 100, 50 o 25): "))
            if energy == 100 or energy == 50 or energy == 25:
                energy_initial = energy
                break
        except:
            print("\nSolo se admite 100, 50 o 25.")

    lapiz.dot(10)

    print(f"""\nCuarta Era, año 201.

    La guerra civil divide Skyrim.

    Mientras imperiales y capas de la tormenta luchan por el destino de la provincia, una amenaza más antigua vuelve a despertar.

    Los dragones han regresado.

    Y tú... {name}.

    Tú eres el Dovahkiin.

    El Sangre de Dragón.

    Guiado por rumores sobre un antiguo artefacto daédrico perdido en las montañas de Skyrim, emprendes una peligrosa expedición.

    Actualmente te encuentras en Carrera Blanca, una de las comarcas de Skyrim, el lugar dónde comienza tu aventura.\n""")

    if energy == 100:
        print("...Como sabías hoy que ibas a hacer una larga expedición, ayer te dormiste temprano y hoy con tiempo de sobra has desayunado en la posada\npara luego preparte con tu armadura, tu espada y tu escudo, por lo que te has ido totalmente renovado con 100 puntos de energía.")
    elif energy == 50:
        print("...Ayer se te pasó la hora mientras hacías otra de tus expediciones pero en cuánto llegaste a casa dormiste,\nlamentablemente no tuviste tiempo para comer mucho por lo que agarraste el primer pan que viste sobre la mesa y te lo comiste a toda prisa\nmientras te preparabas para salir a por tu siguiente aventura con 50 puntos de energía.")
    elif energy == 25:
        print("...Un verdadero Dovahkiin sabe divertirse y tú no eres menos,\npor lo que ayer, al regresar de tu última misión encomendada por el jarl de Carrera Blanca te fuiste a beber Aguamiel con frutos de enebro a La Yegua Abanderada,\npor lo que solo has dormido un par de horas, pero no necesitas más, ya que en cuanto te despierta la posadera porque ya es la hora de cerrar las habitaciones,\nrecoges tus cosas y sales en busca de nuevas riquezas con 25 puntos de energía.")

    print("Posición inicial: (0,0)")
    print("Orientación inicial de referencia: Este (0°)")

    print("\nLas siguientes acciones de movimiento consumen la misma cantidad de energía, 5 puntos de energía cada vez que se elije una de ellas.")
    print("Al seleccionar la acción de descansar podrás recuperar 10 puntos de energía.")
    print("Si decides explorar tienes una probabilidad de 0,3 para cada uno de los siguientes sucesos:")
    print("Encontrar provisiones (recupera 15 puntos de energía).\nEncontrar una pista sobre la ubicación del Santuario Daédrico.\nNo encontrar nada.")
    print("\nTODAS LAS ACCIONES CONSUMEN 1 TURNO\nSI CONSUME 50 TURNOS, SU PARTIDA TERMINARÁ\n\nEscriba 1, 2, 3, 4, 5 o 6 según las siguientes indicaciones:")
    print("\nAcciones de movimiento:\n")
    print("1 = Norte")
    print("2 = Sur")
    print("3 = Este")
    print("4 = Oeste")
    print("\n5 = Descansar")
    print("\n6 = Explorar")

    while energy > 0 and shifts < 50 and victory == False:

        while action not in [1,2,3,4,5,6]:
            try:
                action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3, 4, 5 o 6): "))
                if action == 1 or action == 2 or action == 3 or action == 4 or action == 5 or action == 6:
                    break
            except:
                print("\nSolo se admite 1, 2, 3, 4, 5 o 6.")

        if action == 1:
            player_y += 10
            energy -= 5
            shifts += 1
            lapiz.setheading(90)
            lapiz.forward(10)
            print("\nHas decidido avanzar hacia el Norte.")

        elif action == 2:
            player_y -= 10
            energy -= 5
            shifts += 1
            lapiz.setheading(270)
            lapiz.forward(10)
            print("\nHas decidido avanzar hacia el Sur.")
            
        elif action == 3:
            player_x += 10
            energy -= 5
            shifts += 1
            lapiz.setheading(0)
            lapiz.forward(10)
            print("\nHas decidido avanzar hacia el Este.")

        elif action == 4:
            player_x -= 10
            energy -= 5
            shifts += 1
            lapiz.setheading(180)
            lapiz.forward(10)
            print("\nHas decidido avanzar hacia el Oeste.")

        elif action == 5:
            energy += 10
            shifts += 1
            print("\nHas decidido descansar.")
            action = 0

        elif action == 6:
            if clue_found == False:
                exploration = random.randint(1, 3)
                shifts += 1
                print("\nHas decidido explorar la zona.")
                if exploration == 1:
                    energy += 15
                    print("\nHas encontrado algunas provisiones.\nHas recuperado 15 puntos de energía.")
                elif exploration == 2:
                    print(f"\nParece que los antiguos sacerdotes de Boethiah dejaron una pista.\nHas encontrado una inscripción con la ubicación del Santuario Daédrico.\nEl santuario se encuentra en ({sanctuary_x}, {sanctuary_y}).")
                    clue_found = True
                elif exploration == 3:
                    print("\nNo has encontrado nada.")
            else:
                exploration = random.randint(1, 3)
                shifts += 1
                print("\nHas decidido explorar la zona.")
                if exploration == 1:
                    energy += 15
                    print("\nHas encontrado algunas provisiones.\nHas recuperado 15 puntos de energía.")
                elif exploration == 2:
                    print(f"\nYa habías encontrado esta pista.\nEl santuario se encuentra en ({sanctuary_x}, {sanctuary_y}).")
                elif exploration == 3:
                    print("\nNo has encontrado nada.")
            action = 0

        special_place = (
                (player_x, player_y) == (sanctuary_x, sanctuary_y)
                or (player_x, player_y) == (inn1_x, inn1_y)
                or (player_x, player_y) == (inn2_x, inn2_y)
                or (player_x, player_y) == (imperial_camp_x, imperial_camp_y)
                or (player_x, player_y) == (swamp_x, swamp_y)
                or (player_x, player_y) == (dagger_x, dagger_y)
                )
        
        if action in [1,2,3,4] and not special_place:
            event = random.randint(1, 20)
            action = 0

            if event == 10 or event == 20:
                print(f"\n{name}, ha llegado tu momento.\nHa aparecido un dragón.\nEs hora de que demuestres que eres digno del título del mayor matadragones que ha existido en Tamriel.\nDOVAHKIIN.")
                while dragon_decision != "1" or dragon_decision != "2":
                    dragon_decision = input("\n¿Decides huir(1) o luchar(2) contra él?(Solo se admite 1 o 2): ")
                    if dragon_decision == "1":
                        energy -= 10
                        print("\nHas decidido evitar el combate.\nSabes que no es el mejor momento para enfrentarte a un dragón debido a que has perdido mucha energía durante tu viaje.\nAsí que te alejas de la zona con un hechizo de invisibilidad y corres lo más rapido que puedes.")
                        print("Has perdido 10 puntos de energía.")
                        break
                    elif dragon_decision == "2":
                        energy -= 25
                        if energy > 0:
                            glory += 50
                            dead_dragon_counter += 1
                            print("\nEres tal y cómo cuentan las leyendas, has derrotado al dragón y has demostrado que eres el mayor matadragones de todos los tiempos.")
                            print("Buen trabajo, Dovahkiin.")
                            print("Has perdido 25 puntos de energía.")
                            break
                        else:
                            print("\nEl enfrentamiento estaba muy igualado pero toda tu aventura te ha dejado casi sin fuerzas y te has quedado sin energía en medio de tu batalla.\nHas utilizado un hechizo de invisibilidad para escapar antes de resibir un golpe mortal pero por ahora no podrás continuar con tu aventura.")
                            break

            if event == 6:
                print("\nSe ha formado un tornado cerca de tí y te ha alcanzado.\nHas sobrevivido sin problemas ya que te protegiste con magia de alteración pero el tornado te ha llevado a una nueva ubicación.")
                player_x = random.randint(-10, 10) * 10
                player_y = random.randint(-10, 10) * 10
                lapiz.penup()
                lapiz.goto(player_x, player_y)
                lapiz.pendown()

            if event == 2 or event == 8:
                print("\nTe has cruzado con una caravana de khajiitas.\nHas comprado algunas provisiones con parte del dinero que te llevaste y has recuperado 10 puntos de energía.")
                energy += 10
        else:
            action = 0

        if player_x > 100:
            player_x = 100
            print("\nHas llegado a los límites de Skyrim, intentaste escalar las montañas que te rodean pero al ser tan altas no lo conseguiste.")
        if player_x < -100:
            player_x = -100
            print("\nHas llegado a los límites de Skyrim, intentaste escalar las montañas que te rodean pero al ser tan altas no lo conseguiste.")
        if player_y > 100:
            player_y = 100
            print("\nHas llegado a los límites de Skyrim, intentaste escalar las montañas que te rodean pero al ser tan altas no lo conseguiste.")
        if player_y < -100:
            player_y = -100
            print("\nHas llegado a los límites de Skyrim, intentaste escalar las montañas que te rodean pero al ser tan altas no lo conseguiste.")

        if player_x == dagger_x and player_y == dagger_y:
            glory += 100
            victory = True

        if player_x == sanctuary_x and player_y == sanctuary_y:
            if sanctuary_found == False:
                sanctuary_found = True
                print("\nLlegaste al Santuario Daédrico.")
                if energy > 0:

                    print("""\nHace mucho tiempo, en este lugar, se celebraron grandes rituales daédricos para poder invocar a los guerreros provenientes de Oblivion y a sus Dioses.
                        
                        En este sitio hay muchos documentos y tablillas antiguas pero hay una que resalta más sobre las demás.
                        
                        Esta habla sobre un objeto tan poderoso creado por el mismísimo Mehrunes Dagon, el Dios daédrico y Príncipe de la destrucción, el cambio y la ambición.
                        
                        Según este grabado en piedra, los humanos querían invocar a Mehrunes Dagon para que este les otorgara parte de su poder.
                        
                        Pero este no aceptó su solicitud y acabó con todos con la famosa "Navaja de Mehrunes", un arma tan poderosa, que es capaz de aniquilar a cualquier enemigo de un solo corte.
                        
                        Debido a que los humanos que lo invocaron fueron asesinados el contrato se rompió.
                        
                        Mehrunes Dagon regresó a Oblivion pero como había utilizado su poder para materializar parte de este en forma de un arma, esta última se quedó en nuestro mundo.
                        
                        Se cuenta que tiempo después llegó un humano a ese mismo Santuario y encontró la daga en el suelo.
                        
                        Debido al temor que sintió al notar la presencia de Mehrunes Dagon decidió ocultarla en un cofre de una cueva lejana y dejó una inscripción en el Santuario.
                        
                        Porque sabía que algún día aparecería otro Sangre de Dragón que llegaría hasta allí y que preservaría a buen recaudo la daga.
                        
                        Ese humano era Tiber Septim.
                        
                        EL GRAN TALOS
                        
                        El único humano que logró ser reconocido como un DIOS
                        
                        El Dios de la guerra, la ley, la justicia y el gobierno""")
                    
                    print(f"""\nLeyendo todas las inscripciones descubres que la "Navaja de Mehrunes" se encuentra en ({dagger_x}, {dagger_y}).""")

                elif energy <= 0:
                    print(f"\nHas viajado mucho tiempo y te sientes agotado.\nComo te has quedado sin energía decides esperar en el camino y de repente aparece una caravana de imperiales que te acercan al pueblo más cercano.\nDe momento este es el final de tu aventura pero sabes que esto no acaba aquí, volverás con más fuerza y cumplirás tu objetivo.\n\nFIN DE LA PARTIDA\n")
                    break

                if shifts == 50:
                    print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                    break
                    
                while action not in [1,2,3,4]:
                    try:
                        action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                        if action == 1 or action == 2 or action == 3 or action == 4:
                            break
                    except:
                        print("\nSolo se admite 1, 2, 3 o 4.")
                
                if action == 1:
                    player_y += 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(90)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Norte.")
                    action = 0
                elif action == 2:
                    player_y -= 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(270)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Sur.")
                    action = 0
                elif action == 3:
                    player_x += 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(0)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Este.")
                    action = 0
                elif action == 4:
                    player_x -= 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(180)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Oeste.")
                    action = 0

            else:

                print("\nYa habías estado en este santuario.")

                if energy > 0:
                    print(f"""\nVuelves a leer las antiguas inscripciones.\nLa "Navaja de Mehrunes" se encuentra en ({dagger_x}, {dagger_y}).""")

                elif energy <= 0:
                    print(f"\nHas viajado mucho tiempo y te sientes agotado.\nComo te has quedado sin energía decides esperar en el camino y de repente aparece una caravana de imperiales que te acercan al pueblo más cercano.\nDe momento este es el final de tu aventura pero sabes que esto no acaba aquí, volverás con más fuerza y cumplirás tu objetivo.\n\nFIN DE LA PARTIDA\n")
                    break

                if shifts == 50:
                    print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                    break
                    
                while action not in [1,2,3,4]:
                    try:
                        action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                        if action == 1 or action == 2 or action == 3 or action == 4:
                            break
                    except:
                        print("\nSolo se admite 1, 2, 3 o 4.")
                
                if action == 1:
                    player_y += 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(90)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Norte.")
                    action = 0
                elif action == 2:
                    player_y -= 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(270)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Sur.")
                    action = 0
                elif action == 3:
                    player_x += 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(0)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Este.")
                    action = 0
                elif action == 4:
                    player_x -= 10
                    energy -= 5
                    shifts += 1
                    lapiz.setheading(180)
                    lapiz.forward(10)
                    print("\nHas decidido avanzar hacia el Oeste.")
                    action = 0

        if player_x == inn1_x and player_y == inn1_y:
            inn1_found = True
            energy += 20
            print("""
                Has llegado a la Posada "El Gigante Dormido".
                Has recuperado 20 puntos de energía.""")
            
            if shifts == 50:
                print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                break
            if energy > 0:
                print(f"\nEstás en ({player_x}, {player_y}) y te quedan {energy} puntos de energía.")

            while action not in [1,2,3,4]:
                try:
                    action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                    if action == 1 or action == 2 or action == 3 or action == 4:
                        break
                except:
                    print("\nSolo se admite 1, 2, 3 o 4.")
        
            if action == 1:
                player_y += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(90)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Norte.")
                action = 0
            elif action == 2:
                player_y -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(270)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Sur.")
                action = 0
            elif action == 3:
                player_x += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(0)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Este.")
                action = 0
            elif action == 4:
                player_x -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(180)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Oeste.")
                action = 0

        if player_x == inn2_x and player_y == inn2_y:
            inn2_found = True
            energy += 20
            print("""
                Has llegado a la "Posada de los Cuatro Escudos".
                Has recuperado 20 puntos de energía.""")
            
            if shifts == 50:
                print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                break
            if energy > 0:
                print(f"\nEstás en ({player_x}, {player_y}) y te quedan {energy} puntos de energía.")

            while action not in [1,2,3,4]:
                try:
                    action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                    if action == 1 or action == 2 or action == 3 or action == 4:
                        break
                except:
                    print("\nSolo se admite 1, 2, 3 o 4.")
        
            if action == 1:
                player_y += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(90)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Norte.")
                action = 0
            elif action == 2:
                player_y -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(270)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Sur.")
                action = 0
            elif action == 3:
                player_x += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(0)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Este.")
                action = 0
            elif action == 4:
                player_x -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(180)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Oeste.")
                action = 0

        if player_x == imperial_camp_x and player_y == imperial_camp_y:
            imperial_camp_found = True
            action_camp = random.randint(1, 2)
            print("\nHas llegado a un campamento de soldados imperiales")
            if action_camp == 1:
                energy += 15
                print("\nLos soldados imperiales te han visto pasar y como vieron que estabas de expedición decidieron darte algunas provisiones para recuperar fuerzas.")
                print("Has recuperado 15 puntos de energía.")
                print("Los imperiales recogieron el campamento y han partido.")
                imperial_camp_x = 1000
                imperial_camp_y = 1000
            else:
                energy -= 30
                print("\nLos soldados imperiales te han confundido con un soldado de los Capas de la Tormenta y has tenido que enfrentarte a ellos.")
                print("Has arrasado con todo el campamento.")
                print("Has perdido 30 puntos de energía.")
                imperial_camp_x = 1000
                imperial_camp_y = 1000               

            if shifts == 50:
                print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                break
            if energy > 0:
                print(f"\nEstás en ({player_x}, {player_y}) y te quedan {energy} puntos de energía.")
            elif energy <= 0:
                print(f"\nHas viajado mucho tiempo y te sientes agotado.\nComo te has quedado sin energía decides esperar en el camino y de repente aparece una caravana de imperiales que te acercan al pueblo más cercano.\nDe momento este es el final de tu aventura pero sabes que esto no acaba aquí, volverás con más fuerza y cumplirás tu objetivo.\n\nFIN DE LA PARTIDA\n")
                break

            while action not in [1,2,3,4]:
                try:
                    action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                    if action == 1 or action == 2 or action == 3 or action == 4:
                        break
                except:
                    print("\nSolo se admite 1, 2, 3 o 4.")
        
            if action == 1:
                player_y += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(90)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Norte.")
                action = 0
            elif action == 2:
                player_y -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(270)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Sur.")
                action = 0
            elif action == 3:
                player_x += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(0)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Este.")
                action = 0
            elif action == 4:
                player_x -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(180)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Oeste.")
                action = 0

        if player_x == swamp_x and player_y == swamp_y:
            swamp_found = True
            energy -= 25
            print("\nLlegaste al peligroso pantano de la Ciénaga de Hjaalmarch.\nTuviste que enfrentarte a varios Cangrejos del Barro mientras atravesabas con gran dificultad la zona pantanosa.")
            print("Perdiste 25 puntos de energía.")

            if shifts == 50:
                print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
                break
            if energy > 0:
                print(f"\nEstás en ({player_x}, {player_y}) y te quedan {energy} puntos de energía.")
            elif energy <= 0:
                print(f"\nHas viajado mucho tiempo y te sientes agotado.\nComo te has quedado sin energía decides esperar en el camino y de repente aparece una caravana de imperiales que te acercan al pueblo más cercano.\nDe momento este es el final de tu aventura pero sabes que esto no acaba aquí, volverás con más fuerza y cumplirás tu objetivo.\n\nFIN DE LA PARTIDA\n")
                break

            while action not in [1,2,3,4]:
                try:
                    action = int(input("\n¿Hacia dónde quieres ir?(solo se admite 1, 2, 3 o 4): "))
                    if action == 1 or action == 2 or action == 3 or action == 4:
                        break
                except:
                    print("\nSolo se admite 1, 2, 3 o 4.")
        
            if action == 1:
                player_y += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(90)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Norte.")
                action = 0
            elif action == 2:
                player_y -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(270)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Sur.")
                action = 0
            elif action == 3:
                player_x += 10
                energy -= 5
                shifts += 1
                lapiz.setheading(0)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Este.")
                action = 0
            elif action == 4:
                player_x -= 10
                energy -= 5
                shifts += 1
                lapiz.setheading(180)
                lapiz.forward(10)
                print("\nHas decidido avanzar hacia el Oeste.")
                action = 0

        if victory == True:
            print(f"""
                    FELICIDADES
                    
                    En ({player_x}, {player_y}) has encontrado la cueva en la que estaba escondido el cofre que contenía la famosa y poderosa "Navaja de Mehrunes".
                    Ahora que está está entre tus posesiones, sabes que no caerá en manos equivocadas.
                    Y podrás utilizarla en tus futuras aventuras y batallas contra dragones para liberar a Skyrim de ese antiguo mal renacido por Alduin.

                    FIN DE LA PARTIDA\n""")
            break

        if shifts == 50:
            print(f"""\nCincuenta jornadas han pasado desde el inicio de la expedición.\nA pesar de tus esfuerzos, el artefacto daédrico no ha sido encontrado.\nEl destino de la legendaria "Navaja de Mehrunes" continúa siendo un misterio.\nFIN DE LA PARTIDA\n""")
            break

        if energy > 0:
            print(f"\nEstás en ({player_x}, {player_y}) y te quedan {energy} puntos de energía.")
        elif energy <= 0:
            energy = 0
            print(f"\nHas viajado mucho tiempo y te sientes agotado.\nComo te has quedado sin energía decides esperar en el camino y de repente aparece una caravana de imperiales que te acercan al pueblo más cercano.\nDe momento este es el final de tu aventura pero sabes que esto no acaba aquí, volverás con más fuerza y cumplirás tu objetivo.\n\nFIN DE LA PARTIDA\n")
            break

    lapiz.dot(10)

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    print("        ======INFORME FINAL======        ")

    print(f"\nNombre de la expedición:\n{name_expedition}")

    print(f"\nNombre: {name}")

    print(f"\nEnergía inicial: {energy_initial}\n\nEnergía restante: {energy}")

    print(f"\nHas terminado tu aventura en ({player_x}, {player_y}).")

    print(f"\nTurnos consumidos: {shifts}")

    if sanctuary_found == True:
        print("\nHas encontrado el Santuario Daédrico y descubierto su historia.")

    if inn1_found == True:
        print("""\nHas encontrado la Posada "El Gigante Dormido". """)

    if inn2_found == True:
        print("""\nHas encontrado la "Posada de los Cuatro Escudos". """)

    if imperial_camp_found == True:
        print("\nHas encontrado el campamento imperial.")

    if swamp_found == True:
        print("\nHas encontrado el peligroso pantano de la Ciénaga de Hjaalmarch")
            
    if dead_dragon_counter >= 1:
        print("\nHas demostrado ser digno del título del mayor matadragones de todos los tiempos, DOVAHKIIN.")
        if dead_dragon_counter == 1:
            print("Absorbiste el alma de un dragón.")
        elif dead_dragon_counter > 1:
            print(f"Absorbiste el alma de {dead_dragon_counter} dragones.")

    print(f"\nGloria conseguida: {glory}")

    print("\nCausa de finalización:")
    if victory == True:
        print("""Has recuperado la "Navaja de Mehrunes" y has cumplido tu objetivo.""")
    if shifts == 50 and energy > 0:
        print("Alcanzaste tu límite de turnos.")
    if energy <= 0 and shifts < 50:
        print("Se agotó toda tu energía")
    if energy <= 0 and shifts == 50:
        print("Alcanzaste tu límite de turnos y agotaste toda tu energía.")

    if victory == True and glory >= 150:
        print("""
    Has recuperado la "Navaja de Mehrunes" y has demostrado ser digno del título de Dovahkiin.
    Los bardos cantarán tus hazañas durante generaciones y tus historias llegarán a más continentes de Tamriel.
              """)

    if victory == True and glory < 150:
        print("""
    Has recuperado la "Navaja de Mehrunes" pero solo los habitantes de Carrera Blanca conocen tu historia.
    Celebrarás esta victoria con tus amigos del bar y bailaréis junto al fuego toda la noche para disfrutar esta nueva victoria del Dovahkiin.
              """)

    if victory == False:
        print("""
    No has recuperado la "Navaja de Mehrunes" pero al regresar a Carrera Blanca tus compañeros del Gremio de Guerreros se han ofrecido para ayudarte en tu próxima expedición.
    Todos están de acuerdo en que la navaja es demasiado peligrosa y hay que tenerla a buen recaudo lo más rápido posible.
    Contarás tu pequeño viaje por los Páramos de Skyrim a tus amigos y os reiréis contando chistes mientras tomáis el mejor aguamiel de todo Tamriel.
              """)
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#              

    print ("Este ha sido el progreso y el recorrido de toda tu partida" \
    "\nCuando desees terminar escribe --->" \
    "\nFus Ro Dah" \
    "\nY así superarás la última prueba para demostrar que eres el verdadero DOVAHKIIN")

    while final != "Fus Ro Dah":
        final = input("""\nEscribe "Fus Ro Dah" para superar tu última prueba: """)
        if final == "Fus Ro Dah":
            print("""
                  === Que Akatosh te bendiga y te proteja, DOVAHKIIN ===""")
            break

    while play != "1" and play != "2":
        play = input(""" 
        ¿Desea iniciar una nueva partida?" Sí(1) / No(2): """)
        if play == "1" or play == "2":
            break
    if play == "1":
        print(f"\n=== Y el Dovahkiin lo volvió a hacer ===")
    else:
        print("")