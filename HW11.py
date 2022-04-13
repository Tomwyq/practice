# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:33:23 2022

@author: User
"""
#1
def WhoAmI():
    return('yw3696')
WhoAmI()

# getBondPrice
def getBondPrice(y, face, couponRate, m, ppy):
    cf = couponRate*face/ppy
    pvsum = 0
    for t in range(1,(m*ppy)+1):
        if t == (m*ppy):
            cf += face
        pv = (1+(y/ppy))**(-t)
        pvcf = pv*cf
        pvsum += pvcf
        
    bondPrice = pvsum 
    return(bondPrice)

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
getBondPrice(y, face, couponRate, m, ppy)


#getBondDuration
def getBondDuration(y, face, couponRate, m, ppy):
    cf = couponRate*face/ppy
    pvsum = 0
    pvtsum = 0
    for t in range(1,(m*ppy)+1):
        if t == (m*ppy):
            cf += face
            
        pv = (1+(y/ppy))**(-t)
        pvcf = pv*cf
        pvtcf = pv*cf*t
        pvsum += pvcf
        pvtsum += pvtcf

    bondPrice = pvsum 
    bondDuration = (pvtsum/bondPrice)/ppy
    return(bondDuration)

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
getBondDuration(y, face, couponRate, m, ppy)

# getBondPrice_E
def getBondPrice_E(face, couponRate, m, yc):
    cf = couponRate*face
    pvsum = 0
    for (t,x) in enumerate(yc):
        if (t+1) == m:
            cf += face

        pv = (1+x)**(-(t+1))
        pvcf = pv*cf
        pvsum += pvcf

    bondPrice = pvsum 
    return(bondPrice)

# Test values
yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5
getBondPrice_E(face, couponRate, m, yc)

# getBondPrice_Z
def getBondPrice_Z(face, couponRate, times, yc):
    cf = couponRate*face
    pvsum = 0
    for (t,x) in zip(times,yc):
        if t == times[4]:
            cf += face

        pv = (1+x)**(-t)
        pvcf = pv*cf
        pvsum += pvcf


    bondPrice = pvsum 
    return(bondPrice)

# Test values
yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04
getBondPrice_Z(face, couponRate, times, yc)

# fizz buzz
def FizzBuzz(start, finish):
    outlist = []
    for i in range(start,finish+1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append('fizzbuzz')
        elif i % 5 == 0:
            outlist.append('buzz')
        elif i % 3 == 0 :
            outlist.append('fizz')
        else:
            outlist.append(i)
    return(outlist)

FizzBuzz(15, 30)