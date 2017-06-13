import arr
import os
import sys
import serial
import time
import memory as mem



def forward(val):

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
    doc.close()
    rate=int(val)*10
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)

    for x in range(0,1):
        ang1=int(jointer[21])-rate
        ang2=int(jointer[24])
        ang3=int(jointer[27])-rate
        ang4=int(jointer[30])+rate
        ang5=int(jointer[33])
        ang6=int(jointer[36])+rate

        jointer[21]=str(ang1)
        jointer[24]=str(ang2)
        jointer[27]=str(ang3)
        jointer[30]=str(ang4)
        jointer[33]=str(ang5)
        jointer[36]=str(ang6)
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6

        scr.write(cmd+'\r')
                
        
        
        with open("config.txt",'w') as doc:
            for x in jointer:
                doc.write(''.join(x)+'\n')
                
    scr.close()            
    doc.close() 


def reverse(val):

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
    doc.close()
    rate=int(val)*10
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)

    for x in range(0,1):
        ang1=int(jointer[21])+rate
        ang2=int(jointer[24])
        ang3=int(jointer[27])+rate
        ang4=int(jointer[30])-rate
        ang5=int(jointer[33])
        ang6=int(jointer[36])-rate

        jointer[21]=str(ang1)
        jointer[24]=str(ang2)
        jointer[27]=str(ang3)
        jointer[30]=str(ang4)
        jointer[33]=str(ang5)
        jointer[36]=str(ang6)
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6

    
        scr.write(cmd+'\r')
                
        
    
    with open("config.txt",'w') as doc:
               for x in jointer:
                   doc.write(''.join(x)+'\n')
    doc.close()
    scr.close()

def right(val):

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
    doc.close()
    rate=300
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)

    for x in range(0,1):
        ang1=int(jointer[21])-rate
        ang2=int(jointer[24])
        ang3=int(jointer[27])+rate
        ang4=int(jointer[30])-rate
        ang5=int(jointer[33])
        ang6=int(jointer[36])+rate

        jointer[21]=str(ang1)
        jointer[24]=str(ang2)
        jointer[27]=str(ang3)
        jointer[30]=str(ang4)
        jointer[33]=str(ang5)
        jointer[36]=str(ang6)
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6

    
        scr.write(cmd+'\r')
                
        
    
    with open("config.txt",'w') as doc:
               for x in jointer:
                   doc.write(''.join(x)+'\n')
    doc.close()
    scr.close()

def left(val):

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
    doc.close()
    rate=int(val)*10
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)

    for x in range(0,1):
        ang1=int(jointer[21])+rate
        ang2=int(jointer[24])
        ang3=int(jointer[27])-rate
        ang4=int(jointer[30])+rate
        ang5=int(jointer[33])
        ang6=int(jointer[36])-rate

        jointer[21]=str(ang1)
        jointer[24]=str(ang2)
        jointer[27]=str(ang3)
        jointer[30]=str(ang4)
        jointer[33]=str(ang5)
        jointer[36]=str(ang6)
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6

    
        scr.write(cmd+'\r')
                
        
    
    with open("config.txt",'w') as doc:
               for x in jointer:
                   doc.write(''.join(x)+'\n')
    doc.close()
    scr.close()

def stepl():

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
    doc.close()
    
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)

    i=0
    lf1 =[1500,1500,1800,1800]
    lf2 =[1800,2200,2200,1800]
    lf3 =[1850,2000,2000,1850]
    
    for i in range(0,4):
        ang1=lf1[i]
        ang2=lf2[i]
        ang3=lf3[i]
        

        jointer[21]=str(ang1)
        jointer[22]=str(ang2)
        jointer[23]=str(ang3)
       
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6

    
        scr.write(cmd+'\r')
        
        time.sleep(0.5)
                
        
    
    with open("config.txt",'w') as doc:
               for x in jointer:
                   doc.write(''.join(x)+'\n')
    doc.close()
    scr.close()

def stepr():

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
            
    doc.close()
    
    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)
    i=0
    lf1 =[1300,1300,1600,1600]
    lf2 =[1800,2200,2200,1800]
    lf3 =[1600,1600,1600,1600]
    
    for i in range(0,4):
        ang1=lf1[i]
        ang2=lf2[i]
        ang3=lf3[i]
        

        jointer[27]=str(ang1)
        jointer[28]=str(ang2)
        jointer[29]=str(ang3)
       
    
        fwd1='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])
        fwd2='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])
        fwd3='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])
        fwd4='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])
        fwd5='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])
        fwd6='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
    
        cmd=fwd1+fwd2+fwd3+fwd4+fwd5+fwd6
        
    
        scr.write(cmd+'\r')
        
        time.sleep(0.5)
                
        
    
    with open("config.txt",'w') as doc:
               for x in jointer:
                   doc.write(''.join(x)+'\n')
    doc.close()
    scr.close()

def pattern1():

    print("Clockwise Square\n")
    print "Enter desired value (0-30): "
    get=input()

    forward(get)
    time.sleep(2)
    right(get)
    time.sleep(2)
    reverse(get)
    time.sleep(2)
    left(get)

    raw_input("Done. Press any enter to continue")

def pattern2():

    print("Counter Clockwise Square\n")
    print "Enter desired value (0-30): "
    get=input()

    reverse(get)
    time.sleep(2)
    right(get)
    time.sleep(2)
    forward(get)
    time.sleep(2)
    left(get)

    raw_input("Done. Press any enter to continue")
