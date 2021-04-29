import os
import copy
from copy import deepcopy
from tkinter.filedialog import askopenfilename

listaLineasArchivo=[]
listadeListasGramatica=[]
listaGramaticasT=[]
listaGramaticasTc=[]
listaGramaticasProducciones=[]
listaInfoGramaticas=[]
listaGramaticaAutoPila=[]
def menu():
    #-------------- Funcion que imprime las posibles opciones a acceder y retorna el valor ingresado -----------------------------------
    print("1. Carga de Archivo")
    print("2. Mostrar Información General de la Gramatica")
    print("3. Generar Automata de Pila")
    print("4. Reporte de Recorrido")
    print("5. Reporte en Tabla")
    print("6. Salir")
    opcion = input("Ingrese una opccion: \n")
    return opcion

def cargarArchivo(): 
    global listaGramaticasT
    archivo = askopenfilename()#Abre la interfaz para escoger el archivo a cargar
    print(archivo)#se obtiene el URL

    #Se abre el archivo
    archivoLectura = open('' + archivo + '', 'r')
    
    for linea in archivoLectura:
        lineaGramatica=linea.split()
        listaLineasArchivo.append(lineaGramatica)
    
        if lineaGramatica == ['*']:
            listaTemp = list(listaLineasArchivo)
            listadeListasGramatica.append(listaTemp)
            listaLineasArchivo.clear()

    indexPrueba = len(listadeListasGramatica)

    for x in range (indexPrueba):
        indexUltimo = len(listadeListasGramatica[x])
        listadeListasGramatica[x].pop(int(indexUltimo)-1)
    
    for j in range (indexPrueba):
        lTemp=[]
        lTempProd=[]
        indexRecorido = len(listadeListasGramatica[j])
        for y in range(indexRecorido):
            if(y==0):
                lTemp.append(listadeListasGramatica[j][y])
            elif(y==1):
                cadena=listadeListasGramatica[j][y]
                cadena2=str(cadena)
                Temporal=cadena2.split(";")
                lTemp.append(Temporal)
            else:
                lTempProd.append(listadeListasGramatica[j][y])
        lTemp.append(list(lTempProd))
        listaGramaticasT.append(list(lTemp))
        lTemp.clear()
        lTempProd.clear()
    #---------------------------  Impresion de Todas las Gramaticas bien Separadas -----------------------------------------------
    indexPrueba = len(listaGramaticasT)

    for obj in listaGramaticasT:
        print(obj)
    print("----------------- Lectura -------------------------")
    
def produccionesGramaticas():
    listaGramaticasTc= deepcopy(listaGramaticasT)
    indexPrincipal = len (listaGramaticasTc)
    bandera = False
    for x in range(indexPrincipal):
        indexInterno = len(listaGramaticasTc[x])
        for y in range(indexInterno):
            if(y==2):
                tempProducciones = list(listaGramaticasTc[x][y])
                producciones=[]
                indexProducciones = len(tempProducciones)
                for z in range(indexProducciones):
                    cadenaProduccion = str(listaGramaticasTc[x][y][z]).split("->")
                    cadenaProduccion2=(str(cadenaProduccion).split(","))
                    producciones.append(cadenaProduccion2)
                listaGramaticasTc[x][y]=list(producciones)
                producciones.clear()

    print ("------------------ Aqui vere como quedan Gramticas Normales --------------------")
    print("------------------------------------------------------------------------------------------")
    for obj in listaGramaticasT:
        print(obj)
    print("\n")
    print ("------------------ Aqui vere como quedan Gramticas Expandidas --------------------")
    print("------------------------------------------------------------------------------------------")
    for obj in listaGramaticasTc:
        print(obj)
    print("------------------- Eliminacion -----------------------------------------------")
    for x in range(indexPrincipal):
        indexInterno = len(listaGramaticasTc[x])
        print(indexInterno)
        for y in range(indexInterno):
            #print("prueba"+str(y))
            if(y==2):
                indexBusquedaInterna = len(listaGramaticasTc[x][y])
                print(indexBusquedaInterna)
                for z in range(indexBusquedaInterna):
                    print(str(listaGramaticasTc[x][y][z]))
                    print(int(len(listaGramaticasTc[x][y][z])))
                    if(int(len(listaGramaticasTc[x][y][z])>=4)):
                        bandera=True
                print(bandera)        
        if(bandera==False):
            del(listaGramaticasTc[x])
            del(listaGramaticasT[x])
        else:
            bandera=False
    print("------------------------------------------------------------------------------------------")
    for obj in listaGramaticasT:
        print(obj)
    print("\n")
    print ("------------------ Aqui vere como quedan Gramticas Expandidas --------------------")
    print("------------------------------------------------------------------------------------------")
    for obj in listaGramaticasTc:
        print(obj)
        print("\n")
    print("----------------- gramagicas originales ------------------------------------")
    for obj in listaGramaticasT:
        print(obj)
        print("\n")
    #66listaGramaticasProducciones=list(listaGramaticasTc)

def mostrarInfoGramaticas():
    indexExterno = len(listaGramaticasT)
    for x in range(indexExterno):
        indexMedio = len(listaGramaticasT[x])
        for y in range (indexMedio):
            if(y==0):
                CadenaMostrarGram = "Nombre Gramatica: "+str(listaGramaticasT[x][y])+" \n"
            elif(y==1):
                indexInterno1=len(listaGramaticasT[x][y])
                for z in range(indexInterno1):
                    if(z==0):
                        CadenaMostrarGram=CadenaMostrarGram+"   No Terminales: {"+str(listaGramaticasT[x][y][z])+"} \n"
                    elif(z==1):
                        CadenaMostrarGram=CadenaMostrarGram+"       Terminales: {"+str(listaGramaticasT[x][y][z])+"} \n"
                    elif(z==2):
                        CadenaMostrarGram=CadenaMostrarGram+"           No Terminal Inicial: {"+str(listaGramaticasT[x][y][z])+"} \n"
            elif(y==2):
                CadenaMostrarGram=CadenaMostrarGram+"                       Producciones:  \n"
                indexInterno2=len(listaGramaticasT[x][y])
                for z in range(indexInterno2):
                    CadenaMostrarGram=CadenaMostrarGram+"                         "+str(listaGramaticasT[x][y][z])+" \n"
    print(CadenaMostrarGram)

def generarAutomata():

    nombreAutomata="AP_"
    terminales=""
    alfabetoPila=""
    estados="Estados = {i,p,q,f}"
    estadoInicio="Estado Inicio = { i }"
    estadoFin="Estado Fin = { f }"
    listaProducciones=[]

    listaGramaticasTc2= deepcopy(listaGramaticasT)
    indexPrincipal = len (listaGramaticasTc2)
    for x in range(indexPrincipal):
        indexInterno = len(listaGramaticasTc2[x])
        for y in range(indexInterno):
            if(y==2):
                tempProducciones = list(listaGramaticasTc2[x][y])
                indexProducciones = len(tempProducciones)
                for z in range(indexProducciones):
                    cadenaProduccion = str(listaGramaticasTc2[x][y][z]).split("->")
                    cadenaProduccion2=(str(cadenaProduccion).split(","))
                    print(str(cadenaProduccion2[1]))
                    print(str(cadenaProduccion2[0].replace("[\"[\'","")))
                    indexProdAuto = len(cadenaProduccion2)
                    for w in range(indexProdAuto):
                        if(w==0):
                            #indexProdAuto2=len(cadenaProduccion2[w])
                            cadenaTemp1=str(cadenaProduccion2[w].replace("[\"[\'",""))
                            cadenaTemp2=cadenaTemp1.replace("\"","")
                            cadProdTempAuto="λ,"+cadenaTemp2+";"
                        elif(w==(indexProdAuto-1)):
                            cadenaTemp3=str(cadenaProduccion2[w].replace(" \"",""))
                            cadenaTemp4=cadenaTemp3.replace("\']\"]","")
                            cadenaTemp7=cadenaTemp4.replace("\']]","")
                            cadenaTemp9=cadenaTemp7.replace(" \'","")
                            cadProdTempAuto=cadProdTempAuto+cadenaTemp9
                        else:
                            cadenaTemp5=str(cadenaProduccion2[w].replace(" \"",""))
                            cadenaTemp6=cadenaTemp5.replace(" \'","")
                            cadenaTemp8=cadenaTemp6.replace("\'","")
                            cadProdTempAuto=cadProdTempAuto+cadenaTemp8
                    
                    #producciones.append(cadenaProduccion2)1

                    listaProducciones.append(cadProdTempAuto)
                    cadProdTempAuto=""
  
    indexExterno = len(listaGramaticasT)
    for x in range(indexExterno):
        indexMedio = len(listaGramaticasT[x])
        for y in range (indexMedio):
            if(y==0):
                nombreAutomata=nombreAutomata+str(listaGramaticasT[x][y])
            elif(y==1):
                indexInterno1=len(listaGramaticasT[x][y])
                for z in range(indexInterno1):
                    if(z==0):
                        noTerminales=str(listaGramaticasT[x][y][z])
                    elif(z==1):
                        terminales=terminales+"Terminales = {"+str(listaGramaticasT[x][y][z])+"} \n"
                        alfabetoPila=alfabetoPila+"Alfabeto de Pila = {"+str(listaGramaticasT[x][y][z])+","+noTerminales+", #"
        print(nombreAutomata)
        print(terminales)
        print(alfabetoPila)
        print(estados)
        print(estadoInicio)
        print(estadoFin)
        for obj in listaProducciones:
            print(obj)
        cadenaFinalProduccionAutomataPila=nombreAutomata+";"+terminales+";"+alfabetoPila+";"+estados+";"+estadoInicio+";"+estadoFin+";"+str(listaProducciones)
        listaGramaticaAutoPila.append(cadenaFinalProduccionAutomataPila)
        listaProducciones.clear()  
    
    for obj in listaGramaticaAutoPila:
        print(obj)


def pruebaImprimir():
    print(int(len(listaGramaticasProducciones)))
    for obj in listaGramaticasTc:
        print(obj)


def salir():
    #------------------- Funcion que es llamada antes de salir del programa imprime mis datos personales -------------------------------
    print("Carnet: 201313861")
    print("Nombre: Walther Andree Corado Paiz")
    print("Correo: waltercoradopaiz@gmail.com")
    print("Curso:  Lenguajes Formales y De Programación Seccion B")
    print("Adios")

ciclo=True
while(ciclo):

    numero = menu()
    if numero == "1":
        print("Opcion1")
        cargarArchivo()
        produccionesGramaticas()
        input("")
        
    elif numero == "2":
        print("Opcion2")
        mostrarInfoGramaticas()
        input("")
    elif numero == "3":
        print("")
        generarAutomata()
        input("")
    elif numero == "4":
        print("Opcion4")
        
        input("")
    elif numero == "5":
        print("Opcion5")
        
        input("")    
    elif numero == "6":
        salir()
        input("")
        ciclo=False
    else:
        print("Opcion no validada favor ingresar una opcion valida ")
        