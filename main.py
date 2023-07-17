import numpy as np
from tablas_fajas import Tabla_17_13, Tabla_17_12_C, Tabla_17_15, Tabla_17_10, Tabla17_14

# Función para calcular la longitud de la correa
def longitud(n_d, D, d):
    return n_d * np.pi * (D + d)

# Función para obtener la longitud de la faja más cercana a un valor dado
def longitud_de_faja(dato, tabla):
    long_faja = None
    
    if dato in tabla:  # Si el dato está presente en la tabla, se selecciona ese número
        long_faja = dato
    else:
        mayores = [num for num in tabla if num > dato] 
        if mayores:  # Si hay números mayores
            long_faja = min(mayores)  # Selecciona el número más cercano
    
    return long_faja

# Función para calcular la distancia entre los centros de los diámetros de la correa
def distancia_centros(Lp, D, d):
    C = 0.25 * ((Lp - (np.pi/2) * (D + d)) + np.sqrt(np.power(Lp - (np.pi/2) * (D + d), 2) - 2 * np.power(D - d, 2)))
    return C

# Función para verificar si el valor de la distancia entre centros está en el rango correcto
def ajustar_rango(C, D, d):
    if D < C and C < 3 * (D + d):
        print("El valor de C está en el rango correcto")
    else:
        print("El valor de C NO está en el rango correcto")

# Función para calcular la velocidad de la banda
def velocidad_banda(d, n):
    return (np.pi * d * n) / 12

# Función para obtener el factor K1 de la tabla Tabla_17_13
def factor_K1(valor):
    for i in range(len(Tabla_17_13)):
        if Tabla_17_13[i]["(D-d)\/C"] == valor:
            return Tabla_17_13[i]["K1_VV"]
        elif Tabla_17_13[i]["(D-d)\/C"] > valor:
            sup = i
            inf = i - 1
            break
    if sup is not None and inf is not None:
        k1 = interpolacion(Tabla_17_13[inf]["(D-d)\/C"], Tabla_17_13[inf]["K1_VV"], Tabla_17_13[sup]["(D-d)\/C"], Tabla_17_13[sup]["K1_VV"], valor)
        return k1
    else:
        k1 = None

# Función para obtener el factor k2 de la tabla Tabla17_14
def factor_k2(tabla17_14, longitud):
    for i in range(len(tabla17_14)):
        if tabla17_14[i]["L_min"] <= longitud <= tabla17_14[i]["L_max"]:
            return tabla17_14[i]["Factor"]

    # Si no se encuentra en ningún intervalo, realizar interpolación
    l_mins = [t["L_min"] for t in tabla17_14]
    l_maxs = [t["L_max"] for t in tabla17_14]

    # Encontrar los valores más cercanos de L_max y L_min
    l_max_anterior = max(filter(lambda x: x <= longitud, l_maxs))
    l_min_superior = min(filter(lambda x: x >= longitud, l_mins))

    # Encontrar los factores correspondientes
    factor_lmax_anterior = [t["Factor"] for t in tabla17_14 if t["L_max"] == l_max_anterior][0]
    factor_lmin_superior = [t["Factor"] for t in tabla17_14 if t["L_min"] == l_min_superior][0]

    # Realizar interpolación
    factor_interpolado = factor_lmax_anterior + (factor_lmin_superior - factor_lmax_anterior) * \
                         (longitud - l_max_anterior) / (l_min_superior - l_max_anterior)

    return factor_interpolado

# Función para obtener el valor de H_tab de la tabla Tabla_17_12_C
def H_TAB(V, d):
    # Si el valor de d es mayor a 12, se toma como 12
    if d > 12:
        d = 12

    if V > 5000:
        return None
    for i in range(5):
        velocidad = Tabla_17_12_C[i][0]

        if velocidad == V:
            for j in range(8):
                j += 1 
                if d == Tabla_17_12_C[i][j]["Diámetro"]:
                    H_tab = Tabla_17_12_C[i][j]["H_tab"]
                    return H_tab
            return None
        
        elif velocidad > V:
            sup = i
            inf = i - 1
            break
    
    if sup is not None and inf is not None:
        for k in range(7):
            k += 1
            if d == Tabla_17_12_C[inf][k]["Diámetro"]:
                h_inf = Tabla_17_12_C[inf][k]["H_tab"]

            if d == Tabla_17_12_C[sup][k]["Diámetro"]:
                h_sup = Tabla_17_12_C[sup][k]["H_tab"]
        if h_inf is not None and h_sup is not None:
            H_tab = interpolacion(Tabla_17_12_C[inf][0], h_inf, Tabla_17_12_C[sup][0], h_sup, V)
            return H_tab

    print("No se encontró el valor de V en la tabla.")
    return None

# Función para calcular H_a multiplicando H_tab, k1 y k2
def H_a(H_tab, k1, k2):
    return H_tab * k1 * k2

# Función para obtener el factor de servicio Ks según el tipo de máquina y par de torsión
def factor_servicio(tipo):
    while True:
        try:
            maquina = int(input("\nElija maquinaria impulsada:\n1. Uniforme.\n2. Impacto ligero.\n3. Impacto medio.\n4. Impacto pesado\nElección: "))
            if maquina != 1 and maquina != 2 and maquina != 3 and maquina != 4:
                print("Ingrese una opción válida")
            else: 
                break
        except (ValueError):
            print("Ingrese una opción válida")
        
    if tipo == 1:
        if maquina == 1:
            Ks = Tabla_17_15[0][0]["Ks"]
        elif maquina == 2:
            Ks = Tabla_17_15[0][1]["Ks"]
        elif maquina == 3:
            Ks = Tabla_17_15[0][2]["Ks"]
        elif maquina == 4:
            Ks = Tabla_17_15[0][3]["Ks"]
    elif tipo == 2:
        if maquina == 1:
            Ks = Tabla_17_15[1][0]["Ks"]
        elif maquina == 2:
            Ks = Tabla_17_15[1][1]["Ks"]
        elif maquina == 3:
            Ks = Tabla_17_15[1][2]["Ks"]
        elif maquina == 4:
            Ks = Tabla_17_15[1][3]["Ks"]
    return Ks

# Función para calcular la potencia de diseño multiplicando H_nom, Ks y n_d
def potencia_diseño(H_nom, Ks, n_d):
    H_d = H_nom * Ks * n_d
    return H_d

# Función para calcular la cantidad de bandas necesarias para H_d y H_a
def cantidad_bandas(H_d, H_a):
    num_bandas = H_d / H_a
    if num_bandas.is_integer():
        return int(num_bandas)
    else:
        return np.ceil(num_bandas)

# Función para realizar la interpolación lineal entre dos puntos (x1, y1) y (x2, y2) para un valor x dado
def interpolacion(x1, y1, x2, y2, x):
    y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return y

if __name__ == '__main__':
    print("""
###############################################################
####                  Ingreso de datos                     ####
###############################################################\n""")

    # Obtener los valores de entrada del usuario
    D = float(input("Diámetro D: "))
    d = float(input("Diámetro d: "))
    d = np.floor(d)
    n = float(input("RPM: "))
    n_d = float(input("Factor de diseño: "))
    
    while True:
        H_nom = float(input("Potencia nominal (15-100 HP): "))
        if H_nom > 100 or H_nom < 15:
            print("Potencia fuera de rango.")
        else:
            break
    
    # Calcular la longitud de la correa
    L = longitud(n_d, D, d)
    # Obtener la longitud de la faja más cercana
    long_faja = longitud_de_faja(L, Tabla_17_10)
    print("La longitud de faja es:", long_faja)

    # Calcular la longitud de paso Lp
    Lp = long_faja + 2.9
    print("La longitud de paso es: ", round(Lp, 3))

    # Calcular la distancia entre centros C
    C = distancia_centros(Lp, D, d)
    print(f'La distancia entre centros C es: {round(C, 3)}')

    # Calcular la velocidad de la banda V
    V = velocidad_banda(d, n)
    print(f'V: {round(V, 3)}')

    # Verificar si C está dentro del rango correcto
    ajustar_rango(C, D, d)

    # Calcular el factor K1
    k1 = factor_K1((D - d) / C)
    if k1 is not None:
        print(f'El valor del factor K1 es: {round(k1, 3)}')
    else: 
        print(f'No se encontró un valor para K1 dentro de la tabla, asegúrese de ingresar los datos correctamente.')

    # Obtener el valor de H_tab
    h_tab = H_TAB(V, d)
    print(f'H_Tab: {round(h_tab, 3)}')

    # Calcular el factor k2
    k2 = factor_k2(Tabla17_14, Lp)

    # Calcular H_a
    h_a = H_a(h_tab, k1, k2)
    print(f'H_a: {round(h_a, 3)}')

    print("""
###############################################################
####                  Tipo de máquina                      ####
###############################################################\n""")

    # Obtener el tipo de par de torsión y el factor de servicio Ks
    tipo = int(input("Tipo de par de torsión:\n1. Par de torsión normal.\n2. Par de torsión alto o no uniforme\nElección: "))
    ks = factor_servicio(tipo)

    # Calcular la potencia de diseño H_d
    h_d = potencia_diseño(H_nom, ks, n_d)
    print(f'Potencia de diseño H_d: {h_d} HP')

    # Calcular la cantidad de bandas necesarias
    N_b = cantidad_bandas(h_d, h_a)
    print(f'Se necesitan {N_b} bandas.')
