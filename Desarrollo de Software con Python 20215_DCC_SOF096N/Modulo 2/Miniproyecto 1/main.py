NOMBRE_ARCHIVO = "ley-de-presupuestos-inicial-y-vigentenivel-partidaa--mayo-2021.csv"

## Partidas debe ser un conjunto con pares id_partida y nombre_partida, los pares son únicos. 
partidas = set()

## Datos partidas debe ser un diccionario indexado por el ID de cada partida, y que contenga los datos
## de todos los subtítulos de esa partida. Es decir, la key es id_partida y el value los subtítulos de esa partida.
datos_partidas = dict()

## Esta función carga los datos desde el archivo. Debe completarla las partes que se indican.
def cargar_datos(archivo, partidas, datos_partidas):

    ####### ESTA PARTE DE ABAJO NO SE MODIFICA ######
    with open(archivo, "r", encoding="utf-8") as lineas:
        next(lineas)
        for linea in lineas:
            data = linea.strip("\n").split(";")[0].split(",")
            id = data[0]
            año = data[1]
            mes = data[2]
            moneda = "USD" if data[3]=='DOLARES' else "CLP"
            id_partida = data[4]
            if len(data) == 11:
                nombre_partida = data[5][1:] + data[6][:-1]
                id_subtitulo = data[7]
                nombre_subtitulo = data[8]
                monto_original = float(data[9].replace(".",""))
                monto_a_marzo = float(data[10].replace(".",""))
            elif len(data) == 12:
                nombre_partida = data[5][1:] + data[6] + data[7][:-1]
                id_subtitulo = data[8]
                nombre_subtitulo = data[9]
                monto_original = float(data[10].replace(".",""))
                monto_a_marzo = float(data[11].replace(".",""))
            else:
                nombre_partida = data[5]
                id_subtitulo = data[6]
                nombre_subtitulo = data[7]
                monto_original = float(data[8].replace(".",""))
                monto_a_marzo = float(data[9].replace(".",""))
            ####### ESTA PARTE DE ARRIBA NO SE MODIFICA ######

            ## Por cada línea se entrega la siguiente información: 
            ## id, año, mes, moneda, id_partida, nombre_partida, id_subtitulo, nombre_subtitulo, monto_original y monto_a_marzo

            ## 1. Agregar datos a estructuras apropiadas.
            ##    Construir conjunto con nombres de partidas
            ##    Partidas debe ser un conjunto con pares id_partida y nombre_partida. 
            ## COMPLETAR AQUí

            partidas.add((int(id_partida), nombre_partida))

            ## 1. Agregar datos a estructuras apropiadas.
            ##    Construir diccionario con informacion de todas las ejecuciones de una partida
            ##    datos_partidas debe ser un diccionario indexado por el ID de cada partida, y que contenga los datos
            ##    de todos los subtítulos de esa partida.
            ## COMPLETAR AQUI

            datos_partidas.setdefault(int(id_partida), [])
            datos_partidas[int(id_partida)].append({'id_subtitulo': id_subtitulo, 'nombre_subtitulo': nombre_subtitulo, 'monto_original': monto_original, 'monto_a_marzo': monto_a_marzo, 'moneda': moneda})

    print("Datos leidos.")
    print("Cantidad de partidas distintas leidas:", len(partidas))
    print("")


## 2. Construir función que muestra el detalle de todos los subtítulos de una partida en particular.
##    Debe mostrar un menu con todas las partidas posibles y permitir al usuario elegir una.
##    Recibe como parámetros el conjunto de partidas existentes,
##    un diccionario con los datos de los subtítulos de cada partida y un parámetro de conversión de dólares a pesos.
##    
def montos_por_partida(partidas, datos_partidas, usd_a_clp):
    pass
    ## COMPLETAR AQUI
    op = -1
    while op != 0:
        for partida in partidas:
            print(str(partida[0]) + ": " + partida[1])
        print("0: Menú Principal")
        try:
            op = int(input("Opcion: "))
        
        except ValueError:
            print(f"Ingrese opción valida")
            op = -1
        
        if op != 0 and op in datos_partidas:
          print("Nombre Subtitulo | Monto Original | Monto Marzo 2020 | Diferencia")
          for v in datos_partidas[op]:
            if v['moneda'] == 'USD':
              v['monto_original'] = v['monto_original'] * usd_a_clp
              v['monto_a_marzo'] = v['monto_a_marzo'] * usd_a_clp
            diferencia = v['monto_original'] - v['monto_a_marzo']
            print(f"{v['nombre_subtitulo']} | {v['monto_original']} | {v['monto_a_marzo']} | {diferencia}")
          op = 0



## 3. Construir función que imprima datos de los montos totales originales de cada partida, ordenados de mayor a menor.
##    Recibe como parámetros el conjunto de partidas existentes,
##    un diccionario con los datos de los subtítulos de cada partida y un parámetro de conversión de dólares a pesos.
def partidas_por_monto_original(partidas, datos_partidas, usd_a_clp):
    pass
    ## COMPLETAR AQUI
    partida_monto_total = {}
    for dato_partida in datos_partidas.items():
      monto_total = 0
      id_partida = dato_partida[0]
      for subtitulo in dato_partida[1]:
        if subtitulo['moneda'] == 'USD':
          subtitulo['monto_original'] = subtitulo['monto_original'] * usd_a_clp
        monto_total += subtitulo['monto_original']
      partida_monto_total[id_partida] = monto_total
    partida_monto_total_desc = dict(sorted(partida_monto_total.items(), key = lambda x: x[1], reverse = True))
    for k, v in partida_monto_total_desc.items():
      print("Partida ID: " + str(k) + " Monto Total: " + str(v))





## 4. Agregar una función más que responda a una consulta definida por usted, usando los datos disponible en el archivo
##    Puede cambiar el nombre a la función, pero también deberá cambiarla en la opción 3 del menú.
def funcion_personalizada(partidas, datos_partidas, usd_a_clp):
    pass
    ## COMPLETAR AQUI
    ## Consulta similar a la primera pero el contenido se carga en un DataFrame de Pandas
    ## y permite guardar la información como Excel o mostrar en pantalla
    import pandas as pd
    rows = []
    op = -1
    while op != 0:
        for partida in partidas:
            print(str(partida[0]) + ": " + partida[1])
        print("0: Volver al Menú Principal")
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida")
            op = -1

        if op != 0 and op in datos_partidas:
          for v in datos_partidas[op]:
            if v['moneda'] == 'USD':
              v['monto_original'] = v['monto_original'] * usd_a_clp
              v['monto_a_marzo'] = v['monto_a_marzo'] * usd_a_clp
            diferencia = v['monto_original'] - v['monto_a_marzo']
            rows.append([v['nombre_subtitulo'], v['monto_original'], v['monto_a_marzo'], diferencia])
          op = 0
        df = pd.DataFrame(rows)
        df.columns = ["Nombre Subtitulo","Monto Original","Monto Marzo 2020","Diferencia"]
        opg = -1
        while opg != 0:
          print("1: Mostrar Pandas DataFrame")
          print("2: Guardar Pandas DataFrame como Excel")
          print("0: Volver al Menú Principal")
          try:
            opg = int(input("Opción: "))
          except ValueError:
            print("Ingrese opción válida")
            opg = -1
          if opg != 0:
            if opg == 1:
              print(df)
            elif opg == 2:
              df.to_excel("subtitulo.xlsx")
              print("Archivo Guardado")

############################################################################
## No necesita modificar este código ##
if __name__ == "__main__":

    cargar_datos(NOMBRE_ARCHIVO, partidas, datos_partidas)

    dict_opciones = {1: ("Montos de una partida", montos_por_partida),
                     2: ("Partidas ordenadas de mayor a menor, por monto original", partidas_por_monto_original),
                     3: ("Función personalizada", funcion_personalizada), ## puede cambiar este nombre en la parte 4.
                     0: ("Salir", None)
                    }


    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opcion: "))
        
        except ValueError:
            print(f"Ingrese opción valida")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            dict_opciones[op][1](partidas, datos_partidas, 800)
