def getNextState(S0, mul, mod, inc):
    return(mul*S0 + inc)% mod

def getInc(S0, S1, mul, mod):
    return ((S1 -((S0* mul)% mod))+ mod)

def getMul(firstStateDiff,secondStateDiff, mod ):
    if secondStateDiff ==0 :
        return 0
    
    if firstStateDiff< 0:
        firstStateDiff = -firstStateDiff
        secondStateDiff = - secondStateDiff
    
    secondStateDiff %= mod

    while firstStateDiff > mod:
        firstStateDiff -= mod

    return(mod * getMul(mod, -secondStateDiff, firstStateDiff ) + secondStateDiff )//firstStateDiff
mul = getMul(1617562532769340-2688456964915964,
            2688456964915964-2557694464258732, 
            3173287219423490 )

inc = getInc(2688456964915964,2557694464258732, mul, 3173287219423490 )

state4 = getNextState(2557694464258732, mul ,3173287219423490,inc)

print('multiplicador: ',mul)
print('incremento: ',inc)
print('estado 4: ',state4)