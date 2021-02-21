import random
import names
import math
import time

class Character():
    def __init__(self,name,nationality,tu,power,agility,intellgence,will,health,perception):
        self.name=name
        self.nationality=nationality
        self.tu=tu
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
        deb=weapon_dmg(self.power,self.agility,self.tu)
        js={'name':self.name,'nationality':self.nationality,'power':self.power,'agility':self.agility,'intellgence':self.intellgence,'will':self.will,
        'health':self.health,'hp':self.hp,'perception':self.perception,'base_speed':self.base_speed,'base_action':self.base_action}
        js={**js,**deb}
        return js
def weapon_dmg(power,agility,tu):
    prm={'1k-3':8,'1k-2':9,'1k-2':10,'1k-1':11,'1k-1':12,'1k':13,'1k':14,'1k+1':15,'1k+1':16,'1k+2':17}
    amp={'1k-2':8,'1k-1':9,'1k':10,'1k+1':11,'1k+1':12,'2k-1':13,'2k':14,'2k+1':15,'1k+2':16,'3k-1':17}
    if agility>13:
        skill=random.randint(0,3)
    else:
        skill=random.randint(1,4)
    tu0={'axe':'amp+2','small axe':'amp','throwing axe':'amp+2','loght cudgel':'amp+1 drb','big knife':'amp -2/frw','small knife':'amp-3/frw-1','small stick':'amp drb/frw drb','spear':'frw+2 pen/2hd-frw-3 pen','hammer':'amp+4 drb','staff':'amp+2 drb/frw+1 drb'}
    tu1={'caste':'frw','cudgel':'frw drb','dagger':'frw-1','glefa':'amp+3 cut/frw+3 pen','dart':'frw+1','2hd axe':'amp+2','hair':'amp+2 cut/amp pen','knot':'amp-2(0.5) drb'}
    tu2={'palash':'amp+1 cut/frw+1 drb','cut palash':'amp+1 cut/frw+2 pen','pike':'frw+3 pen','naginata':'amp+2cut/frw+3 pen','short sword':'apm cut/frw pen','long spear':'frw+2 pen/frw+3 pen','tzep':'amp+4 drb'}
    tu3={'cut 2hd sword':'amp+3cut/frw+3 pen'}
    tu4={'small sword':'prm+1 pen'}
    if tu==0:
        arm=tu0
    elif tu==1:
        arm={**tu0, **tu1}
    elif tu==2:
        arm={**tu0, **tu1,**tu2}
    elif tu==3:
        arm={**tu0, **tu1,**tu2,**tu3}
    elif tu==4:
        arm={**tu0, **tu1,**tu2,**tu3,**tu4}
    else:
        arm={'kulak suka':'amp/prm'}
    chose='1k-1'
    for i,a in prm.items():
        if a == power:
            chose=i
    chosey='1k+1'
    for i,a in amp.items():
        if a == power:
            chosey=i
    rand=random.randint(0,len(arm)-1)
    count=-1
    weap={'kulak suka':'amp/prm'}
    for i,a in arm.items():
        count+=1
        if count==rand:
            weap=[i,a]
    #weapon=random.choice(arm.values())
    dbt={'prm':chose,'amp':chosey,'weapon':weap}
    return dbt
def createpers(points,tu):

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
                if i==0:
                    par=random.randint(10,17)
                else:
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
    Boy=Character(name,random.choice(nationality),tu,data[0],data[1],data[2],data[3],data[4],data[5])
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
