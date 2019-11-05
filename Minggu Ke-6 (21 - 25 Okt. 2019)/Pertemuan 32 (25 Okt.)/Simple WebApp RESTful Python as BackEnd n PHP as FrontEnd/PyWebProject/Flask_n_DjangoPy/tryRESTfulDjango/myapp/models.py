from django.db import models
import numpy as np

class Car(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()

class myGA():
    def dec2bin(x):
        return bin(x)[2:] # x int, return as a string
    def bin2dec(x):
        return int(x, 2) # x string, return as a int
    def MyFx(x):
        return ((-np.math.pow(x, 2)) + (14 * x)) - 13;
    def OneCutPointCrossover(x):        
        size=np.shape(x)
        Pop_Size = int(size[0])
        StringLenChromosome = int(size[1])
        hasil= np.empty((2,StringLenChromosome)) # inisialisasi
        hasilcek= np.empty((2,StringLenChromosome)) # inisialisasi

        # // Menentukan PosisiOneCutPoint secara random
        BatasBawahRand = 1; BatasAtasRand = StringLenChromosome - 1
        lower=BatasBawahRand; upper=BatasAtasRand
        mbaris=1;nkolom=1
        PosisiOneCutPoint_init = myGA.myrandint(mbaris,nkolom,lower,upper) # berupa array[1x1]
        PosisiOneCutPoint = int(''.join(map(str,PosisiOneCutPoint_init[0]))) # convert array[1x1] ke scalar
        print("PosisiOneCutPoint= " + str(PosisiOneCutPoint))

        # // memilih 2 parent secara random 
        P1=np.empty((1,StringLenChromosome)) # inisialisasi Parent ke-1
        P2=np.empty((1,StringLenChromosome)) # inisialisasi Parent ke-2
        BatasBawahRand = 0; BatasAtasRand = Pop_Size - 1
        flag = True
        IndexP1 = 0; IndexP2 = 0
        while flag:
            IndexP1=myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
            IndexP2=myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
            if IndexP1 !=IndexP2:
                flag=False

        print("Index P1 = " + str(IndexP1 + 1) + ", Index P2 = " + str(IndexP2 + 1))
        # // menampilkan hasil induk terpilih
        print("P1= ")
        print(x[IndexP1])
        print("")
        print("P2= ")
        print(x[IndexP2])

        # copy array
        P1=x[IndexP1]
        #print(P1)
        hasil[0]=x[IndexP1]
        hasil=hasil.astype(int)
        #print(hasil[0])
        hasilcek[0]=x[IndexP1]
        hasilcek=hasilcek.astype(int)
        #print(hasilcek[0])

        P2=x[IndexP2]
        #print(P2)
        hasil[1]=x[IndexP2]
        #print(hasil[1])
        hasilcek[1]=x[IndexP2]
        #print(hasilcek[1])



        # cara 1 // melakukan proses pindah silang P1 dan P2
        hasil[0,PosisiOneCutPoint:StringLenChromosome]=P2[PosisiOneCutPoint:StringLenChromosome]
        hasil[1,PosisiOneCutPoint:StringLenChromosome]=P1[PosisiOneCutPoint:StringLenChromosome]

        # atau dengan for
        # cara 2 // melakukan proses pindah silang P1 dan P2
        for i in range(PosisiOneCutPoint,StringLenChromosome):
            hasilcek[0][i]=P2[i]
            hasilcek[1][i]=P1[i]

        #print("Cek:")
        #print(hasil)
        #print(hasilcek)

        return hasil,hasilcek
    def RandomMutasi(x):
        size=np.shape(x)
        Pop_Size = int(size[0])
        StringLenChromosome = int(size[1])
        hasil= np.empty((1,StringLenChromosome)) # inisialisasi

        # // Menentukan PosisiPointRandom secara random
        BatasBawahRand = 1; BatasAtasRand = StringLenChromosome      
        PosisiPointRandom = myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
        print("")
        print("PosisiPointRandom= " + str(PosisiPointRandom))

        # // memilih 1 parent secara random 
        P1=np.empty((1,StringLenChromosome)) # inisialisasi 1 Parent
        BatasBawahRand = 0; BatasAtasRand = Pop_Size - 1
        IndexP1 = myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)

        print("Index P1 = " + str(IndexP1 + 1))
        # // menampilkan hasil induk terpilih
        print("P1= ")
        print(x[IndexP1])
        print("")

        # copy array
        P1=x[IndexP1]
        #print(P1)
        hasil=x[IndexP1]
        hasil=hasil.astype(int)
        #print(hasil)

        # // melakukan proses random mutasi
        if(hasil[PosisiPointRandom-1]==0):
            hasil[PosisiPointRandom-1]=1
        else:
            hasil[PosisiPointRandom-1]=0

        print(hasil)
        return hasil
    def myrand(mbaris,nkolom,lower,upper):        
        BatasRANDplusOne=10000
        #mbaris=10
        #nkolom=4
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundary-lower_boundary))+lower_boundary
        #print(normalize_Rand_Sample_minMax)
        #x = normalize_Rand_Sample_minMax
        return normalize_Rand_Sample_minMax
    def myrandint(mbaris,nkolom,lower,upper):        
        BatasRANDplusOne=1000
        #mbaris=10
        #nkolom=4
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundaryinit= 1
        lower_boundaryinit= 0
        randbilrealmulainolsampaisatu=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundaryinit-lower_boundaryinit))+lower_boundaryinit
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax = lower_boundary+(randbilrealmulainolsampaisatu*(upper_boundary-lower_boundary))
        x =np.round(normalize_Rand_Sample_minMax,0)
        x=x.astype(int)
        return x
    def myrandintscalar(lower,upper):        
        BatasRANDplusOne=1000
        mbaris=1
        nkolom=1
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundaryinit= 1
        lower_boundaryinit= 0
        randbilrealmulainolsampaisatu=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundaryinit-lower_boundaryinit))+lower_boundaryinit
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax = lower_boundary+(randbilrealmulainolsampaisatu*(upper_boundary-lower_boundary))
        x =np.round(normalize_Rand_Sample_minMax,0)
        x=x.astype(int)

        ## konversi ke scalar
        # yinit=''.join(str(i) for i in x[0]) # atau dengan
        yinit = ''.join(map(str,x[0]))
        y=int(yinit) # y string, return as a int
        return y