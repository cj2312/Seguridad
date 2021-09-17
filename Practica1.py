archivo = open('h.txt','r')
archivoEscritura = open('HERALDOSNEGROS_pre.txt','w')
a=''
for linea in archivo:
	for i in linea:

		#1. Realizar las siguientes sustituciones: j x i, h x i, ñ x n, k x l, u x v, w x v, y x z

		if i.isalpha():#4. Elimine los espacios en blanco y los signos de puntuación Guarde el resultado en el archivo “HERALDOSNEGROS_pre.txt”
			#solo lee caracteres alpha, elimina los espacios y signos puntuación
			if i=='j' or i=='J' or i=='h' or i=='H':
				a=a+'i';
				pass
			elif i=='ñ' or i=='Ñ':
				a=a+'n'
				pass
			elif i=='k' or i== 'K':
				a=a+'l'
				pass
			elif i=='u' or i=='U' or i=='W' or i=='w':
				a=a+'v'
				pass
			elif i=='y' or i=='Y':
				a=a+'z'
				pass

			#2. Elimine las tildes

			elif i=='á' or i=='Á':
				a=a+'a'
				pass
			elif i=='é' or i=='É':
				a=a+'e'
				pass
			elif i=='í' or i=='Í':
				a=a+'i'
				pass
			elif i=='ó' or i=='Ó':
				a=a+'o'
				pass
			elif i=='ú' or i=='Ú':
				a=a+'u'
				pass
			else:
				a=a+i

	#3. Convierta todas las letras a mayúsculas

	aMay=a.upper()

	archivoEscritura.write(aMay)
	a=''

archivoEscritura.close()
archivo.close()

#5. Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para
#cada letra de la ’A’ a ’Z’. La función deberá definirse como frecuencias(archivo) deberá devolver un
#diccionario cuyos índices son las letras analizadas y cuyos valores son las frecuencias de las mismas
#en el texto (número de veces que aparecen). Reconozca en el resultado obtenido los cinco caracteres
#de mayor frecuencia

leer = open('HERALDOSNEGROS_pre.txt','r')
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = [0]
lista *=26
for linea in leer:
	for i in linea:
		pos = alfabeto.index(i)
		lista[pos]+=1
		pass
	pass
it=0;
for x in lista:
	print(alfabeto[it]+' -> '+str(x))
	it+=1
	pass
tabla = [alfabeto,lista]
print(tabla)


#6. Aplicar el método Kasiski, que recorre el texto preprocesado y halla los trigramas en el mismo
#(sucesión de tres letras seguidas que se repiten) y las distancias (número de caracteres entre ellos)
#entre los trigramas

archivo = open('HERALDOSNEGROS_pre.txt','r')
a=[]

aux=1
temp=''
for linea in archivo: #aaasdfbbbiuccc
	for i in linea:
		if aux==1:
			temp=i
			aux+=1

			continue
		if temp== i:
			aux+=1
			temp=i

		if temp!=i:
			temp=i
			aux=1
		if aux==3:
			a.append(i*3)
			temp=''
			aux=1

print(a)



#archivoEscritura.close()
archivo.close()

#9. Volver a preprocesar el archivo insertando la cadena AQUÍ cada 20 caracteres, el texto resultante
#deberá contener un número de caracteres que sea múltiplo de 4, si es necesario rellenar al final con
#caracteres X según se necesite
archivoo = open('HERALDOSNEGROS_pre.txt','r')
archivoEscriturao = open('HERALDOSNEGROS.txt','w')
a=''
cont=0
temp=0
for linea in archivoo:
	for i in linea:
		if temp == 20:
			a=a+'AQUI'
			temp=0
			cont+=4
			
		else:
			a=a+i
			temp+=1
		cont+=1
if cont%4:
	archivoEscriturao.write(a)
else:
	archivoEscriturao.write(a+((cont%4)*'X'))

archivoEscriturao.close()
archivoo.close()

