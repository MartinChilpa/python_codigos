import re
import math

def ingreso_grafica():
  ecua_1=(input("Ingresa tu ecuación a graficar:"))
  #print(ecua_1)
  #Se le agrega un espacio al inicio y al final para poder leer correctamente dichos valores
    #Se reasigna a una variable
  ecuacion=(" "+ecua_1+" ")

  return ecuacion

ecua=ingreso_grafica()

#Pedir intervalo y paso
print("Ingresa tu intervalo (a,b)")
  #Inicio
a=int(input("a: "))
  #Fin
    #Se le suma 1 ya que range toma el segundo argumento -1
b=int(input("b: "))
  #Paso

paso=float(input("Ingresa el paso: "))

#Crear el vector de X
x=[]
  #Contador
i=a
while a<=b:
  #print(i)
  x.append(a)
  a+=paso
  a=round(a,4)
#print(x)



#Lectura de Coeficientes

  #Pontencias 
    #Una lista de tuplas de cinco elementos
      #1.- Espacio o signo
      #2.- Coeficiente 
      #3.- Variable dependiente 
      #4.- Signo de potencia
      #5.- Valor de la potencia
potencias=re.findall("(\s|\+|\-)([\d]+)([a-z])(\^)([\d]+)",ecua)
print("Potencias:",potencias)

  #Potencias con signo en la potencia
potencias_consigno=re.findall("(\s|\+|\-)([\d]+)([a-z])(\^)(\+|\-|)(.[\d]+)",ecua)
print(potencias_consigno)

  #Potencia sin coeficiente(x^n)
potencias_sin_coeficinete=re.findall("(\s|\+|\-)([\w])(\^)([\w]+)",ecua)
print("Potencias sin coeficiente:",potencias_sin_coeficinete)

  #Potencia sin coeficiente pero con signo
pote_sincoef_consigno=re.findall("(\+|\-|\s)([a-z])([\^])([\+\-][.\d]+)",ecua)
print(pote_sincoef_consigno)





  #Lineales
    #Una lista de tuplas de cuatro elementos
      #1-.Espacio o signo
      #2.-Coeficiente
      #3.-Variable independiente
      #4.-Delimitador, debe ser espacio o signo
lineales=re.findall("(\s|\+|\-|^[0-9])(\d+)([a-z])([^\^])",ecua)
#print("lineales:",lineales)

  #Lineal sin coeficiente(x)
lineales_sin_coeficinete=re.findall("(\s|\+|\-)([a-z])([^\^])",ecua)
#print("lineales sin coeficiente:",lineales_sin_coeficinete)


  #Independientes
    #Lista de tuplas con tres elementos
      #1.-Espacio o signo
      #2.- Valor de la variable independiente
      #3.- Espacio o signo
     
independientes=re.findall("(?<!\^)[\-\+\s][\d]+(?!\w+)",ecua)
#print("Independ:",independientes)
print("\n\n")


##Agregado de Potencias con signo antes de vaciar

for i in range(0, len(potencias_consigno)):
  sub_pote=[]
  for j in range(0,4):
    if potencias_consigno[i][4] == "-":
      num_1=float(potencias_consigno[i][5])*-1
    else:
      num_1=float(potencias_consigno[i][5])
    sub_pote.append(potencias_consigno[i][j])
  sub_pote.append(num_1)
  potencias.append(sub_pote)
print("Potencias_consigno",potencias)

##Agregado de Potencias sin coeficiente con signo antes de vaciar

sub_pote_sincoe_consig=[]

for i in range(0, len(pote_sincoef_consigno)):
  sub_pote_sincoe_consig=[]
  for j in range(0,3):
    num_1=float(pote_sincoef_consigno[i][3])
    sub_pote_sincoe_consig.append(pote_sincoef_consigno[i][j])
  sub_pote_sincoe_consig.append(num_1)
  potencias_sin_coeficinete.append(sub_pote_sincoe_consig)##Cambiar por potencias_sin_coeficiente
print("Potencia_sin_coe",potencias_sin_coeficinete)##Cambiar por potencias_sin_coeficiente

###########

#Determinar longitud de las listas
long_potencias=len(potencias)
long_potencias_sin=len(potencias_sin_coeficinete)

long_lineal=len(lineales)
long_lineal_sin=len(lineales_sin_coeficinete)

long_independientes=len(independientes)



#Calculo del valor arrogado por las potencias

#Se declara lista vacia
potencia_grados=[]

      ###vALOR DE POTENCIAS ###

#Se obtiene el grado al que esta elevado
for i in range(0,long_potencias):
  potencia_grados.append(float(potencias[i][4]))
#print("Lista de potencias",potencia_grados)

#Se obtiene el grado al que esta elevado sino tiene coeficiente
if long_potencias_sin != 0:
  for i in range(0,long_potencias_sin):
    #print("Sin coeficiente:",potencias_sin_coeficinete[i][3])
    potencia_grados.append(float(potencias_sin_coeficinete[i][3]))
    print("Lista final de potencias",potencia_grados)



#Se declara lista vacia
potencia_coeficientes=[]

    ###VALOR DE COEFICIENTES DE LAS POTENCIAS###  

for i in range(0,long_potencias):
  if potencias[i][0]== "-":
    negativo=int((potencias[i][1]))*(-1)
    potencia_coeficientes.append(negativo)
  else:
    potencia_coeficientes.append(int(potencias[i][1]))
#print("Lista final de coeficiente de potencias:",potencia_coeficientes)

if long_potencias_sin !=0:
    for i in range(0,long_potencias_sin):
      if potencias_sin_coeficinete[i][0] == "-":
        potencia_coeficientes.append(int(-1))
        #negativo=int((potencias_sin_coeficinete[i][1]))*(-1)
        #potencia_coeficientes.append(negativo)
      else:
        potencia_coeficientes.append(int(1))
print("Lista final de coeficientes",potencia_coeficientes)


      ###################COEFICIENTES LINEALES########################################
lineales_coeficientes=[]

for i in range(0,long_lineal):
  if lineales[i][0]=="-":
    negativo=int((lineales[i][1]))*-1
    lineales_coeficientes.append(negativo)
  else:
    lineales_coeficientes.append(int(lineales[i][1]))
#print("Lista de coeficienres lieneales",lineales_coeficientes)


for i in range(0,long_lineal_sin):
  if lineales_sin_coeficinete[i][0]=="-":
    lineales_coeficientes.append(int(-1))
  else:
    lineales_coeficientes.append(int(1))
print("Lista de coeficienres lieneales",lineales_coeficientes)

      ###################INDEPENDIENTES########################################
termino_independiente=[]

for i in range(0,long_independientes):
  termino_independiente.append(float(independientes[i]))
print("Independientes",termino_independiente)



############# Obtencion de los valores elevedos

x_elevadas=[]
for j in range(0,len(potencia_grados)):
  contenedor=[]
  for i in range(0,len(x)):
    print("x",x[i],"Grado",potencia_grados[j])
    res=math.pow( x[i], potencia_grados[j] )
    print(res)
    contenedor.append(res)
  x_elevadas.append(contenedor)
  #print(contenedor)
#print("X_elevadas",x_elevadas)

############# MUltiplicar por el coeficiente
x_elevadas_final=[]

for i in range(0,len(x_elevadas)):
  for j in range(0,len(x)):
    x_elevadas[i][j]=x_elevadas[i][j]*potencia_coeficientes[i]

x_elevadas_final=x_elevadas
#print(x_elevadas_final)
############ Sumar las potencias

x_potencias=[]

for i in range(0,len(x)):
  k=0
  for j in range(0,len(x_elevadas_final)):
    #print(x_elevadas_final[j][i])
    k+=(x_elevadas_final[j][i])
    #print("k",k)
  x_potencias.append(k)
#print("POTENCIAS",x_potencias)

########### SUstitucion en los lineales

x_lineales=[]

for i in range(0,len(x)):
  valor=0
  valor2=0
  for j in range(0,len(lineales_coeficientes)):
    valor=lineales_coeficientes[j]*x[i]
    valor2+=valor
  x_lineales.append(valor2)


##Suma del valor de potencia con el valor lienal

x_sin_indepen=[]
valor=0

for i in range (0, len(x_lineales)):
  valor+=(x_lineales[i])
  valor+=(x_potencias[i])
  x_sin_indepen.append(valor)
  valor=0


###########Suma del terminos independientes

indepen_final=0

for i in range(0,len(termino_independiente)):
  indepen_final+=termino_independiente[i]
#print("TOTAL DE TERMINO INDEPE",indepen_final)

#############Suma del termino independiente para obtener Y

y=[]

for i in range(0,len(x_sin_indepen)):
  valor=(x_sin_indepen[i])+(indepen_final)
  valor=round(valor,4)
  y.append(valor)
print("\nLista de x:",x)
print("Lista de y:",y)


########################### GRAFICADORA ###################################


#Se obtiene longitud de la tabulacion
long_x=len(x)
graficadora_final_master=[]

#Maximo y minimo de variable dependiente
y_max=int(max(y))
y_min=int(min(y))

y_grafica=[]

while y_min<=y_max:
  y_grafica.append(y_max)
  y_max-=(paso)

y_unico = []
 
for i in y:
	if i not in y_unico:
		y_unico.append(i)
  
long_y_grafica=len(y_grafica)
  


###
y_unico.sort()
y_unico.reverse()

grid=[]

long_unico=len(y_unico)


for i in range(0,long_unico):
  sub_grid=[]
  for j in range(0,long_x):
    if y_unico[i]==y[j]:
      sub_grid.append(j)
    #print("Y_uni",y_unico[i])
    #print("Y",y[j])
  #print("Sub:",sub_grid)
  grid.append(sub_grid)

#print("GRID",grid)

#print(grid)
long_grid= len(grid)
var_asterisco=0

#grid_y_graficadora=[]
#subgrid_y_graficadora=[]
cont=0

for m in y_grafica:
  
  graficadora=[]
  for k in range(0,long_x):
    graficadora.append(" ")
  
  #print(m)
  if m not in y:
    #print(m)
    print(" ")
    graficadora_final_master.append(" ")
    
  else: 
    #print("Asigancion de asterisco")
    #print(grid[cont])
    

    long_subgrid=len(grid[cont])

    for i in range(0,long_subgrid):

      #print(grid[cont][i])
      var_asterisco=grid[cont][i]
      #print("Graficadora",graficadora)
      graficadora.insert(var_asterisco, "*")
    graficadora_final="".join(graficadora)
    print(graficadora_final)
    graficadora_final_master.append(graficadora_final)
    cont+=1

print("\n")
print("Y:",y)
print("X:",x)
#print(y_grafica)