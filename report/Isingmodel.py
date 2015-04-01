
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

file= open("datanptrial.txt","w")

def neighbor(N,matrix,x,y,kT,que): #code to make a lsit of neighbors if they are not same sign
    neilist=[0,0,0,0]
    neilist[0]= [(x-1)%N,y]
    neilist[1]=[(x+1)%N,y]
    neilist[2]=[x,(y+1)%N]
    neilist[3]=[x,(y-1)%N]
    for k in neilist:
        hor=k[0]
        ver=k[1]
        a=random() 
        b=1- np.exp(-2/kT)
        if matrix[x][y] != matrix[hor][ver] and a < 1- np.exp(-2/kT) :
            matrix[hor][ver] *= -1.0
            que.append(k)
    return matrix , que

def printmatrix(matrix,N):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))
    
def calcmag(matrix,N):
    sum=0
    for horz in range(N):
        for vert in range(N):
            sum += matrix[horz][vert]
    sum=abs(sum)
    float(sum)
    return sum

def calcsus(mlist,tlist):
    sus=[]
    for x in range(len(mlist)-1):
        sus.append((mlist[x+1]-mlist[x])/(tlist[x+1]-tlist[x]))
    return sus

def internalenergy(matrix,N):
    sum=0
    
    for horz in range(N):
        for vert in range(N):
                    sum += -((matrix[horz][vert]*matrix[(horz+1)%(N)][vert])+(matrix[horz][vert]*matrix[horz][(vert-1)%N]))
    float(sum)
    return sum*2.0
def calcspecificheat(elist,tlist):
    specific=[]
    for x in range(len(tlist)-1):
        try:
            specific.append((elist[x+1]-elist[x])/(tlist[x+1]-tlist[x]))
        except ZeroDivisionError:
            print tlist[x+1],tlist[x]
    return specific                
                

 
                                   
def graphmag(temp,mag,error):
    plt.title("Magnatization vs Temperature")
    plt.scatter(temp,mag)
    plt.ylim(0,1.2)
    plt.errorbar(temp,mag,yerr=error, linestyle="None")
    plt.ylabel("Magnatization")
    plt.xlabel("Temperature")
    plt.axhline(y=0,c='k')
    plt.show()
def graphsus(temp,sus):
    plt.title("Susceptibility vs Temperature")
    plt.scatter(temp,sus)
    plt.ylabel("Susceptibility")
    plt.xlabel("Temperature")
    plt.axhline(y=0,c='k')
    plt.show()
def graphenergy(temp,energy,error):
    energy=abs(energy)
    plt.title("Internal Energy vs Temperature")
    plt.scatter(temp,energy)
    plt.errorbar(temp,energy,yerr=error, linestyle="None")
    plt.ylabel("Internal Energy")
    plt.xlabel("Temperature")
    plt.axhline(y=0,c='k')
    plt.show()
def graphspecifichheat(temp,specificheat):
    plt.title("Specific Heat vs Temperature")
    plt.scatter(temp,specificheat)
    plt.ylabel("Specific Heat")
    plt.xlabel("Temperature")
    plt.axhline(y=0,c='k')
    plt.show()
def graphlog(temp,mag,tc):
    for x in temp:
        x += -tc
        x=abs(x)
        x=np.log(x)
    for y in mag:
        y=np.log(y)
    plt.title("Log plot of Magnatization vs Temperature")
    plt.xlim(2,2.5)
    m, b = np.polyfit(temp, mag, 1)
    print m
    plt.ylabel("Log of Magnatization")
    plt.xlabel("Log of Temperature")
    plt.axhline(y=0,c='k')
    plt.scatter(temp,mag)
    plt.plot(temp,m*temp + b,"-")
    plt.show()

def maxclustercalc(kT,N):
    if kT <2:
        return 10
    if 2<=kT< 3.1:
        return 2*N
    else:
        return 2*(N**2)

def writesomething(file,string,list):
        file.write(string)
        file.write("\n")
        for x in list:
            file.write(str(x))
            file.write(" ")
        file.write("\n")
        
def main ():
    tc=2.1
    N=100
    #we will want to loop over temp
    kT=1.5
    max_kT=3.5
    maxsample=10
    sample=0
    h=0
    v=0
    avgmaglist=[]
    energylist=[]
    temp=[]
    sigmamag=[]
    sigmaenergy=[]
  
    while kT < max_kT :
        magforakt=[]
        energyforakt=[]
        maxcluster=maxclustercalc(kT,N)
        #will want to run untill que is empty
        for sample in range(maxsample):
            matrix = [[1.0]*(N) for i in range(N)] #create a N,N matrix
            #if past 2kt use 2N if not use 10
            for cluster in range(maxcluster): #do the wold algoriths a set number of times
                x=randint(0,N-1)
                y=randint(0,N-1)
                que=[]
                matrix[x][y]*= -1.0 #flip a random points sign (add to cluster)
                matrix, que = neighbor(N,matrix,x,y,kT,que) #add neighbors of starting point to a list
                while len(que) != 0: #run this loop untill the que is empty
                    for i in que: #start itirating through que
                        h=i[0]
                        v=i[1]
                        matrix, que = neighbor(N,matrix,h,v,kT,que) #adding its neigbors to the que
                        que.remove(i)
            
            magg= calcmag(matrix,N) #create a list of the sum of the spins after each cycle
            avgmagnum=magg/(N**2)
            magforakt.append(avgmagnum) #create a list of the sum of the spins after each cycle
            energy = internalenergy(matrix,N)
            energyforakt.append(energy)
            print sample
        summ=0
        sume=0
        summ2=0
        np.array(magforakt)
        np.array(energyforakt)

        #for m in magforakt :
         #   summ += m
          #  summ2 += m*m
        #for e in energyforakt :
           # sume += e
        #avgt=summ/len(magforakt)
        #avgm2=summ2/len(magforakt)
        avgmaglist.append(np.mean(magforakt))
        sigmamag.append(np.std(magforakt))
        #avge=sume/len(energyforakt)
        energylist.append(np.mean(energyforakt))
        sigmaenergy.append(np.std(energyforakt))
        temp.append(kT) 
        #standard deviation needs to be put in
       
        print kT

        kT += .07
    
    sus = calcsus(avgmaglist,temp)
    for x in sus:
        abs(x)
        x *= -1
    specificheat = calcspecificheat(energylist,temp)

    graphmag(temp,avgmaglist)
    graphsus(temp[:-1],sus)
    graphspecifichheat(temp[:-1],specificheat)
    graphenergy(temp,energylist)
    graphlog(temp,avgmaglist,tc)

    writesomething(file,"temp",temp)
    writesomething(file,"mag",avgmaglist)
    writesomething(file,"mag sigma",sigmamag)
    writesomething(file,"energy",energylist)
    writesomething(file,"energy sigma",sigmaenergy)
    writesomething(file,"specific",specificheat)
    writesomething(file,"sus",sus)
  
main()



    


            
 