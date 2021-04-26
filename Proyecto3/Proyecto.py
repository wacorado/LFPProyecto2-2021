import os
import copy
from copy import deepcopy
from tkinter.filedialog import askopenfilename

listaLineasArchivo=[]
listadeListasGramatica=[]
listaGramaticasT=[]
listaGramaticasTc=[]
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
        
        input("")
    elif numero == "3":
        print("Opcion3")
        
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
        