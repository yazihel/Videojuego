

def mostrar_introduccion():
    print("==================================================")
    print("          LA GRAN AVENTURA DE SNOOPY              ")
    print("==================================================")
    print("Woodstock se ha perdido en el vecindario.")
    print("Snoopy debe encontrarlo antes de la hora de cenar.")
    print("Toma decisiones, gana puntos y obten recompensas.")
    print("==================================================")

def adivinar_numero(mensaje):


    while True:
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            print("Error: por favor ingresa un numero entero")

def mostrar_estado(perfil):

    print("--------------------------------------------------")
    print(f"Jugador: {perfil['nombre']} | Puntos: {perfil['puntos']}")
    
    print("Inventario: ", end="")
    if len(perfil["inventario"]) == 0:
        print("Vacio")
    else:
        for item in perfil["inventario"]:
            print(f"[{item}] ", end="")
    print("--------------------------------------------------")

def jugar_aventura():
    mostrar_introduccion()
    
    
    perfil = {
        "nombre": "Snoopy",
        "puntos": 0,
        "inventario": []
    }
    
    jugando = True
    nivel = 1
    
    
    while jugando:
        
        if perfil["puntos"] >= 50 and "Lentes de Aviador" not in perfil["inventario"]:
            print("*** HAZ DESBLOQUEADO UNA RECOMPENSA ***")
            print("te mereces una recompensa, encuentras los Lentes de Aviador.")
            print("¡Ahora eres el As para poder salvar a woodstock!")
            perfil["inventario"].append("Lentes de Aviador")
            
        mostrar_estado(perfil)
        
    
        if nivel == 1:
            print("[ Nivel 1: El barrio ]")
            print("Snoopy sale de su casita. Hay dos caminos:")
            print("1. Ir al campo de beisbol")
            print("2. Entrar a la casa de Charlie Brown")
            print("3. Rendirse y dormir (Salir del juego)")
            
            opcion = adivinar_numero("Elige una opcion (1-3): ")
            
            if opcion == 1:
                print("Snoopy va al campo y encuentra la manta de Linus tirada")
                print("Ganas 20 puntos.")
                perfil["puntos"] = perfil["puntos"] + 20
                perfil["inventario"].append("Manta")
                nivel = 2
            elif opcion == 2:
                print("Snoopy entra a la casa y Sally le da unas galletas")
                print("Ganas 30 puntos.")
                perfil["puntos"] = perfil["puntos"] + 30
                perfil["inventario"].append("Galletas")
                nivel = 2
            elif opcion == 3:
                print("Snoopy bosteza y se va a dormir")
                jugando = False
            else:
                print("Opcion no valida. Intenta de nuevo")
                
        
        elif nivel == 2:
            print("[ Nivel 2: El puesto de Lucy ]")
            print("Lucy se pone en frente de Snoopy y dice: Para pasar debes responder mi acertijo")
            print("¿Que figura geometrica es la cometa de Charlie Brown?")
            print("1. Un rombo")
            print("2. Un circulo")
            print("3. Un cuadrado")
            
            opcion = adivinar_numero("Tu respuesta (1-3): ")
            
            if opcion == 1:
                print("Lucy suspira: 'Correcto. Puedes pasar'")
                print("Ganas 30 puntos.")
                perfil["puntos"] = perfil["puntos"] + 30
                nivel = 3
            elif opcion == 2 or opcion == 3:
                print("Lucy grita: ¡Incorrecto! Cabeza de chorlito")
                print("Pierdes 10 puntos, pero logras escapar")
                perfil["puntos"] = perfil["puntos"] - 10
                nivel = 3
            else:
                print("Opcion no valida.")
                
        
        elif nivel == 3:
            print("[ Nivel 3: El arbol come-cometas ]")
            print("Snoopy escucha a Woodstock llorando arriba del arbol")
            print("1. trepar rapidamente a lo mas alto")
            print("2. ofrecer comida desde abajo")
            
            opcion = adivinar_numero("Que hara Snoopy (1-2): ")
            
            if opcion == 1:
            
                if "Lentes de Aviador" in perfil["inventario"]:
                    print("Snoopy usara sus Lentes de Aviador.")
                    print("se imagina que manejando su avioneta y trepa hasta la cima")
                    print("¡salvaste a Woodstock!")
                    perfil["puntos"] = perfil["puntos"] + 50
                    print("GANASTE")
                    jugando = False
                else:
                    print("Snoopy intenta trepar, pero resbala y cae.")
                    print("sin su equipo de aviador no pudo subir tan alto.")
                    print("PERDISTE.")
                    jugando = False
            elif opcion == 2:
                
                if "Galletas" in perfil["inventario"]:
                    print("Snoopy pone las Galletas en el suelo")
                    print("Woodstock baja al sentir el olor. ¡Lo salvaste!")
                    perfil["puntos"] = perfil["puntos"] + 40
                    print("GANASTE")
                    jugando = False
                else:
                    print("snoopy ladra, pero no tiene comida.")
                    print("Woodstock tiene demasiado miedo para bajar.")
                    print("PERDISTE.")
                    jugando = False
            else:
                print("Opcion no valida.")

    
    print("==================================================")
    print("               ETAPA FINAL                      ")
    print(f"puntaje Final: {perfil['puntos']} puntos")
    print("objetos recolectados en la aventura:")
    if len(perfil["inventario"]) == 0:
        print("ninguno")
    else:
        for item in perfil["inventario"]:
            print(f"- {item}")
    print("==================================================")


jugar_aventura()