'''
Number Decorator (numdeco)
Author : Rishi Kumar S
'''

def deco(k=0):
    # deco with suffix T(trillion), B(billion), M(million), K
    try :
        if k > 999999999999:
            print(str(k)[:-12]+'T '+str(k)[-12:-9]+'B '+str(k)[-9:-6]+'M '+str(k)[-6:-3]+'K '+str(k)[-3:])
        elif k > 999999999:
            print(str(k)[:-9]+'B '+str(k)[-9:-6]+'M '+str(k)[-6:-3]+'K '+str(k)[-3:])
        elif k > 999999:
            print(str(k)[:-6]+'M '+str(k)[-6:-3]+'K '+str(k)[-3:])
        elif k > 999:
            print(str(k)[:-3]+'K '+str(k)[-3:])
        elif k > 99:
            print(str(k)[:-3]+'0.'+str(k)[-3]+'K')
        elif k > 9:
            print(str(k)[:-2]+'0.0'+str(k)[-2]+'K')
        else:
            print(str(k))

    except :
        print('Error!! Enter only numbers')


def decoco(k=0):
    # decoco with suffix Commas(,)
    try :
        if k > 999999999999:
            print(str(k)[:-12]+','+str(k)[-12:-9]+','+str(k)[-9:-6]+','+str(k)[-6:-3]+','+str(k)[-3:])
        elif k > 999999999:
            print(str(k)[:-9]+','+str(k)[-9:-6]+','+str(k)[-6:-3]+','+str(k)[-3:])
        elif k > 999999:
            print(str(k)[:-6]+','+str(k)[-6:-3]+','+str(k)[-3:])
        elif k > 999:
            print(str(k)[:-3]+','+str(k)[-3:])
        elif k > 99:
            print(str(k)[:-3]+'0.'+str(k)[-3:])
        elif k > 9:
            print(str(k)[:-2]+'0.0'+str(k)[-2:])
        else:
            print(str(k))

    except :
        print('Error!! Enter only numbers')

# Indian version

def indeco(k=0):
    # deco with suffix C(Crore), L(Lakhs), T(Thousand)
    try :
        if k > 9999999:
            print(str(k)[:-7]+'C '+str(k)[-7:-5]+'L '+str(k)[-5:-3]+'T '+str(k)[-3:])
        elif k > 999999:
            print(str(k)[:-5]+'L '+str(k)[-5:-3]+'T '+str(k)[-3:])
        elif k > 99999:
            print(str(k)[:-5]+'L '+str(k)[-5:-3]+'T '+str(k)[-3:])
        elif k > 999:
            print(str(k)[:-3]+'T '+str(k)[-3:])
        elif k > 99:
            print(str(k)[:-3]+'0.'+str(k)[-3]+'T')
        elif k > 9:
            print(str(k)[:-2]+'0.0'+str(k)[-2]+'T')
        else:
            print(str(k))

    except :
        print('Error!! Enter only numbers')
        
def indecoco(k=0):
    # indecoco with suffix Commas(,)
    try :
        if k > 9999999:
            print(str(k)[:-7]+','+str(k)[-7:-5]+','+str(k)[-5:-3]+','+str(k)[-3:])
        elif k > 999999:
            print(str(k)[:-5]+','+str(k)[-5:-3]+','+str(k)[-3:])
        elif k > 99999:
            print(str(k)[:-5]+','+str(k)[-5:-3]+','+str(k)[-3:])
        elif k > 999:
            print(str(k)[:-3]+','+str(k)[-3:])
        elif k > 99:
            print(str(k)[:-3]+'0.'+str(k)[-3:])
        elif k > 9:
            print(str(k)[:-2]+'0.0'+str(k)[-2:])
        else:
            print(str(k))

    except :
        print('Error!! Enter only numbers')
