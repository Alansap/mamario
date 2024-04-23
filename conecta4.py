def printtablero(tablero):
    print("|", end="")
    for i in range(1,len(tablero[0])+1):
        print(str(i) + "|", end="")
    print("")
    for columna in tablero:
        print("|", end="")
        for columna in columna:
            print(columna + "|", end="")
        print("")
    #separador
    print("+", end="")
    for i in range(1,len(tablero[0])+1):
        print("-", end="+")
    print("")

def tablero(x,y):
    tablero = []
    for i in range(x):
        tablero.append([])
        for j in range(y):
            tablero[i].append(' ')
    return tablero
    
    ###Hay que hacer aqui la funcion check wi, que busque las putas lineas completas en la posicion y para el turno que se le da
    
def checkwin(tablero, fila, columna, turno)


def colocar_ficha(tablero, columna, turno):
    for i in range(len(tablero[0])-1, 0, -1):
        if tablero[i][columna-1]==' ':
            tablero[i][columna-1] = turno
            checkwin(tablero, i, columna,turno)
            break
empate = False
jug = 1;



j1 = 'O'
bot = 'X'
#tamaño del tablero
x=7
y=7

tablero = tablero(x,y)
print(tablero)
#print(tablero(x,y))

printtablero(tablero)

while (True):
    print("Va el jugador", jug)
    col = int (input())
    if(jug == 1):
        colocar_ficha(tablero, col, j1)
        jug = 2
    else:
        colocar_ficha(tablero, col, bot)
        jug = 1
    printtablero(tablero)


            
