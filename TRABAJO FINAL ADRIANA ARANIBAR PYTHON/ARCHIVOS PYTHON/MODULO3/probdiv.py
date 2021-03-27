#1
def datosAlumnos():
	listado = []
	n = int(input("Cantidad de alumnos:"))
	for i in range(n):
		nom = input("Nombre: ")
		alumno = [nom]
		for j in range(3):
			nota = int(input("Ingrese nota "+str(j+1)+": "))
			while nota < 0 or nota > 10:
				print("Nota invalida.")
				nota = int(input("Ingrese nota "+str(j+1)+": "))
			alumno.append(nota)
		listado.append(alumno)
	return listado
#2
def aproDesap(listado):
	aprob = 0
	desap = 0
	for alumno in listado:
		prom = sum(alumno[1:])/3
		if prom >= 4:
			aprob += 1
		else:
			desap += 1
	print("Aprobados",aprob)
	print("Desaprobados",desap)
#3
def promTotal(listado):
	promT = 0
	for alumno in listado:
		prom = sum(alumno[1:])/3
		promT += prom
	promT = promT/len(listado)
	print("Promedio total del curso:", promT)
#4
def promedios(listado):
	alumnoMayor = ""
	alumnoMenor = ""
	mayorProm = 0
	menorProm = 10
	for alumno in listado:
		prom = sum(alumno[1:])/3
		if prom < menorProm:
			alumnoMenor = alumno[0]
			menorProm = prom
		if prom >= mayorProm:
			alumnoMayor = alumno[0]
			mayorProm = prom
	print("Mayor promedio: ", alumnoMayor)
	print("Menor promedio: ", alumnoMenor)
#5
def buscarAlumno(alumno, listado):
	alumnos = []
	for datos in listado:
		if alumno in datos[0]:
			datos.append(sum(datos[1:])/3)
			alumnos.append(datos)
	return alumnos

listado = datosAlumnos()
aproDesap(listado)
promTotal(listado)
promedios(listado)
print(buscarAlumno('Jose', listado))