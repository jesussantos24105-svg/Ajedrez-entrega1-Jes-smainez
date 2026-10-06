

#Constantes del tablero 
tamano_tablero: int=8
letras_validas: str='abcdefgh'
numeros_validos: str= '12345678'
Encabezado: str = " "
columnaprint: float = 0
turno: int = 1

#Creamos el tablero con los simbolos
#El "[list[str]]" no es necesario pero sí muy útil, hace que el programa sea más estricto y esté atento a cualquier valor que este fuera de str, (no permitiría números o por lo menos te aviasría).
tablero_simbolos: list[list[str]] = [
    ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"],  # fila 8 (piezas negras)
    ["\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"],  # fila 7 (peones negros)
    [".", ".", ".", ".", ".", ".", ".", "."],                                                  # fila 6 (vacia)
    [".", ".", ".", ".", ".", ".", ".", "."],                                                  # fila 5 (vacia)
    [".", ".", ".", ".", ".", ".", ".", "."],                                                  # fila 4 (vacia)
    [".", ".", ".", ".", ".", ".", ".", "."],                                                  # fila 3 (vacia)
    ["\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"],  # fila 2 (peones blancos)
    ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"],  # fila 1 (piezas blancas)
]
"""En este apartado bien como indica, estamos creando el encabezado o columnas para ello vamos a utilizar el bucle for in range de 8 que es el tamaño
del tablero.

Llamamos encabezzAdo por ponerle un nombre pero no es estrictamente necesario, a mi parecer es más intuitivo, pero como luego observamos
que su uso es meramente para ir de la posición del 0-7 de las letras válidas, luego tenemos el encabezado de la línea 30 que nos permite 
acumular las letras que vamos extrayendo"""

for encabezzAdo in range (tamano_tablero):
     letras_columna: str= (letras_validas[encabezzAdo])
     Encabezado = Encabezado + " " + letras_columna + " "
print(Encabezado)

"""Ahora vamos a crear las líneas, creamos un bucle dentro de un bucle que irá recorriendo las casillas del tablero la cual reconocerá
que existe en esa casilla y según lo que haya (por ejemplo si la casilla no tiene nada imprimirá un vacío porque ya hemos añadido manualmente los puntos en 
nuestra lista, (en caso de que no hubiésemos puesto los puntos de forma manual tendriamos que añadir en la línea 44 un "."), y si reconoce un símbolo 
(una pieza de ajedrez) imprimirá esa pieza entre dos espacios """
for indice_fila in range(tamano_tablero):
     numero_fila: int = tamano_tablero - indice_fila #Para que se adapte el rango de (0-7)
     linea: str= str(numero_fila) + " " 
     for indice_columnam in range(tamano_tablero):
          simbolo: str= tablero_simbolos[indice_fila][indice_columnam]
          if simbolo == "":
               celda: str = ""
          else:
               celda: str =" " + simbolo  + " "
          linea: str = linea + celda
     print(linea)

#Creamos el tablero con el nombre de las piezas, para poder localizarlas en un futuro con su nombre y no con un código.
tablero_nombres: list[list[str]] = [
    ["Torre negra", "Caballo negro", "Alfil negro", "Dama negra", "Rey negro", "Alfil negro", "Caballo negro", "Torre negra"],
    ["Peón negro", "Peón negro", "Peón negro", "Peón negro", "Peón negro", "Peón negro", "Peón negro", "Peón negro"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["Peón blanco", "Peón blanco", "Peón blanco", "Peón blanco", "Peón blanco", "Peón blanco", "Peón blanco", "Peón blanco"],
    ["Torre blanca", "Caballo blanco", "Alfil blanco", "Dama blanca", "Rey blanco", "Alfil blanco", "Caballo blanco", "Torre blanca"]
]

"""Iniciamos el juego, se empieza en turno de blanca por las reglas del ajedrez."""
estado: str = "turno blancas"

"""Creamos un bucle infinito que nos pida casillas tantas veces hasta que se encuentre algo que lo rompa ("salir")."""

while estado != "salir":
    if estado == "turno blancas":
        print("Turno blancas")
        print(f"Turno {turno}")
        casilla: str = input("casilla que desea ir: ").strip().lower () #Añado estas dos funciones para que aunque el usuario ponga separaciones o escriba las letras en mayísculas la terminal pueda seguir leeyendolo.
        #Primero quiero comprobar si quiere salir porque en el caso que quiera no debo contener ni mostrar más información#
        if casilla == "salir".strip(). lower():
            estado = "salir"
            """En caso de que no quiera salir revisamos toda la longitud del input que nos ha dado, debe cumplir que esta dentro 
            de las letras y números válidos"""
        elif len(casilla) == 2 and (casilla[0]in letras_validas) and (casilla[1] in numeros_validos):
            letras_columna: str = casilla [0]
            columna: int = 0 
            """El código tiene asignado el valor de las casillas en números por eso según la letra que sea debemos asignarle su valor correspondiente
            en números"""
            if letras_columna == "a":
                columna=0
            elif letras_columna == "b":
                columna=1
            elif letras_columna == "c":
                columna=2
            elif letras_columna == "d":
                columna=3
            elif letras_columna == "e":
                columna=4
            elif letras_columna == "f":
                columna=5
            elif letras_columna == "g":
                columna=6
            elif letras_columna == "h":
                columna=7
            """Debemos asignarle el segundo valor o número a casilla"""
            fila_tablero: int = tamano_tablero - int(casilla[1])
            nombre_pieza: str = tablero_nombres[fila_tablero][columna]
            """Le decimos al código que según lo que encuentre en esa posición del tablero imprima "Esta casilla esta vacía" o 
             el nombre de la pieza que sacará de la segunda lista que le hemos dado con los nombres. """
            if nombre_pieza == ".":
                print("Esta casilla esta vacía")
            else: 
                print(f"Existe la pieza {nombre_pieza} en esta casilla")
            estado = "turno negras"
            """Este else completa el if del principio para que en el caso de que no escriba ni salir, ni una casilla dentro del tablero
            el código imprima el siguiente mensaje"""
            turno = turno + 1
        else:
             print("La posición que indicaste no es correcta")
     

        """Ahora hacemos exactamente lo mismo pero con la única diferencia que es el turno de las negras"""        
    elif estado == "turno negras":
        print("Turno negras")
        print(f"Turno {turno}")
        casilla: str = input("casilla que desea ir: ").strip().lower () 
        if casilla == "salir".strip().lower():
            estado = "salir"
        elif len(casilla) == 2 and (casilla[0]in letras_validas) and (casilla[1] in numeros_validos):
            letras_columna: str = casilla [0]
            columna: int = 0 
            if letras_columna == "a":
                columna=0
            elif letras_columna == "b":
                columna=1
            elif letras_columna == "c":
                columna=2
            elif letras_columna == "d":
                columna=3
            elif letras_columna == "e":
                columna=4
            elif letras_columna == "f":
                columna=5
            elif letras_columna == "g":
                columna=6
            elif letras_columna == "h":
                columna=7

            fila_tablero: int = tamano_tablero - int(casilla[1])
            nombre_pieza: str = tablero_nombres[fila_tablero][columna]
            if nombre_pieza == ".":
                print("Esta casilla esta vacía")
            else:
                print(f"Existe la pieza {nombre_pieza} en esta casilla")
            estado = "turno blancas"
            turno = turno + 1
        else:
             print("La posición que indicaste no es correcta")