import json
import requests

print ('Nombre de usuarios que desea consultar:')
nombre = input()
nombre1= input()
print ('Nombre del primer usuario:',nombre)
print ('Nombre del segundo usuario',nombre1)

#funcion score events
def type(n):
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

#funcion Followers
def Followers(n):
    a=0    
    URL='https://api.github.com/users/'+n
    resp = requests.get(URL)
    data=json.loads(resp.content)
    a=data["followers"]
    
    return a

#funcion Stars
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

#funcion puntajetotalç
def puntajet(a,b,c):
    PuntajeTotal=((a*0.4)+(c*0.4)+(b*0.2))
    return PuntajeTotal

#funcion battle
def battle(n,n1):
    a=type(n)
    b=Followers(n)
    c=Stars(n)
    p1=puntajet(a,b,c)
    me="puntaje "+n
    mo="puntaje "+n1
    print (me,p1)
    d=type(n1)
    e=Followers(n1)
    f=Stars(n1)
    p2=puntajet(d,e,f)
    print(mo,p2)

    if p1 < p2:
        return n1
    elif p1>p2:
        return n
    else:
        h="Empate"
        return h

ba=battle(nombre,nombre1)
print ('Ganador:',ba)