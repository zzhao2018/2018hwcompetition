def getQuShi(data,TL):
    Len=len(data)
    up=Len
    mid=up-TL
    low=mid-TL
    tlData=[]
    qushi=[]
    if TL<=3:
        return 1
    lastData=data[mid:up]
    lLastData=data[low:mid]
    lastSum=sum(lastData)
    lLastSum=sum(lLastData)
    return float(lastSum)/float(lLastSum)
