import time
import datetime
import copy
import math

def getDateLength(beginData,endData):
    beginT=time.strptime(beginData,'%Y-%m-%d')
    lastT=time.strptime(endData,'%Y-%m-%d')
    dateB=datetime.datetime(beginT[0],beginT[1],beginT[2])
    dateL=datetime.datetime(lastT[0],lastT[1],lastT[2])
    return int(str(dateL-dateB).split()[0])




#get num of date,put data in the list
def getParameterData(data,dataList):
    paraData=[]
    for ele in dataList:
        paraData.append(data[ele])
    return paraData

#get u
def getU(data):
    u=0.0
    for e in data:
        u+=e
    u=float(u)/float(len(data))
    return u

#get theta
def getTheta(data,u):
    theta=0
    L=len(data)
    if L<=1:
        return 0
    for e in data:
        theta+=(e-u)**2
    theta=math.sqrt(theta/(L-1))
    return theta

#test if the date is normal
def testNormal(x,u,theta):
    if x>2 and abs(x-u)>3*theta:
        x=int(u)+1
    return x

#get all the day
def getAllData(data,dateB,dateL):
    #begin fill date
    while dateB<=dateL:
        date=str(dateB).split()[0]
        if date not in data:
            data[date]=0
        dateB=dateB+datetime.timedelta(days=1)

#split the date to some part
def splitDateList(Y,loc,Len):
    l=0
    data=[]
    allLen=len(Y)
    while l<Len:
        if (loc+l)>=allLen:
            break
        data.append(Y[loc+l])
        l+=1
    return data


#deal unnormal data
def dealUnnormalDate(copyData,newList,inputL,Len):
    #deal unnormal data
    L=len(newList)
    for ele in inputL:
        Y=getParameterData(copyData[ele],newList)
        loc=0
        newData=[]
        while loc<L:
            #get u and theta
            splitData=splitDateList(Y,loc,Len)
            u=getU(splitData)
            theta=getTheta(splitData,u)
#            print u
#            print theta
#            print max(int(u+3*theta),2)
#            print splitData
            #normal the date
            LL=len(splitData)
            for i in range(LL):
                splitData[i]=testNormal(splitData[i],u,theta)
#            print splitData
#            print '*'*50
            #update newData
            newData.extend(splitData)
            loc+=Len
        #updata dict
        for e1,e2 in zip(newData,newList):
            copyData[ele][e2]=e1
        

#deal the data
def getDealData(data,dateList,inputL):
    copyData=copy.deepcopy(data)
    #deal date
    beginT=time.strptime(dateList[0],'%Y-%m-%d')
    lastT=time.strptime(dateList[-1],'%Y-%m-%d')
    dateB=datetime.datetime(beginT[0],beginT[1],beginT[2])
    dateL=datetime.datetime(lastT[0],lastT[1],lastT[2])
    #get all data
    for ele in inputL:
        getAllData(copyData[ele],dateB,dateL)
    #get dateList
    newList=[]
     #begin fill dateList
    while dateB<=dateL:
        date=str(dateB).split()[0]
        newList.append(date)
        dateB=dateB+datetime.timedelta(days=1)
    #deal the unnormal data
    dealUnnormalDate(copyData,newList,inputL,20)
    return copyData,newList
    
