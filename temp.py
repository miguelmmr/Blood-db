import dbfun
import os


os.system('cls')
print( "\n\t========================================")
print( "\n\t\t|   Banco de Sangre  |" )
print( "\n\t========================================")
print("\n")

print('\n\t(1) Entrar como admin')
print('\n\t(2) Entrar como invitado')
print('\n\n\t(s) Salir')

opc1=input('\n\t Ingrese opción: ')
menu0=0
while menu0==0:
    if opc1=='2':
        n=1
        menu0=1
        menul=1
    elif opc1=='1':
        user = input("\n\tUsuario: ")
        print('\n')
        pasw = input("\n\tContraseña: ")
        menul = 0
        menu0=1
        os.system('cls')
    elif opc1=='s':
        n=4
        menu0=1
        menul=1
    else:
        os.system('cls')
        print( "\n\t========================================")
        print( "\n\t\t|   Banco de Sangre  |" )
        print( "\n\t========================================")
        print("\n")
        print('\n\t(1) Entrar como admin')
        print('\n\t(2) Entrar como invitado')
        print('\n\n\t(s) Salir')
        opc1=input('\n\t Ingrese opción: ')

while menul ==0:
    print('\n')
    
    menul=1
    if user == "Usuario1" and pasw == "password2":
        n=1
        os.system('cls')
    elif user =="usuario2" and pasw =="password2":
        n=2
    elif user =="DB_A6E49B_jeyson2496_admin" and pasw =="lf7ejpsy":
        n=3
    else:
        print('\tUsuario o contraseña incorrecto')
        print('\n')
        print('\t\tEnter para regresar')
        print('\n')
        salir = input('\t\tIngrese "s" para salir  ')
        if salir == 's':
            n=4
        else:
            os.system('cls')
            menul=0
            print( "\n========================================")
            print( "\n\t|   Banco de Sangre  |" )
            print( "\n========================================")
            print("\n")
            user = input("Usuario: ")
            print('\n')
            pasw = input("Contraseña: ")
            
if n==1: 
    i=0
    while i==0:
        os.system('cls')
        print('\n')
        print('\t____________________________________')
        print('\t(1)  Mostrar lista de donadores')
        print('\t(2)  Buscar donante')        
        print('\t(s)  Salir ')
        print('\t____________________________________')
        m = input("\tIngrese el numero de la opción:   ")
        if m =='1':
            os.system('cls')
            dbfun.showDP()
            print('\n')
            wait = input("Presione enter para continuar.")
        elif m=='2':
            ib=0
            while ib==0:
                os.system('cls')
                print('\n')
                print('\t____________________________________')
                print('\t(1)  ID')
                print('\t(2)  Nombre')
                print('\t(3)  Grupo sanguineo')
                print('\t(4)  Dirección')
                print('\t(s)  Para regresar')
                print('\t____________________________________')
                choiceB= input('\tIngrese el tipo de dato con que quiere buscar: ')
                if choiceB == '1':
                    os.system('cls')
                    idd=input('\n\tIngrese el id del donante: ')
                    if idd.isdigit():
                        os.system('cls')
                        dbfun.showTable(dbfun.searchID(idd))
                    else:
                        print('\n\tNo existe ID, intentelo de nuevo')
                    sp=input(' ')
                    os.system('cls')
                elif choiceB == '2':
                    os.system('cls')
                    nom=input('\n\tIngrese el nombre del donante: ')
                    os.system('cls')
                    dbfun.showTable(dbfun.searchN(nom))
                    sp=input(' ')
                    os.system('cls')
                elif choiceB=='3':
                    os.system('cls')
                    gp=input('\n\tIngrese el grupo sanguineo del donante: ')
                    if gp=='A+' or gp=='A-' or gp=='B+' or gp=='B-' or gp=='AB+' or gp=='AB-' or gp=='O+' or gp=='O-':
                        os.system('cls')
                        dbfun.showTable(dbfun.searchBT(gp))
                        sp=input(' ')
                    else:
                        print('\n\tNo existe el Grupo sanguineo, intentelo de nuevo')
                        sp=input('')
                elif choiceB =='4':
                    os.system('cls')
                    ad=input('\n\tIngrese la dirección del donante: ')
                    dbfun.showTable(dbfun.searchAD(ad))
                    sp=input(' ')
                    os.system('cls')
                elif choiceB=='s':
                    os.system('cls')
                    ib=1
                else:
                    print('\n')
                    print('\tINGRESE UNA OPCIÓN VALIDA!')  
                    wait=input('\t')        
        elif m=='s':
            os.system('cls')
            print('\t____________________________________')
            print("\n\t\tSesión terminada")
            print('\t____________________________________\n')
            i=1
        else:
            print('\n')
            print('\tINGRESE UNA OPCIÓN VALIDA!')
            wait=input('\t')
elif n==2: 
    i=0
    while i==0:
        print('Mostrar lista de donadores: (1)')
        print('Añadir donador nuevo: (2)')
        print('Salir (3)')
        m = input("Ingrese el numero de la opción:   ")
        if m =='1': 
            
            dbfun.showT()
        elif m=='2':
            
            print('Ingrese los datos del nuevo donante:\n')
            nombre=input('Nombre:  ')
            sang = input('Gr. Sanguineo:  ')
            direc = input('Dirección')
            dbfun.set_donador(nombre, sang, direc)
        elif m=='3':
            print("nos fuimos")
            i=1
        else:
            print('try again nigger')

elif n==3:
    i=0
    while i==0:
        os.system('cls')
        print('\n')
        print('\t____________________________________')
        print('\t(1)  Mostrar lista de donantes')
        print('\t(2)  Buscar donante')
        print('\t(3)  Añadir donante')
        print('\t(4)  Eliminar datos de donante')
        print('\t(5)  Actualizar datos de donante')
        print('\t(6)  Registro de sangre')
        print('\t(s)  Salir ')
        print('\t____________________________________')
        m = input("\n\tIngrese una opción:   ")
        if m =='1':
            os.system('cls')
            dbfun.showDP()
            print('\n')
            wait = input("Presione enter para continuar.")
        elif m=='2':
            ib=0
            while ib==0:
                os.system('cls')
                print('\n')
                print('\t____________________________________')
                print('\t(1)  ID')
                print('\t(2)  Nombre')
                print('\t(3)  Grupo sanguineo')
                print('\t(4)  Dirección')
                print('\t(s)  Para regresar')
                print('\t____________________________________')
                choiceB= input('\tIngrese el tipo de dato con que quiere buscar: ')
                if choiceB == '1':
                    os.system('cls')
                    idd=input('\n\tIngrese el id del donante: ')
                    if idd.isdigit():
                        os.system('cls')
                        dbfun.showTable(dbfun.searchID(idd))
                    else:
                        print('\n\tNo existe ID, intentelo de nuevo')
                    sp=input(' ')
                    os.system('cls')
                elif choiceB == '2':
                    os.system('cls')
                    nom=input('\n\tIngrese el nombre del donante: ')
                    os.system('cls')
                    dbfun.showTable(dbfun.searchN(nom))
                    sp=input(' ')
                    os.system('cls')
                elif choiceB=='3':
                    os.system('cls')
                    gp=input('\n\tIngrese el grupo sanguineo del donante: ')
                    if gp=='A+' or gp=='A-' or gp=='B+' or gp=='B-' or gp=='AB+' or gp=='AB-' or gp=='O+' or gp=='O-':
                        os.system('cls')
                        dbfun.showTable(dbfun.searchBT(gp))
                        sp=input(' ')
                    else:
                        print('\n\tNo existe el Grupo sanguineo, intentelo de nuevo')
                        sp=input('')
                elif choiceB =='4':
                    os.system('cls')
                    ad=input('\n\tIngrese la dirección del donante: ')
                    dbfun.showTable(dbfun.searchAD(ad))
                    sp=input(' ')
                    os.system('cls')
                elif choiceB=='s':
                    os.system('cls')
                    ib=1
                else:
                    print('\n')
                    print('\tINGRESE UNA OPCIÓN VALIDA!')  
                    wait=input('\t')   
        elif m=='3':
            os.system('cls')
            print('\n\tIngrese los datos del nuevo donante:\n')
            nombre=input('\nNombre:  ')
            sang = input('\nGr. Sanguineo:  ')
            direc = input('\nDirección:  ')
            sp=input('\nSeguro que quiere añadir esta información?(Y/N)')
            if sp=='Y':
                if sang=='A+' or sang=='A-' or sang=='B+' or sang=='B-' or sang=='AB+' or sang=='AB-' or sang=='O+' or sang=='O-':
                    dbfun.set_donador(nombre, sang, direc)
                    os.system('cls')
                    dbfun.sumblood(sang)
                    print('\n\tSe ha ingresado exitosamente la información del nuevo donante!')
                    sp=input(' ')
                else:
                    os.system('cls')
                    print('\n\tNo existe el Grupo sanguineo, intentelo de nuevo')
                    sp=input(' ')
            elif sp=='N':
                os.system('cls')
                print('\n\tNo se agrego información')
            else:
                os.system('cls')
                print('\n\tOpción no valida, intentelo nuvamente')
                sp=input(' ')
            os.system('cls')
            
        elif m=='4':
                ld=0
                while ld ==0:
                    os.system('cls')
                    print('\n')
                    print('\t____________________________________')
                    print('\t(1)  ID')
                    print('\t(2)  Nombre')
                    print('\t(s)  Para regresar al menu')
                    print('\t____________________________________')
                    choiceD= input('\n\tIngrese una opción: ')
                    os.system('cls')
                    if choiceD =='1':
                        datod = input('\n\tIngrese información del donante:')
                        if datod.isdigit():
                            os.system('cls')
                            dbfun.delete(choiceD,datod)
                            sp=input('')
                            ld=1
                        else:
                            os.system('cls')
                            print('\n\tOpción no válida, intentelo de nuevo')
                            sp=input('')
                    elif choiceD=='2':
                        datod = input('\n\tIngrese información del donante: ')
                        os.system('cls')
                        dbfun.delete(choiceD,datod)
                        sp=input('')
                        ld=1
                    elif choiceD == 's':
                        ld = 1
                        os.system('cls')
                    else:
                        print('\n\tINGRESE UNA OPCIÓN VALIDA')
                        sp=input('')
                        os.system('cls')
                        
        elif m=='5':
            
            lc=0
            while lc ==0:
                os.system('cls')
                print('\n')
                print('\t____________________________________')
                print('\t(1)  Actualizar cantidad donada ')
                print('\t(2)  Modificar información de donante')
                print('\t(s)  Regresar')
                print('\t____________________________________')
                choiceC= input('\n\tIngrese una opción: ')
                if choiceC =='1':
                    ld=0
                    while ld ==0:
                        #os.system('cls')
                        # print('\n')
                        # print('\t____________________________________')
                        # print('\t(1)  ID')
                        # print('\t(2)  Nombre')
                        # print('\t(s)  Para regresar al menu')
                        # print('\t____________________________________')
                        #choiceD= input('\tIngrese el ID del donante recurrente ')  
                        # if choiceD =='1':
                        os.system('cls')
                        print('\n\t(s) Salir\n')
                        datod = input('\n\tIngrese el ID del donante recurrente ')  
                        if datod.isdigit():
                            if dbfun.count(dbfun.searchID(datod))>0:
                                z=0
                                while z==0:
                                    os.system('cls')
                                    dbfun.showTable(dbfun.searchID(datod))
                                    op=input('\n\tEs la información del donante recurrente?(Y/N):')
                                    if op == 'Y':
                                        dbfun.addbloodID(datod)
                                        print('\n\tInformación del donante actualizada exitosamente') 
                                        sd=input('')
                                        ld=1
                                        lc=1
                                        z=1
                                    elif op == 'N':
                                        print('\n\tNo se actualizo información.')
                                        sd=input('')
                                        ld=1
                                        lc=1
                                        z=1
                                    else:
                                        print('\n\tOpción no válida.')
                                        sp=input('')
                            else:
                                print('\n\tNo existe ID, intentelo de nuevo')
                                sp=input('')
                        elif datod == 's':
                            ld=1
                        else:
                              print('\n\tNo existe ID, intentelo de nuevo') 
                              sp=input('')
                        # elif choiceD =='2':
                        #     os.system('cls')
                        #     datod = input('\n\tIngrese el nombre:')
                        # elif choiceD == 's':
                        #     ld = 1
                        #     lc = 1
                        #     os.system('cls')
                        # else:
                        #     print('\n\tINGRESE UNA OPCIÓN VÁLIDA!') 
                        #     sd=input('')
                elif choiceC == '2':
                    ld=0
                    while ld ==0:
                        # os.system('cls')
                        # print('\n')
                        # print('\t____________________________________')
                        # print('\t(1)  ID')
                        # print('\t(2)  Nombre')
                        # print('\t(s)  Para regresar al menu')
                        # print('\t____________________________________')
                        # choiceD= input('\tIngrese el tipo de dato por el que quiere modificar la información: ')  
                        # if choiceD =='1':
                        os.system('cls')
                        print('\n\t(s) Salir\n')
                        datod = input('\n\tIngrese ID del donante: ')
                        if datod.isdigit():
                            if dbfun.count(dbfun.searchID(datod))>0:
                                os.system('cls')
                                dbfun.showTable(dbfun.searchID(datod))
                                op=input('\n\tEs la información a modificar?(Y/N):')
                                if op == 'Y':
                                    nnombre = input('\tIngrese nuevo nombre: ')
                                        #nts=input('\tIngrese el tipo de sangre:')
                                    nad=input('\tIngrese dirección: ')
                                    z=0
                                    while z==0:
                                        op1=input('\n\tEs correcta la nueva información?(Y/N):')
                                        if op1 =='Y':
                                            dbfun.modtable(datod,nnombre,nad)
                                                #print('\n\tDato modificado correctamente.')
                                                #sd=input('')
                                            ld=1
                                            lc=1
                                            z=1
                                        elif op1 =='N':
                                            print('\n\tPrueba una nueva opción.')
                                            z=1
                                                #sd=input('')
                                        else:
                                            print('\n\tIngrese una opción válida.')
                                                #sp=input('')       
                                        sp=input('')
                                elif op == 'N':
                                    print('\n\tN')
                                    sp=input('')
                                    ld=1
                                    lc=1
                                else:
                                    print('\n\tOpción no válida.')
                                    sp=input('')
                            else:
                                print('\n\tNo existe ID, intentelo de nuevo')
                                sp=input('')
                        elif datod == 's':
                            ld=1
                        else:
                            print('\n\tNo existe ID, intentelo de nuevo')
                            sp=input('')
                        # elif choiceD =='2':
                        #     os.system('cls')
                        #     datod = input('\n\tIngrese el nombre:')
                        # elif choiceD == 's':
                        #     ld = 1
                        #     lc = 1
                        #     os.system('cls')
                        # else:
                        #     print('\n\tINGRESE UNA OPCIÓN VÁLIDA!') 
                        #     sd=input('')
                elif choiceC =='s':
                    lc=1
                    os.system('cls')
                else :
                    print('\n')
                    print('\tINGRESE UNA OPCIÓN VALIDA!')  
                    wait=input('\t')
        elif m=='6':
            os.system('cls')
            print('\n')
            print('\t____________________________________')
            print('\t(1)  Ver registro')
            print('\t(2)  Retirar sangre')
            print('\t(s)  Regresar')
            print('\t____________________________________')
            choiceD= input('\n\tIngrese una opción: ')
            ld=0
            while ld==0:
                if choiceD =='1':
                    os.system('cls')
                    dbfun.showB()
                    sp=input('')
                    ld=1
                elif choiceD =='2':
                    os.system('cls')
                    print('Seleccione un tipo de sangre: ')
                    print('\t(1)  A+')
                    print('\t(2)  A-')
                    print('\t(3)  B+')
                    print('\t(4)  B-')
                    print('\t(5)  AB+')
                    print('\t(6)  AB-')
                    print('\t(7)  O+')
                    print('\t(8)  O-')
                    print('\t(s)  Salir')
                    o1=input('\tIngrese opción: ')
                    if o1 =='1' :
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('A+')>=float(o2):
                                dbfun.resblood('A+',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '2':
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('A-')>=float(o2):
                                dbfun.resblood('A-',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '3':
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('B+')>=float(o2):
                                dbfun.resblood('B+',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '4':
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('B-')>=float(o2):
                                dbfun.resblood('B-',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '5':
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('AB+')>=float(o2):
                                dbfun.resblood('AB+',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '6' :
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('AB-')>=float(o2):
                                dbfun.resblood('AB-',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '7' :
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('O+')>=float(o2):
                                dbfun.resblood('O+',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == '8' :
                        o2=input('\tIngrese la cantidad(litros): ')
                        if dbfun.isfloat(o2):
                            if dbfun.cant('O-')>=float(o2):
                                dbfun.resblood('O-',float(o2))
                                print('\n\tSe retiro exitosamente')
                            else:
                                os.system('cls')
                                print('\n\tNo hay suficiente sangre')
                        else:
                            os.system('cls')
                            print('\n\tNo ingreso un dato adecuado')
                        sp=input('')
                        ld=1
                    elif o1 == 's':
                        ld=1
                    else:
                        print('\n\tINGRESE UNA OPCIÓN VÁLIDA!') 
                        sd=input('')
                    
                elif choiceD =='3':
                    ld = 1
                    os.system('cls')
                else:
                    print('\n\tINGRESE UNA OPCIÓN VÁLIDA!') 
                    ld=1
                    sd=input('')
        elif m=='s':
            os.system('cls')
            print('\t____________________________________')
            print("\n\t\tSesión terminada")
            print('\t____________________________________\n')
            i=1
        else:
            print('\n')
            print('\tINGRESE UNA OPCIÓN VALIDA!')  
            wait=input('\t')
else:
    os.system('cls')
    print('\n\tGracias por su visita')
    sp=input('')
    print(sp)
    

