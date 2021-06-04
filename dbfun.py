# paquetes a usar
import pyodbc
import os

# Datos para la conexión al servidor online 
ds='sql5101.site4now.net'                 # Nombre del servidor
nombre_bd='DB_A6E49B_jeyson2496'          # Nombre de la base de datos
usuario='DB_A6E49B_jeyson2496_admin'      # Usuario
password='lf7ejpsy'                       # Contraseña


# Hacemos la conexión con los datos previos. La variable "conn" es nuestra conexión
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+ds+';Database='+nombre_bd+';UID='+usuario+';PWD='+password)

# Damos los atributos de cursor a "coon". Un cursor es un objeto de acceso de datos
cursor = conn.cursor();


# DEFINIREMOS LAS FUNCIONES A USAR.

# NUMERO DE FILAS DE UNA TABLA
def count(D):
    return len(D.fetchall())

# MUESTRA TODA LA TABLA DE DATOS
def showT():

    print('\n')
    print('ID          Nombre                Gr. Sanguineo         Dirección          Cant. Donada')
    for rows in cursor.execute('select * from Datos'):
        print(rows)
        
def showDP():
    print('\n')
    print('ID          Nombre                \tGr. Sanguineo        \t Dirección           \t\t Cant. Donada\n')
    a=cursor.execute('select * from Datos').fetchall()
    i=0
    for rows in cursor.execute('select * from Datos'):
        print(a[i][0],'  \t',a[i][1],' \t',a[i][2],' \t\t',a[i][3],' \t',a[i][4])
        i=i+1

# MUESTRA LA TABLA DE SANGRE
def showB():
    print('\n')
    print('\tBlood Type   \tCantidad ')
    a=cursor.execute('select * from Blood').fetchall()
    i=0
    for rows in cursor.execute('select * from Blood'):
        print('\t',a[i][0],'  \t',a[i][1],)
        i=i+1
    
        
# AGREGA UN DONANTE
def set_donador(nombre,t_sangre,direccion):
    A=[nombre,t_sangre,direccion,0.45]
    cursor.execute('INSERT INTO Datos (Name, Blood_Type, Adress, Blood) VALUES(?,?,?,?)',A)
    conn.commit()

# SUMA DE SANGRE DE ACUARDO AL TIPO
def sumB(BT):
    a=cursor.execute('SELECT SUM(Blood) FROM Datos WHERE Blood_Type=(?)',BT).fetchall()
    return a[0][0]

# AGREGAR CANTIDAD DE SANGRE
def updateB(BT):
    s=sumB(BT)
    cursor.execute('UPDATE Blood SET liters=? WHERE Blood_Type=?',s,BT)
    conn.commit()


# BUSCA Y RETORNA UN DONANTE POR NOMBRE
def searchN(nombre):
    return cursor.execute('SELECT * FROM Datos WHERE Name Like ?','%'+nombre+'%')    

# BUSCA Y RETORNA UN DONANTE POR ID
def searchID(ID):
    return cursor.execute('SELECT * FROM Datos WHERE ID=(?)',ID)


# BUSCA Y RETORNA DONANTE(S) POR MEDIO DEL TIPO DE SANGRE
def searchBT(BT):
    return cursor.execute('SELECT * FROM Datos WHERE Blood_Type=(?)',BT)

# MUESTRA UNA TABLA EN PARTICULAR
def showTable(t):
    print('\n')
    print('ID          Nombre                \tGr. Sanguineo        \t Dirección           \t\t Cant. Donada')
    a=t.fetchall()
    i=0
    for rows in a:
        print(a[i][0],'  \t',a[i][1],' \t',a[i][2],' \t\t',a[i][3],' \t',a[i][4])
        i=i+1
    if i==0:
        print('\nNo hay datos')
            
# MUESTRA INFORMACIÓN POR MEDIO DEL ID       
def showID(ID):
    i=0
    for rows in searchID(ID):
        i=i+1
    if i==0:
        print('No se encontro donantes con ese nombre')
    else:
        print('\n')
        print('\t  ID          Nombre                Gr. Sanguineo         Dirección             ')
        for rows in searchID(ID):
            print('\t',rows)            



# MUESTRA INFORMACIÓN POR MEDIO DEL NOMBRE
def showN(nombre):
    print('\n')
    i=0
    for rows in searchN(nombre):
        i=i+1
    if i==0:
        print('No se encontro donantes con ese nombre')
    else:
        for rows in searchN(nombre):
            print(rows)            



# MUESTRA INFORMACIÓN POR MEDIO DEL TIPO DE SANGRE
def showBT(BT):
    print('\n')
    i=0
    for rows in searchBT(BT):
        i=i+1
    if i==0:
        print('No se encontro donantes con ese grupo sanguineo')
    else:
        for rows in searchBT(BT):
            print(rows)
    return i

#  BUSCA Y RETORNA INFORMACION POR MEDIO DE LA DIRECCIÓN
def searchAD(AD):
    return cursor.execute('SELECT * FROM Datos WHERE Adress Like ?','%'+AD+'%')

# MUESTRA INFORMACION POR MEDIO 
def showAD(AD):
    print('\n')
    i=0
    for rows in searchAD(AD):
        i=i+1
    if i==0:
        print('No se encontro donantes con esa dirección')
    else:
        for rows in searchAD(AD):
            print(rows)

# ELIMINA LA INFORMACIÓN DE UN DOTANTE POR ID
def deleteID(ID):
    cursor.execute('DELETE from Datos WHERE ID=(?)',ID)
    conn.commit()

# ELIMINA LA INFORMACIÓN DE UN DOTANTE POR NOMBRE
def deleteN(nombre):
    cursor.execute('DELETE from Datos WHERE Name=(?)',nombre)
    conn.commit()
    


def delete(choice , dato):
    if choice == '1':

        if count(searchID(dato))==0:
            print('\n\tNo se encontraron datos.')
        else:
            ib=0            
            while ib==0:
                # os.system('cls')
                showTable(searchID(dato))
                yn = input('\nEsta seguro de elimiar este donante? (Y/N): ')
                if yn =='Y':
                    deleteID(dato)
                    ib=1
                    print('Información del donante eliminado exitosamente')
                    # sp=input(' ')
                    # os.system('cls')
                if yn =='N':
                    ib=1   
            
    elif choice =='2':

        if count(searchN(dato))==0:
            showN(dato)
        elif count(searchN(dato))==1: 
            ib=0            
            while ib==0:
                #os.system('cls')
                showTable(searchN(dato))
                yn = input('\nEsta seguro de elimiar este donante? (Y/N): ')
                if yn =='Y':
                    deleteN(dato)
                    ib=1
                    print('Información del donante eliminado exitosamente')
                    sp=input(' ')
                    #os.system('cls')
                if yn =='N':
                    ib=1
        else: 
            ib=0
            while ib==0:           
                showTable(searchN(dato))    
                n=input('\nIngrese ID de la persona a eliminar: ')
                os.system('cls')
                if n.isdigit():
                    if count(searchID(n))>0:
                        ia=0
                        while ia==0:
                            os.system('cls')
                            showTable(searchID(n))
                            yn = input('\nEsta seguro de elimiar este donante? (Y/N): ')
                            if yn =='Y':
                                deleteID(n)
                                ib=1
                                ia=1
                                print('\nInformación del donante eliminado exitosamente')
                                #sp=input(' ')
                            elif yn =='N':
                                print('\nNo se elimino información')
                                ib=1
                                ia=1
                            else:
                                print('\nIngrese una opción valida ')
                                sp=input(' ')
                    else:
                        print('\nIngrese un ID valido')
                        sp=input(' ')
                        
                else:
                    print('\nIngrese un ID valido')
                    sp=input(' ')
    else:
        print(sp)        

def modtable(dato,nombre,ad):
    
        # if count(searchID(dato))==0:
        #     print('No se encontraron datos con ese nombre.')
        # else:
            ib=0            
            while ib==0:
                os.system('cls')
                showID(dato)
                yn = input('\nEsta seguro de modificar esta informacion? (Y/N): ')
                if yn =='Y':
                    os.system('cls')
                    modrows(dato,nombre,ad)
                    ib=1
                    showID(dato)
                    print('\nInformación modificada exitosamente')   
                if yn =='N':
                    ib=1
                # else:
                #     print('\n\tINGRESE UNA OPCION VALIDA!')
    # else:
    #     if count(searchN(dato))==0:
    #         showN(dato)
    #     else: 
    #         ib=0            
    #         while ib==0:
    #             os.system('cls')
    #             showTable(searchN(dato))
    #             n=input('Ingrese ID del dato a modificar:')
    #             yn = input('\nEsta seguro de modificar esta información? (Y/N): ')
    #             if yn =='Y':
    #                 os.system('cls')
    #                 modrows(n,nombre,ad)
    #                 ib=1
    #                 print('Información modificada exitosamente')
    #                 sp=input(' ')
    #             if yn =='N':
    #                 ib=1
    #else:
        #print(sp)


def modrows(ID,nombre,d):
    cursor.execute('UPDATE Datos SET Name=?, Adress=? WHERE ID=?',nombre,d,ID)
    conn.commit()

def sumblood(ts):
    a=cursor.execute('SELECT Liters FROM Blood WHERE Blood_Type=?',ts).fetchall()
    a=a[0][0]+0.45
    cursor.execute('UPDATE Blood SET Liters=? WHERE Blood_Type=?',a,ts)
    conn.commit()
    
    
def resblood(ts,f):
    a=cursor.execute('SELECT Liters FROM Blood WHERE Blood_Type=?',ts).fetchall()
    a=a[0][0]-f
    cursor.execute('UPDATE Blood SET Liters=? WHERE Blood_Type=?',a,ts)
    conn.commit()

def cant(b):
    a=cursor.execute('SELECT Liters FROM Blood WHERE Blood_Type=?',b).fetchall()
    return a[0][0]

def bloodcheck(bt,cant):
    if cant(bt)>=cant:
        resblood(bt,cant)
        print('\n\tSe ha retirado exitosamente')
    else:
        os.system('cls')
        print('\n\tNo hay suficiente sangre')
        
def addbloodID(ID):
    a=cursor.execute('SELECT Blood FROM Datos WHERE ID=?',ID).fetchall()
    a=a[0][0]+0.45
    cursor.execute('UPDATE Datos SET Blood=? WHERE ID=?',a,ID)
    conn.commit()

def isfloat(str):
    c=0
    d=0
    for a in str: 
        if a.isdigit() :
            c=c+0
        elif a=='.': 
            d=d+1
        else: 
            c=c+1
    if c==0 and (d==0 or d==1):
         result =True
    else: 
        result =False
    return result
