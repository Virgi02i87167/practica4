cantidad = int(input("Cuantos estudiantes desea ingresar: "))
resultados = {}

for i in range(0, cantidad):
    print("\n")
    print("Ingresando datos del estudiante")
    nombre = input("Ingrese el nombre del estudiante numero {0}°: ".format(i+1))
    notas = []
    
    for j in range(0,3):
        nota = float(input("Ingrese la nota {0}: ".format(j+1)))
        notas.append(nota)

    resultados.setdefault(nombre, notas)

for clave, valor in resultados.items():
    print("-"*60)
    fila = clave.ljust(10)
    for nota in valor:
        fila += "| "+str(nota).ljust(10)

    fila += "| "+str(round((sum(valor) / len(valor)),2)).format().ljust(10)
    print(fila)