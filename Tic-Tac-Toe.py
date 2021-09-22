#Implementacion de juego Tic-Tac-Toe en Python.
'''El tablero se arma usando una matriz, donde las claves serán 
la ubicación (por ejemplo: arriba a la izquierda, a la mitad a la derecha, etc.)
y sus valores iniciales serán espacios vacíos y después de cada movimiento 
cambiaremos el valor de acuerdo a la elección del jugador.'''

tablero = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in tablero:
    board_keys.append(key)
'''Se imprimira el tablero actualizado después de cada movimiento del juego y 
    por lo que se crea una función en la que se define la función printBoard
    para poder imprimir fácilmente el tablero cada vez que llamemos a esta función.'''

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# Funcion principal del juego.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(tablero)
        print("jugador uno con tiro, " + turn + ". Elije una casilla")

        move = input()        
        #Se verifica si la casilla esta disponible o no
        if tablero[move] == ' ':
            tablero[move] = turn
            count += 1
        else:
            print("Casilla ocupada.\nElije otra casilla")
            continue

# se declara ganador al jugador X o O, si cumple alguna de las sigientes condiciones despues de 5 movimientos. 
        if count >= 5:
            if tablero['7'] == tablero['8'] == tablero['9'] != ' ': # Cruce de linea inferior
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")                
                break
            elif tablero['4'] == tablero['5'] == tablero['6'] != ' ': # Cruce de lineas medio
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break
            elif tablero['1'] == tablero['2'] == tablero['3'] != ' ': # Cruce de lineas superior
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break
            elif tablero['1'] == tablero['4'] == tablero['7'] != ' ': # Linea vertical izquierda
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break
            elif tablero['2'] == tablero['5'] == tablero['8'] != ' ': # Linea vertical central
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break
            elif tablero['3'] == tablero['6'] == tablero['9'] != ' ': # Linea vertical derecha
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break 
            elif tablero['7'] == tablero['5'] == tablero['3'] != ' ': # diagonal
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break
            elif tablero['1'] == tablero['5'] == tablero['9'] != ' ': # diagonal
                printBoard(tablero)
                print("\nGame Over.\n")                
                print(" **** " +turn + " es ganador. ****")
                break 

        # declaración de empate.
        if count == 9:
            print("\nGame Over.\n")                
            print("Empate!!")

        # Cambio de jugador con cada movimiento.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Se pregunta a jugadores si quieren repetir la partida.
    restart = input("¿quieres iniciar una nueva partida?(s/n)  ")
    if restart == "s" or restart == "S":  
        for key in board_keys:
            tablero[key] = " "

        game()

if __name__ == "__main__":
    game()