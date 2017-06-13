import arr
import os
import sys
import serial
import glob
import time

arr.init()

def load():

    print "loading config"
    global array
    global com_port
    global baud
    global speed
    global l1j1
    global l1j2
    global l1j3 
    global l2j1 
    global l2j2 
    global l2j3 
    global l3j1 
    global l3j2 
    global l3j3 
    global r1j1 
    global r1j2 
    global r1j3 
    global r2j1 
    global r2j2
    global r2j3
    global r3j1
    global r3j2
    global r3j3
    
    with open("config.txt", "r") as doc:
        for line in doc:
            arr.config.append(line.strip())
            
    
    array = arr.config
    com_port=array[0]
    baud=array[1]
    speed=array[2]
    #joint port
    l1j1 = array[3]
    l1j2 = array[4]
    l1j3 = array[5]
    l2j1 = array[6]
    l2j2 = array[7]
    l2j3 = array[8]
    l3j1 = array[9]
    l3j2 = array[10]
    l3j3 = array[11]
    r1j1 = array[12]
    r1j2 = array[13]
    r1j3 = array[14]
    r2j1 = array[15]
    r2j2 = array[16]
    r2j3 = array[17]
    r3j1 = array[18]
    r3j2 = array[19]
    r3j3 = array[20]
    #angle
    l1s1 = array[21]
    l1s2 = array[22]
    l1s3 = array[23]
    l2s1 = array[24]
    l2s2 = array[25]
    l2s3 = array[26]
    l3s1 = array[27]
    l3s2 = array[28]
    l3s3 = array[29]
    r1s1 = array[30]
    r1s2 = array[31]
    r1s3 = array[32]
    r2s1 = array[33]
    r2s2 = array[34]
    r2s3 = array[35]
    r3s1 = array[36]
    r3s2 = array[37]
    r3s3 = array[38]
    doc.close()

def save():

    print "Overwriting Config"    
    with open("config.txt",'w') as doc:
        for x in array:
            doc.write(''.join(x)+'\n')
        

def reset():
    loop_rst=1
    while loop_rst==1:
        print "ARE YOU SURE YOU WANT TO RESET ALL VALUES TO DEFAULT? THIS IS NOT REVERSIBLE.\n IF YES ENTER THE FOLLOWING CODE: 1234"
        conf= input()
        if conf==1234:
            print "reinitializing config"
            with open("default.txt", "r") as doc:
                backup=[]
                for line in doc:
                    backup.append(line.strip())

            with open("config.txt",'w') as doc:
                for x in backup:
                    doc.write(''.join(x)+'\n')

            raw_input( "Done. Press any key to return to previous menu")
            doc.close()
            loop_rst=0
            os.system('cls')
        else:
            loop_rst=0
            raw_input("Reset canceled, Press any key to return to previous menu.")
            
                    
def serial_ports():
    
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result                
                  

def pab(): #initialize port and baud rate
    

    with open("config.txt", "r") as doc:
        pabber=[]
        for line in doc:
            pabber.append(line.strip())
            
    loop_pab=1
    
    while loop_pab ==1:
        os.system('cls')
        print "Initializing Port/Baud"
        print "----------------------\n"
        print "Available Ports: "
        print(serial_ports()) 
        print ("\nCurrent COM: "+pabber[0])
        print ("Current Baud: "+pabber[1])
        print "Enter selection:"
        print "1.)Initialize COM Port\n2.)Initialize baud rate\n0.)Back"
        sel_pab=input()
        os.system('cls')
        
                 

        if sel_pab==1:
            print "\nEnter COM port number (1,2, etc.)"
            pabber[0]=str(raw_input()).upper()
            print("Port initialized as COM"+pabber[0]+"\n")
            loop_pab=1

            with open("config.txt",'w') as doc:
                for x in pabber:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')
                
        elif sel_pab==2:
            print "\nEnter Baud Rate (9600, 14400, etc.)"
            pabber[1]=str(raw_input())
            print("Baud rate initialized as "+pabber[1]+"\n")
            loop_pab=1
            with open("config.txt",'w') as doc:
                for x in pabber:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')
            
        elif sel_pab==0:
            raw_input ("Returning to previous menu. Press any key to continue.")
            loop_pab=0
                        
            
        else:
            raw_input( "Unkonwn entry! Please try again")
            loop_pab=1
            
          
 
           
            

def leg(): #initialize leg pin number
    
    with open("config.txt", "r") as doc:
        legger=[]
        for line in doc:
            legger.append(line.strip())
            
    loop_leg=1
    os.system('cls')
    while loop_leg ==1:

        os.system('cls')
        print "Initialize Leg"
        print "----------------\n"
        print ("LF: J1-"+legger[3]+" J2-"+legger[4]+" J3-"+legger[5])
        print ("LM: J1-"+legger[6]+" J2-"+legger[7]+" J3-"+legger[8])
        print ("LB: J1-"+legger[9]+" J2-"+legger[10]+" J3-"+legger[11])
        print ("RF: J1-"+legger[12]+" J2-"+legger[13]+" J3-"+legger[14])
        print ("RM: J1-"+legger[15]+" J2-"+legger[16]+" J3-"+legger[17])
        print ("RB: J1-"+legger[18]+" J2-"+legger[19]+" J3-"+legger[20])
               
        print "\nChoose Leg to Edit:"
        print "1.)Left Front (LF)\n2.)Left Middle (LM)\n3.)Left Back (LB)\n4.)Right Front (RF)\n5.)Right Middle (RM)\n6.)Right Back (RB)\n0.)Exit"
        sel_leg=input()
        os.system('cls')
               
        if sel_leg==1:
            print "Initializing Left Front (LF):"
            print "\nEnter number for J1 (0-32)"
            legger[3]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[4]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[5]=str(raw_input())
            print("\nLF-J1 set as "+legger[3])
            print("LF-J2 set as "+legger[4])
            print("LF-J3 set as "+legger[5])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==2:
            print "Initializing Left Middle (LM):"
            print "\nEnter number for J1 (0-32)"
            legger[6]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[7]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[8]=str(raw_input())
            print("\nLM-J1 set as "+legger[6])
            print("LM-J2 set as "+legger[7])
            print("LM-J3 set as "+legger[8])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==3:
            print "Initializing Left Back (LB):"
            print "\nEnter number for J1 (0-32)"
            legger[9]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[10]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[11]=str(raw_input())
            print("\nLB-J1 set as "+legger[9])
            print("LB-J2 set as "+legger[10])
            print("LB-J3 set as "+legger[11])
            
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==4:
            print "Initializing Right Front (RF):"
            print "\nEnter number for J1 (0-32)"
            legger[12]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[13]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[14]=str(raw_input())
            print("\nRF-J1 set as "+legger[12])
            print("RF-J2 set as "+legger[13])
            print("RF-J3 set as "+legger[14])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==5:
            print "Initializing Right Middle (RM):"
            print "\nEnter number for J1 (0-32)"
            legger[15]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[16]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[17]=str(raw_input())
            print("\nRF-J1 set as "+legger[15])
            print("RF-J2 set as "+legger[16])
            print("RF-J3 set as "+legger[17])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==6:
            print "Initializing Right Back (RM):"
            print "\nEnter number for J1 (0-32)"
            legger[18]=str(raw_input())
            print "\nEnter number for J2 (0-32)"
            legger[19]=str(raw_input())
            print "\nEnter number for J3 (0-32)"
            legger[20]=str(raw_input())
            print("\nRF-J1 set as "+legger[18])
            print("RF-J2 set as "+legger[19])
            print("RF-J3 set as "+legger[20])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        
        elif sel_leg==0:
            raw_input ("Returning to previous menu. Press any key to continue.")
            loop_leg=0
                        
            
        else:
            raw_input( "Unkonwn entry! Please try again")
            loop_pab=1

def angle(): #initialize default angles of leg
    
    with open("config.txt", "r") as doc:
        legger=[]
        for line in doc:
            legger.append(line.strip())
            
    loop_leg=1
    os.system('cls')
    while loop_leg ==1:

        os.system('cls')
        print "Default Angle:"
        print "----------------\n"
        print ("LF: J1-"+legger[21]+" J2-"+legger[22]+" J3-"+legger[23])
        print ("LM: J1-"+legger[24]+" J2-"+legger[25]+" J3-"+legger[26])
        print ("LB: J1-"+legger[27]+" J2-"+legger[28]+" J3-"+legger[29])
        print ("RF: J1-"+legger[30]+" J2-"+legger[31]+" J3-"+legger[32])
        print ("RM: J1-"+legger[33]+" J2-"+legger[34]+" J3-"+legger[35])
        print ("RB: J1-"+legger[36]+" J2-"+legger[37]+" J3-"+legger[38])
               
        print "\nSet Default Start Angle:"
        print "1.)Left Front (LF)\n2.)Left Middle (LM)\n3.)Left Back (LB)\n4.)Right Front (RF)\n5.)Right Middle (RM)\n6.)Right Back (RB)\n0.)Exit"
        sel_leg=input()
        os.system('cls')
               
        if sel_leg==1:
            print "Initializing Left Front (LF):"
            print "\nEnter number for J1 (500-2000)"
            legger[21]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[22]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[23]=str(raw_input())
            print("\nLF-J1 set as "+legger[21])
            print("LF-J2 set as "+legger[22])
            print("LF-J3 set as "+legger[23])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==2:
            print "Initializing Left Middle (LM):"
            print "\nEnter number for J1 (500-2000)"
            legger[24]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[25]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[26]=str(raw_input())
            print("\nLM-J1 set as "+legger[24])
            print("LM-J2 set as "+legger[25])
            print("LM-J3 set as "+legger[26])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==3:
            print "Initializing Left Back (LB):"
            print "\nEnter number for J1 (500-2000)"
            legger[27]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[28]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[29]=str(raw_input())
            print("\nLB-J1 set as "+legger[27])
            print("LB-J2 set as "+legger[28])
            print("LB-J3 set as "+legger[29])
            
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==4:
            print "Initializing Right Front (RF):"
            print "\nEnter number for J1 (500-2000)"
            legger[30]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[31]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[32]=str(raw_input())
            print("\nRF-J1 set as "+legger[30])
            print("RF-J2 set as "+legger[31])
            print("RF-J3 set as "+legger[32])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==5:
            print "Initializing Right Middle (RM):"
            print "\nEnter number for J1 (500-2000)"
            legger[33]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[34]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[35]=str(raw_input())
            print("\nRF-J1 set as "+legger[33])
            print("RF-J2 set as "+legger[34])
            print("RF-J3 set as "+legger[35])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        elif sel_leg==6:
            print "Initializing Right Back (RM):"
            print "\nEnter number for J1 (500-2000)"
            legger[36]=str(raw_input())
            print "\nEnter number for J2 (500-2000)"
            legger[37]=str(raw_input())
            print "\nEnter number for J3 (500-2000)"
            legger[38]=str(raw_input())
            print("\nRF-J1 set as "+legger[36])
            print("RF-J2 set as "+legger[37])
            print("RF-J3 set as "+legger[38])
            loop_leg=1

            with open("config.txt",'w') as doc:
                for x in legger:
                    doc.write(''.join(x)+'\n')
            raw_input( "Done. Press Enter to continue")
            os.system('cls')

        
        elif sel_leg==0:
            raw_input ("Returning to previous menu. Press any key to continue.")
            loop_leg=0
                        
            
        else:
            raw_input( "Unkonwn entry! Please try again")
            loop_pab=1

def stance(): #force robot to default stance

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())


    portno='COM'+str(jointer[0])
    baud=jointer[1]
    spd=jointer[2]
    scr=serial.Serial(portno,baud)
    
    fwd=[]
    for f in range(6):
        fwd.append(0)
                    
   
    print ("Running Default Leg Position")
                
                
    fwd[0]='#'+str(jointer[3])+'P'+str(jointer[21])+'#'+str(jointer[4])+'P'+str(jointer[22])+'#'+str(jointer[5])+'P'+str(jointer[23])+'S'+spd
    fwd[1]='#'+str(jointer[6])+'P'+str(jointer[24])+'#'+str(jointer[7])+'P'+str(jointer[25])+'#'+str(jointer[8])+'P'+str(jointer[26])+'S'+spd
    fwd[2]='#'+str(jointer[9])+'P'+str(jointer[27])+'#'+str(jointer[10])+'P'+str(jointer[28])+'#'+str(jointer[11])+'P'+str(jointer[29])+'S'+spd
    fwd[3]='#'+str(jointer[12])+'P'+str(jointer[30])+'#'+str(jointer[13])+'P'+str(jointer[31])+'#'+str(jointer[14])+'P'+str(jointer[32])+'S'+spd
    fwd[4]='#'+str(jointer[15])+'P'+str(jointer[33])+'#'+str(jointer[16])+'P'+str(jointer[34])+'#'+str(jointer[17])+'P'+str(jointer[35])+'S'+spd
    fwd[5]='#'+str(jointer[18])+'P'+str(jointer[36])+'#'+str(jointer[19])+'P'+str(jointer[37])+'#'+str(jointer[20])+'P'+str(jointer[38])+'S'+spd
                        
                               

    i=int(0)
    print "Complete in..."
    for x in range(0,6):
        j=5-i
        print str(j)            
        scr.write(fwd[i]+'\r')
        time.sleep(1)
                        
        i=i+1
                    

    raw_input("Done. Press Enter to continue.")
        
    scr.close()
    os.system('cls')
