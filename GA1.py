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

def swap(a,b):
    tmp = a
    a = b
    b = tmp

class Node: #Luu tung ca the va he so Fitness
    def __init__(self,data,fitness):
        self.data=data
        self.fitness=fitness

def Input():
    a=float(input())
    b=float(input())
    c=float(input())
    accu=float(input('Nhap do chinh xac: '))
    return a, b, c, accu

class Genetic:
    def __init__(self):
        self.a, self.b, self.c, self.accu = Input()
        self.arr=[]

    def getFitness(self, x): #ham thich nghi
        return abs(self.a*(x**2)+self.b*x+self.c)

    def push(self,item):# Them mot ca the va sap xep cac ca the tang dan vao mang
        for i in range(len(self.arr)):
            if self.arr[i].fitness> item.fitness:
                self.arr.insert(i,item)
                return
        self.arr.append(item)   


    
    def population(self, Range): #ham chon quan the
        m=float(-self.b/(2*self.a)+Range) #chan tren
        n=float(-m) #chan duoi
        if m==0:
            m=m+10
            n=n+10
        for i in range(100): #Chon 100 ca the
            x=float(random.uniform(m,n))
            self.push(Node(x,self.getFitness(x)))
            if self.arr[i].fitness<=self.accu:
                print(x)
                return
    
    def exit(self):
        for i in range(100): 
            if self.arr[i].fitness<=self.accu:
                print(self.arr[i].data)
                return True
        return False

    def mate(self): #lai ghep
        newPopulation=[]
        for i in range(50):
            x = self.arr[random.randrange(0,50)]
            y = self.arr[random.randrange(0,50)]
            midPoint = random.randrange(0,64)
            x1=float_to_bin(x.data)
            y1=float_to_bin(y.data)
            for i in range(midPoint):   # Lai cheo 2 day bit
                swap(x1[i],y1[i])
            newPopulation.append(Node(bin_to_float(x1),0))
            newPopulation.append(Node(bin_to_float(y1),0))
        for i in range(100):
            self.arr[i] = newPopulation[i]
            self.arr[i].fitness = self.getFitness(self.arr[i].data)
    

    def run(self):
        Range = 50
        self.population(Range)
        generations = 0
        while(self.exit() == False):
            self.mate()
            generations += 1
            if(generations > 20): #neu vuot qua 20 doi con thi dot bien
                Range += 50
                self.population(Range)
            for i in range(100):
                print(self.arr[i].data)
genetic = Genetic()
genetic.run()