import random
import names
import math
import time

class Character():
    def __init__(self,name,nationality,power,agility,intellgence,will,health,perception):
        self.name=name
        self.nationality=nationality
        self.power=power
        self.agility=agility
        self.intellgence=intellgence
        self.will=will
        self.health=health
        self.hp=power#s
        self.perception=perception
        self.base_speed=(agility+health)/4#s
        self.base_action=self.action()#s
    def action(self):
        n=0
        return math.floor(self.base_speed * 10 ** n) / ( 10 ** n)
    def json(self):
        js={'name':self.name,'nationality':self.nationality,'power':self.power,'agility':self.agility,'intellgence':self.intellgence,'will':self.will,
        'health':self.health,'hp':self.hp,'perception':self.perception,'base_speed':self.base_speed,'base_action':self.base_action}
        return js

def createpers(points):

    default=10
    cost={'power':10,'agility':20,'intellgence':20,'will':5,'perception':5,'health':10}
    while True:
        pow=points*0.7
        pow=round(pow)
        for i in range(5):
            p=pow%5

            if p==0 :
                break

            else: pow-=1


        data=[]
        count=0
        for i in cost.values():
            random.seed(time.time(),version=2)

            if pow>=0:
                par=random.randint(8,15)
                if par>10:
                    eq=par-default
                    cos=i#self.cost[i]
                    pow-=eq*cos
                    count+=1
                elif par<10:
                    eq=default-par
                    cos=i
                    pow+=eq*cos
                    count+=1
                data.append(par)

            else:
                data.append(default)
            #print(pow)
        if count>3 and pow==0:

            break
    name=names.get_first_name()
    nationality=['russian','great ukr','jude','aryan']
    Boy=Character(name,random.choice(nationality),data[0],data[1],data[2],data[3],data[4],data[5])
    return Boy
def createchar():
    random.seed(time.time(),version=2)
    name=names.get_first_name()
    nationality=['russian','great ukr','jude','aryan']
    power=random.randint(8,15)
    if power>=12:
        agility=random.randint(8,12)
    else:
        agility=random.randint(10,14)
    if power+agility>25:
        intellgence=random.randint(8,11)
    else:
        intellgence=random.randint(10,14)
    will=random.randint(8,11)
    health=random.randint(8,12)
    perception=random.randint(8,12)
    Boy=Character(name,random.choice(nationality),power,agility,intellgence,will,health,perception)
    return Boy
#pivo=createchar()
#pivas=createpers(128)
#print(pivas.json())
