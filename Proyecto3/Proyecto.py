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
listaNombresGramaticasAP=[]
listaTerminalesGramaticasAP=[]
listaAlfabetoGramaticasAP=[]
listaProduccionesGramaticasAp=[]
listaProduccionesAPila=[]
contadorGraficas=0
listaIndiceGraficas=[]
nombreAutomata="AP_"
terminales=""
alfabetoPila=""
estados="Estados = i,p,q,f"
estadoInicio="Estado Inicio = { i }"
estadoFin="Estado Fin = { f }"
produccionCadTemp=""
listaProducciones=[]
listaCadenaIngresada=[]
pilaAutomata=[]
listaEstadoPila=[]
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
    global nombreAutomata, terminales, alfabetoPila, estados, estadoInicio, estadoFin, produccionCadTemp, listaProducciones
    
    #--------------------------------------- Obtener Producciones de la Gramatica indicadas -------------------------------------------
    listaGramaticasTc2= deepcopy(listaGramaticasT)
    #indexPrincipal = len (listaGramaticasTc2)
    
    
    for obj in listaProducciones:
        print(obj)
    
    indexExterno = len(listaGramaticasT)
    for x in range(indexExterno):
        indexMedio = len(listaGramaticasT[x])
        for y in range (indexMedio):
            if(y==0):
                nomTemp1=str(listaGramaticasT[x][y]).replace("['","")
                nomTemp2=nomTemp1.replace("']","")
                nombreAutomata=nombreAutomata+nomTemp2 #-------------- Aqui Obtengo el nombre del Automata -----------------------
            elif(y==1):
                indexInterno1=len(listaGramaticasT[x][y])
                for z in range(indexInterno1):
                    if(z==0):
                        noTerminales=str(listaGramaticasT[x][y][z]).replace("['","")
                    elif(z==1):
                        terminales=terminales+""+str(listaGramaticasT[x][y][z])
                        alfabetoPila=alfabetoPila+""+str(listaGramaticasT[x][y][z])+","+noTerminales+", #"
                        listaTerminalesTemp=[]
                        terminalTemp=str(listaGramaticasT[x][y][z]).split(",")
                        listaTerminalesTemp.append(terminalTemp)
                        indexProduccionesSiguientes=len(listaTerminalesTemp)
                        for r in range(indexProduccionesSiguientes):
                            indexProduccionesSiguientes2=len(listaTerminalesTemp[r])
                            for g in range(indexProduccionesSiguientes2):
                                produccionNueva=str(listaTerminalesTemp[r][g])+","+str(listaTerminalesTemp[r][g])+",λ"
                                listaProducciones.append(produccionNueva)
        indexInterno = len(listaGramaticasTc2[x])
        for y in range(indexInterno):
            if(y==2):
                tempProducciones = list(listaGramaticasTc2[x][y])
                indexProducciones = len(tempProducciones)
                for z in range(indexProducciones):
                    cadenaProduccion = str(listaGramaticasTc2[x][y][z]).split("->")
                    cadenaProduccion2=(str(cadenaProduccion).split(","))
                    indexProdAuto = len(cadenaProduccion2)
                    for w in range(indexProdAuto):
                        if(w==0):
                            cadenaTemp1=str(cadenaProduccion2[w].replace("[\"[\'",""))
                            cadenaTemp2=cadenaTemp1.replace("\"","")
                            cadProdTempAuto="λ,"+cadenaTemp2+","
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
                    listaProducciones.append(cadProdTempAuto)
                    cadProdTempAuto=""
    print(nombreAutomata)
    listaNombresGramaticasAP.append(nombreAutomata)
    print(terminales)
    listaTerminalesGramaticasAP.append(terminales)
    print(alfabetoPila)
    listaAlfabetoGramaticasAP.append(terminales)
    print(estados)
    print(estadoInicio)
    print(estadoFin)
    for obj in listaProducciones:
        print(obj)
    listaProduccionesGramaticasAp.append(list(listaProducciones))
    listaProducciones.clear()
    #------------------------------- Datos para Grafo y HTML -----------------------------------------------------
    indexlistas=len(listaProduccionesGramaticasAp)
    for x in range(indexlistas):
        indexProducciones1 = len(listaProduccionesGramaticasAp[x])
        for y in range(indexProducciones1):
            print(listaProduccionesGramaticasAp[x][y])
            produccionCadTemp=produccionCadTemp+str(listaProduccionesGramaticasAp[x][y])+"\n"
        listaProduccionesAPila.append(produccionCadTemp)
        produccionCadTemp=""
        #-------------------- Creacion de Grafos ---------------------------------
        global contadorGraficas
        file = open("grafo"+str(contadorGraficas)+".dot","w")
        file.write("digraph G{\n")
        file.write("rankdir=LR;\n")
        file.write(crearNodo("A","i","circle","black"))
        file.write(crearNodo("B","p","circle","black"))
        file.write(crearNodo("C","q","circle","black"))
        file.write(crearNodo("D","f","doublecircle","black"))
        file.write(unionNodo("A","B")+"[label = \"λ,λ;#\"];")
        file.write(unionNodo("B","C")+"[label = \"λ,λ;"+str(listaGramaticasT[0][1][2]).replace("']","")+"\"];")
        file.write(unionNodo("C","C")+"[label = \""+str(listaProduccionesAPila[x])+"\"];")
        file.write(unionNodo("C","D")+"[label = \"λ,#;λ\"];")
        file.write("}")
        file.close()
        os.system('dot -Tpng grafo'+str(contadorGraficas)+'.dot -o grafo'+str(contadorGraficas)+'.png')
        #os.startfile("grafo.png")
        listaIndiceGraficas.append(contadorGraficas)
        contadorGraficas=contadorGraficas+1
    
    file = open("index.html","w")
    file.write("<!DOCTYPE HTML>\n")
    file.write("<htm lang = \"es\">\n")
    file.write("<head>\n")
    file.write("<TITLE>GENERAR AUTOMATA DE PILA</TITLE>\n")
    #file.write("<link href=\"/Users/negrocorado/Desktop/Style.css\" rel=\"stylesheet\" type=\"text/css\">\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<div id = \"titulo\">\n")
    file.write("<h1>RESULTADO DE AUTOMATA DE PILA GENERADO</h1>\n")
    file.write("</div>\n")
    file.write("<div id= \"cuerpo\">\n")
    file.write("<table id= \"TablaGramatica\">\n")
    file.write("<tr>\n")
    file.write("    <td>\n")
    indexHTML=len(listaNombresGramaticasAP)
    for x in range(indexHTML):
        file.write("<h2>Nombre:  "+str(listaNombresGramaticasAP[x])+" </h2>\n")
        file.write("<h2>Terminales: { "+str(listaTerminalesGramaticasAP[x])+" }</h2>\n")
        file.write("<h2>AlfabetoPila: { "+str(listaAlfabetoGramaticasAP[x])+" }</h2>\n")
        file.write("<h2>"+estados+"</h2>\n")
        file.write("<h2>"+estadoInicio+"</h2>\n")
        file.write("<h2>"+estadoFin+"</h2>\n")
    file.write("    </td>\n")
    file.write("    <td>\n")
    indexGrafos=len(listaIndiceGraficas)
    for y in range(indexGrafos):
        file.write("        <img src=\""+"grafo"+str(listaIndiceGraficas[y])+".png"+"\">\n")
    file.write("    </td>\n")
    file.write("</tr>\n")
    file.write("</table>")
    file.write("</div>\n")
    file.write("<div>\n")
    file.write("<p><h3>  Walther Andree Corado Paiz </h3></p>\n")
    file.write("<p><h3>  Carnet: 201313861 </h3></p>\n")
    file.write("<p><h3>  Lenguajes Formales B- </h3></p>\n")
    file.write("</div>\n")
    file.write("</body>\n")
    file.write("</htmlL>\n")
    #os.startfile("index.html")
    #os.open("index.html")

def reporteRecorrido():
    global pilaAutomata,contadorGraficas,listaProduccionesAPila
    cadenaIngreso=input("Ingrese una Cadena a Evaluar:\n")
    print(cadenaIngreso)
    print(len(cadenaIngreso))
    indexCadenaIngreso=len(cadenaIngreso)
    #for x in range(indexCadenaIngreso):
        #print(cadenaIngreso[x])
    #----------------------------------------------- Se Crea el primer Grafo para la pagina -----------------------------------------
    file = open("grafo"+str(contadorGraficas)+".dot","w")
    file.write("digraph G{\n")
    file.write("rankdir=LR;\n")
    file.write(crearNodo("A","i","circle","yellow"))
    file.write(crearNodo("B","p","circle","black"))
    file.write(crearNodo("C","q","circle","black"))
    file.write(crearNodo("D","f","doublecircle","black"))
    file.write(unionNodo("A","B")+"[label = \"λ,λ;#\""+",color=red];")
    file.write(unionNodo("B","C")+"[label = \"λ,λ;"+str(listaGramaticasT[0][1][2]).replace("']","")+"\""+",color=black"+"];")
    indexProducionesOp4=len(listaProduccionesAPila)
    for x in range(indexProducionesOp4):
        file.write(unionNodo("C","C")+"[label = \""+str(listaProduccionesAPila[x])+"\"];")
    file.write(unionNodo("C","D")+"[label = \"λ,#;λ\""+",color=black"+"];")
    file.write("}")
    file.close()
    os.system('dot -Tpng grafo'+str(contadorGraficas)+'.dot -o grafo'+str(contadorGraficas)+'.png')
    #os.startfile("grafo.png")
    listaIndiceGraficas.append(contadorGraficas)
    contadorGraficas=contadorGraficas+1
    pilaAutomata.append("#")
    listaEstadoPila.append(list(pilaAutomata))
    imprimePila()
    #----------------------------------------------- Se Crea el Segundo Grafo para la pagina -----------------------------------------
    file = open("grafo"+str(contadorGraficas)+".dot","w")
    file.write("digraph G{\n")
    file.write("rankdir=LR;\n")
    file.write(crearNodo("A","i","circle","black"))
    file.write(crearNodo("B","p","circle","yellow"))
    file.write(crearNodo("C","q","circle","black"))
    file.write(crearNodo("D","f","doublecircle","black"))
    file.write(unionNodo("A","B")+"[label = \"λ,λ;#\""+",color=black];")
    file.write(unionNodo("B","C")+"[label = \"λ,λ;"+str(listaGramaticasT[0][1][2]).replace("']","")+"\""+",color=red"+"];")
    indexProducionesOp4=len(listaProduccionesAPila)
    for x in range(indexProducionesOp4):
        file.write(unionNodo("C","C")+"[label = \""+str(listaProduccionesAPila[x])+"\"];")
    file.write(unionNodo("C","D")+"[label = \"λ,#;λ\""+",color=black"+"];")
    file.write("}")
    file.close()
    os.system('dot -Tpng grafo'+str(contadorGraficas)+'.dot -o grafo'+str(contadorGraficas)+'.png')
    #os.startfile("grafo.png")
    listaIndiceGraficas.append(contadorGraficas)
    contadorGraficas=contadorGraficas+1
    pilaAutomata.append("S")
    listaEstadoPila.append(list(pilaAutomata))
    print("Cadena: "+cadenaIngreso)
    imprimePila()

    indexPilaEstudiada=len(pilaAutomata)
    #for x in range(indexPilaEstudiada):
    
    print(str(pilaAutomata[indexPilaEstudiada-1]))
    indexCadenaIngreso=len(cadenaIngreso)
    for a in range(indexCadenaIngreso):
        indexProducciones = len(listaProduccionesGramaticasAp)
        for y in range(indexProducciones):
            #print(str(listaProduccionesGramaticasAp[y]))
            indexProducciones2 = len(listaProduccionesGramaticasAp[y])
            for x in range(indexProducciones2):
                #print(str(listaProduccionesGramaticasAp[y][x]))
                produccion=str(listaProduccionesGramaticasAp[y][x]).split(",")
                indexProudccionBuscar = len(produccion)
                for z in range(indexProudccionBuscar):
                    if(z==1):
                        if(len(produccion[z])==1):
                            if(pilaAutomata[indexPilaEstudiada-1]==produccion[z]):
                                if(str(produccion[z+1])=="λ"):
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    #pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    grafoEstadoQ()
                                    imprimePila()
                                else:
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    grafoEstadoQ()
                                    imprimePila()
                            elif(pilaAutomata[indexPilaEstudiada-1]==cadenaIngreso[a]):
                                if(str(produccion[z+1])=="λ"):
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    #pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    cadenaIngreso.replace(cadenaIngreso[a],"",1)
                                    grafoEstadoQ()
                                    imprimePila()
                                else:
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    cadenaIngreso.replace(cadenaIngreso[a],"",1)
                                    grafoEstadoQ()
                                    imprimePila()
                        else:
                            indexComparativoProducciones=len(produccion[z])
                            if(pilaAutomata[indexPilaEstudiada-1][indexComparativoProducciones-1]==produccion[z]):
                                if(str(produccion[z+1])=="λ"):
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    #pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    grafoEstadoQ()
                                    imprimePila()
                                else:
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    grafoEstadoQ()
                                    imprimePila()
                            elif(pilaAutomata[indexPilaEstudiada-1][indexComparativoProducciones-1]==cadenaIngreso[a]):
                                if(str(produccion[z+1])=="λ"):
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    #pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    cadenaIngreso.replace(cadenaIngreso[a],"",1)
                                    grafoEstadoQ()
                                    imprimePila()
                                else:
                                    pilaAutomata.remove(str(pilaAutomata[indexPilaEstudiada-1]))
                                    pilaAutomata.append(str(produccion[z+1]))
                                    listaEstadoPila.append(list(pilaAutomata))
                                    cadenaIngreso.replace(cadenaIngreso[a],"",1)
                                    grafoEstadoQ()
                                    imprimePila()
                            
                            

                        
    #--------------- se genera el HTML DEL recorrido: ----------------------------
    file = open("Recorrido.html","w")
    file.write("<!DOCTYPE HTML>\n")
    file.write("<htm lang = \"es\">\n")
    file.write("<head>\n")
    file.write("<TITLE>GENERAR RECORRIDO DE AUTOMATA DE PILA</TITLE>\n")
    #file.write("<link href=\"/Users/negrocorado/Desktop/Style.css\" rel=\"stylesheet\" type=\"text/css\">\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<div id = \"titulo\">\n")
    file.write("<h1>GENERAR RECORRIDO DE AUTOMATA DE PILA</h1>\n")
    file.write("</div>\n")
    file.write("<div id= \"cuerpo\">\n")
    file.write("<table id= \"TablaGramatica\">\n")
    indexPilaEstudiada=len(listaEstadoPila)
    for x in range(indexPilaEstudiada):
        file.write("<tr>\n")
        file.write("    <td>\n")
        file.write("<h3>Pila: "+str(listaEstadoPila[x])+"</h3>\n")
        file.write("<h3>Cadena: "+cadenaIngreso+"</h3>\n")
        file.write("    </td>\n")
        file.write("    <td>\n")
        file.write("        <img src=\""+"grafo"+str(listaIndiceGraficas[x+1])+".png"+"\">\n")
        file.write("    </td>\n")
        file.write("</tr>\n")
    file.write("</table>")
    file.write("</div>\n")
    file.write("<div>\n")
    file.write("<p><h3>  Walther Andree Corado Paiz </h3></p>\n")
    file.write("<p><h3>  Carnet: 201313861 </h3></p>\n")
    file.write("<p><h3>  Lenguajes Formales B- </h3></p>\n")
    file.write("</div>\n")
    file.write("</body>\n")
    file.write("</htmlL>\n")
    #os.startfile("index.html")
    #os.open("index.html")
    print("HTML GENERADO")

def grafoEstadoQ():
    global contadorGraficas
    #----------------------------------------------- Se Crea el Tercer Grafo para la pagina -----------------------------------------
    file = open("grafo"+str(contadorGraficas)+".dot","w")
    file.write("digraph G{\n")
    file.write("rankdir=LR;\n")
    file.write(crearNodo("A","i","circle","black"))
    file.write(crearNodo("B","p","circle","black"))
    file.write(crearNodo("C","q","circle","yellow"))
    file.write(crearNodo("D","f","doublecircle","black"))
    file.write(unionNodo("A","B")+"[label = \"λ,λ;#\""+",color=black];")
    file.write(unionNodo("B","C")+"[label = \"λ,λ;"+str(listaGramaticasT[0][1][2]).replace("']","")+"\""+",color=black"+"];")
    indexProducionesOp4=len(listaProduccionesAPila)
    for x in range(indexProducionesOp4):
        file.write(unionNodo("C","C")+"[label = \""+str(listaProduccionesAPila[x])+"\",color=red];")
    file.write(unionNodo("C","D")+"[label = \"λ,#;λ\""+",color=black"+"];")
    file.write("}")
    file.close()
    os.system('dot -Tpng grafo'+str(contadorGraficas)+'.dot -o grafo'+str(contadorGraficas)+'.png')
    #os.startfile("grafo.png")
    listaIndiceGraficas.append(contadorGraficas)
    contadorGraficas=contadorGraficas+1

def imprimePila():
    cadenaPila=""
    indexPilaEstudio=len(pilaAutomata)
    for x in range(indexPilaEstudio):
        cadenaPila=cadenaPila+str(pilaAutomata[x])
    print("Pila: "+cadenaPila)

def crearNodo(identificador,nombre, shape, color):
    return identificador + "[label=\""+ nombre + "\",shape="+ shape + ",color="+color+ "]\n"

def unionNodo(nodoA,nodoB):
    return nodoA + "->" + nodoB +"\n"

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
        reporteRecorrido()
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
        