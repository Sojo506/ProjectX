def lineaSup(largo):
   linea = "   ╔"
   for i in range(1, largo-1):
      linea += "═"
   linea += "╗"
   print(linea)


def lineaMed(largo):
   linea = "   ╠"
   for i in range(1, largo-1):
      linea += "═"
   linea += "╣"
   print(linea)


def lineaInf(largo):
   linea = "   ╚"
   for i in range(1, largo-1):
      linea += "═"
   linea += "╝" + "\n"
   print(linea)


def lineaBlanco(largo):
   linea = "   ║"
   for i in range(1, largo-1):
      linea += " "
   linea += "║"
   print(linea)


def lineaDato(d, largo):
   linea = ""
   linea += "   ║ "
   linea += d
   blancos = largo - len(d)
   for i in range(1, blancos-2):
      linea += " "
   linea += "║"
   print(linea)


def menuPrincipal():
   lineaSup(60)
   lineaBlanco(60)
   lineaDato("                      Estadística", 60)
   lineaBlanco(60)
   lineaMed(60)
   lineaBlanco(60)
   lineaDato("01. Ingresar datos", 60)
   lineaDato("02. Obtener resultados", 60)
   lineaDato("03. Salir", 60)
   lineaBlanco(60)
   lineaInf(60)

while True:
   menuPrincipal()
   while True:
      try:
         opc = int(input("\nFavor ingresar su opción: "))
         break
      except ValueError:
         print("Valor incorrecto!")
   print()
   if opc == 1:
      datos = []
      while True:
         try:
            cant = int(input("Cantidad de datos a ingresar -> "))
            break
         except ValueError:
            print("Valor incorrecto!")
      for i in range(cant):
         while True:
            try:
               dato = float(input("--> "))
               datos.append(dato)
               break
            except ValueError:
               print("Valor incorrecto!")
   elif opc == 2:
      promedio = sum(datos) / cant
      minimo = min(datos)
      maximo = max(datos)
      print("\t\t .:RESULTADOS OBTENIDOS:.")
      print(f"Promedio: {promedio}\nMínimo: {minimo}\nMáximo: {maximo}")
      print()
   elif opc == 3:
      print("\t\t .:Gracias por utilizar el programa!:.") 
      break  