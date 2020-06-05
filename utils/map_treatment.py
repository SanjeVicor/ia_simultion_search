 
def get_matrix(data_list):
    matrix = list()
    for idx,e in enumerate(data_list):
        row = e.split(",")
        for i in range(len(row)): 
            row[i] = row[i].replace(" ","")
            if not row[i].isdigit():
                return False, f"Error, se encontro un caracter no permitido: {row[i]}, checa la linea {idx + 1}, en la columna {i+1}"
            try:
                row[i] = int(row[i])
                if row[i] < 0:
                    return False, "Error, número negativo encontrado"
            except:
                return False, "Error desconocido" 
        matrix.append(row)

    return matrix, None

def is_matrix_ok(matrix):
    length = len(matrix[0])
    for index, row in enumerate(matrix):
        if len(row) != length:
            return False, f"Error en fila(linea) {index + 1} -> tamaño requerido {length}, obtenido {len(row)}"
    return True, None

def read_file(path): 
    data = [line.rstrip('\n') for line in open(path)]
   
    if len(data) == 0:
        return None, "Archivo Vacio"
    matrix, exception = get_matrix(data)
    if not matrix :
        return None , exception

    if len(matrix) > 15:
        return None, f"Demasiadas filas max 15, número obtenido {len(matrix)}"

    if len(matrix[0]) > 15:
        return None, f"Demasiadas columnas max 15, número obtenido {len(matrix[0])}"

    ok , exception = is_matrix_ok(matrix)
    if ok:
        #print(matrix)
        return matrix, None
    else:
        return None , exception