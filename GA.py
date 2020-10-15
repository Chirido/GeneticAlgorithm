import random
from codecs import decode
import struct
# def float_to_bin(num):
#     return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

# def bin_to_float(binary):
#     return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack('>d', bf)[0]


def int_to_bytes(n, length):  # Helper function
    """ Int/long to byte string.
        Python 3.2+ has a built-in int.to_bytes() method that could be used
        instead, but the following works in earlier versions including 2.x.
    """
    return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]


def float_to_bin(value):  # For testing.
    """ Convert float to 64-bit binary string. """
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return '{:064b}'.format(d)

def Fitness(a,b,c,x): #ham thich nghi
    return abs(a*(x**2)+b*x+c)

def swap(a,b):
    t=a
    a=b
    b=t

def mate(a,b): #Lai ghep hai ca the
    x=float_to_bin(a)
    y=float_to_bin(b)
    



#a*x^2+b*x+c
a=float(input())
b=float(input())
c=float(input())
acc=float(input()) #Nhap do chinh xac
print('Do chinh xac: ',acc)
m=float(-b/2+100) #chan duoi
n=float(-m) #chan tren
if m==0:
    m=m+1
    n=n-1

def Genetic(m,n):
    result=0.0
    ex=[]
    fit=[]
    for i in range(100):
        ex.append(float(random.uniform(m,n))) #Chọn quần thể
        fit.append(float(Fitness(a,b,c,ex[i]))) #Tinh do thich nghi
        if fit[i]<=acc: #Neu ca the co do chinh xac nho hon hoac bang do chinh xac da cho thi lay
            result=ex[i]
            break

    if result!=0.0:
        print(result)
    else: #Sap xep quan the theo thu tu tang dan do thich nghi
        for i in fit-1:
            j=i+1
            for j in fit:
                if fit[j]<fit[i]:
                    swap(fit[j],fit[i])
                    swap(ex[j],ex[i])
    
    choose=[]
    for i in range(50): #Chon 50 ca the tot nhat de lai ghep
        choose[i]=ex[i]
    
    






    
    




