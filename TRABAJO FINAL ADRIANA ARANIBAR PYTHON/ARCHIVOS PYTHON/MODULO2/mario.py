print("Bienvenido al juego de Mario")
bandera = True
while True:
    try:
        inpu=str(input("""
          Elija una opción:
            1) Construir pirámide
            2) Salir
            Opción elegida: """))
        if inpu=="1":
            height=int(input("""
            Ingrese la altura de la piramide: """))
            if height<0:
               print("Ingrese un número válido: ")
            for i in range(height):
                print(" "*(height-i-1)+"#"*(i+1))
        elif inpu=="2":
                break
    except:
        print("Ingrese otro número: ")