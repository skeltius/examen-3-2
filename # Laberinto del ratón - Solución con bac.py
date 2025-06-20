laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

def imprimir_laberinto(visitados=None):
    print("Laberinto:")
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if visitados and (i, j) in visitados:
                print(f"{celda}", end=" ")  
            elif celda == 0:
                print("0", end=" ")  
            elif celda == 'I':
                print("I", end=" ")  
            elif celda == 'F':
                print("F", end=" ")  
            elif celda in (3, 4):
                print(f"{celda}", end=" ")  
            else:
                print(celda, end=" ")
        print()

def resolver():
    inicio = next((i, j) for i, fila in enumerate(laberinto) 
                 for j, celda in enumerate(fila) if celda == 'I')
    
    mejor_ruta = []
    max_puntos = 0
    
    def backtrack(x, y, puntos, visitados, ruta_actual):
        nonlocal mejor_ruta, max_puntos
        
        if laberinto[x][y] == 'F':
            if puntos >= 23 and puntos > max_puntos:
                max_puntos = puntos
                mejor_ruta = ruta_actual.copy()
            return
        
        visitados.add((x, y))
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and laberinto[nx][ny] != 0 and (nx, ny) not in visitados:
                valor = laberinto[nx][ny]
                suma_puntos = 1 if valor in ['I', 'F', 1] else valor
                
                ruta_actual.append((nx, ny))
                backtrack(nx, ny, puntos + suma_puntos, visitados, ruta_actual)
                ruta_actual.pop()
        
        visitados.remove((x, y))
    
    backtrack(inicio[0], inicio[1], 0, set(), [inicio])
    
    if mejor_ruta:
        mejor_ruta.insert(0, inicio)
        print(f"¡Solución encontrada con {max_puntos} puntos!")
        print("Ruta seguida (coordenadas [fila, columna]):")
        for i, (x, y) in enumerate(mejor_ruta):
            print(f"Paso {i+1}: [{x}, {y}] -> {laberinto[x][y]}")
        return mejor_ruta
    else:
        print("No se encontró un camino con 23 puntos o más")
        return None

if __name__ == "__main__":
    print("=== LABERINTO DEL RATÓN ===")
    imprimir_laberinto()
    solucion = resolver()
    
    if solucion:
        print("Laberinto con la solución marcada:")
        imprimir_laberinto(set(solucion))
    else:
        print("No se encontró solución válida")
