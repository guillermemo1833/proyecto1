import json
import requests

#Funcion Score Events
def Tipe(n):
    P="PushEvent"
    Cr="CreateEvent"
    I="IssuesEvent"
    Co="CommitCommentEvent"
    score=0
    i=0
    
    URL='https://api.github.com/users/'+n+'/events'
    resp = requests.get(URL)
    data=json.loads(resp.content)

    for i in range(len(data)):
        a=data[i]["type"]
     
        if P == a:            
            score=score+5
        elif Cr==a:            
            score=score+4
        elif Co==a:            
            score=score+2
        elif I==a:
            score=score+3            
        else:
            score=score+1
    return score

#Funcion Followers
def Followers(n):
    a=0    
    URL='https://api.github.com/users/'+n
    resp = requests.get(URL)
    data=json.loads(resp.content)
    a=data["followers"]
    
    return a

#Funcion Stars
def Stars(n):
    k=0
    a=0
    cont=0
    URL='https://api.github.com/users/'+n+'/repos'
    resp = requests.get(URL)
    data=json.loads(resp.content)
    for k in range(len(data)):
        a=data[k]["stargazers_count"]
        cont=cont+a
    return cont

#Funcion Puntajetotal
def Puntajet(n):
    a=Tipe(n)
    b=Followers(n)
    c=Stars(n)
    PuntajeTotal=((a*0.4)+(c*0.4)+(b*0.2))
    return PuntajeTotal

#Funcion Battle
def Battle(n,n1):
    print ('Nombre del primer usuario:',n)
    print ('Nombre del segundo usuario',n1)
    p1=Puntajet(n)
    print (me,p1)
    p2=Puntajet(n1)
    print(mo,p2)

    if p1 < p2:
        return n1
    elif p1>p2:
        return n
    else:
        h="Empate"
        return h

#Funcion para Escribir en un archivo de texto 
def Escribir(n):
    a=Puntajet(n)
    URL=':     https://api.github.com/users/n'+n+'     '
    Apuntes=str(a)
    f = open ('datos_puntajes.txt','a')
    juntar=n+URL+Apuntes+'\n'
    f.write(juntar)
    f.close()

#Funcion para limpiar un archivo 
def Limpiar():
    f = open ('datos_puntajes.txt','w+')
    f.write('')
    f.close()

#Funcion para elejir opcion 
def Pregunta():
    print ('Elija una opcion:')
    print ('(1)  Preguntar por el puntaje de los eventos ()')
    print ('(2)  Preguntar por seguidores ()')
    print ('(3)  Preguntar por estrellas ()')
    print ('(4)  Preguntar por puntaje total ()')
    print ('(5)  Hacer una batalla ()')
    print ('(6)  Gurdar en un archivo ()')
    print ('(7)  Eliminar contenido del archivo ()')
    print ('(0)  Salir ()')
    i= input ()
    if i=='1':
        print ('Nombre del usuario:')
        nombre = input ()
        evento=Tipe(nombre)
        print('Puntaje event Store:',evento,'\n')
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='2':
        print ('Nombre del usuario:')
        nombre = input ()
        seguidores=Followers(nombre)
        print ('Seguidores:',seguidores)
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='3':
        print ('Nombre del usuario:')
        nombre = input ()
        estrellas=Stars(nombre)
        print ('Estrellas:',estrellas)
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='4':
        print ('Nombre del usuario:')
        nombre = input ()
        puntaje=Puntajet(nombre)
        print ('Puntaje total:',puntaje)
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='5':
        print ('Nombre de los usuarios:')
        nombre = input ()
        nombre1= input ()
        batalla=Battle(nombre,nombre1)
        print ('Ganador:',batalla)
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='6':
        print ('Nombre del usuario:')
        nombre = input ()
        archivo=Escribir(nombre)
        print (archivo)
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    elif i=='7':
        Limpiar
        print ('Precione enter para continuar...')
        input()
        Pregunta()
    else:
        print ('Adios')

print ('(1)  Ver el menu ()')
print ('(0)  Salir ()')
m=input()
if m=='1':
    Pregunta()
else:
    print ('Adios')