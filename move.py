import arr
import os
import sys
import serial
import time
import memory as mem


def joint():

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())

    

    cur= "None"
    jt_ok=0
    ser=99
    loop_joint=1
    spd=jointer[2]
    pos=1500
    
    while loop_joint==1:
        os.system('cls')

        arr.joint_display()
        print "Joint Testing"
        print ("Selected Joint: "+cur)
        print ("jt_ok: "+str(jt_ok))
        print ("Selected Speed: "+spd)
        print "\nEnter Selection:"
        print "1.)Select Joint\n2.)Set Speed\n3.)Run Sweep\n4.)Test joint\n0.)Back"
        sel_joint=input()
        os.system('cls')

        if sel_joint==1:
            print ("Joint Selection. Currenlty set as: "+cur)
            print "Enter Leg (LF,LM,LB,RF,RM,RB)"
            l=raw_input().upper()
            print "Enter Joint(J1, J2, J3)"
            j=raw_input().upper()
            cur=l+j
            
            if cur == 'LFJ1':
                ser=jointer[3]
                jt_ok=1
            elif cur == 'LFJ2':
                ser=jointer[4]
                jt_ok=1
            elif cur == 'LFJ3':
                ser=jointer[5]
                jt_ok=1
            elif cur == 'LMJ1':
                ser=jointer[6]
                jt_ok=1
            elif cur == 'LMJ2':
                ser=jointer[7]
                jt_ok=1
            elif cur == 'LMJ3':
                ser=jointer[8]
                jt_ok=1
            elif cur == 'LBJ1':
                ser=jointer[9]
                jt_ok=1
            elif cur == 'LBJ2':
                ser=jointer[10]
                jt_ok=1
            elif cur == 'LBJ3':
                ser=jointer[11]
                jt_ok=1
            elif cur == 'RFJ1':
                ser=jointer[12]
                jt_ok=1
            elif cur == 'RFJ2':
                ser=jointer[13]
                jt_ok=1
            elif cur == 'RFJ3':
                ser=jointer[14]
                jt_ok=1
            elif cur == 'RMJ1':
                ser=jointer[15]
                jt_ok=1
            elif cur == 'RMJ2':
                ser=jointer[16]
                jt_ok=1
            elif cur == 'RMJ3':
                ser=jointer[17]
                jt_ok=1
            elif cur == 'RBJ1':
                ser=jointer[18]
                jt_ok=1
            elif cur == 'RBJ2':
                ser=jointer[19]
                jt_ok=1
            elif cur == 'RBJ3':
                ser=jointer[20]
                jt_ok=1
            if jt_ok==1:                
                raw_input ("Joint "+cur+" selected. Press any button to continue.")
                os.system('cls')
            else:
                raw_input("Joint not selected!")

        elif sel_joint==2:
            print ("Speed currenlty set as: "+spd)
            print "Enter speed (0-1500):"
            spd=raw_input()
            raw_input ("Done, speed set as "+spd+". Press any button to continue.")
            os.system('cls')

        elif sel_joint==3:

            if jt_ok==0:
                raw_input("LEG NOT SELECTED! PLEASE ENTER A USABLE LEG")
                os.system('cls')
            else:
                test_run=1

                portno='COM'+str(jointer[0])
                baud=jointer[1]
                scr=serial.Serial(portno,baud)
            
                while test_run==1:
                    print "Testing angle of joint "+cur+" at "+spd+"ms"
                    ang=str(raw_input("Please enter desired angle (500-2000):"))
                    cmd='#'+str(ser)+'P'+str(ang)+'S'+spd
                    scr.write(cmd+'\r')
                    time.sleep(1)
                    chk=raw_input("Press enter to insert new angle or N to exit").upper()
                    if chk=='N':
                        test_run=0
                        scr.close()
                    os.system('cls')

        
                
        elif sel_joint==0:
            raw_input ("Returning to previous menu. Press any key to continue.")
            loop_joint=0
        
        else:
            raw_input( "Unkonwn entry! Please try again")       
                                
def leg():

    with open("config.txt", "r") as doc:
        jointer=[]
        for line in doc:
            jointer.append(line.strip())
            
    cur= "None"        
    loop_leg=1
    leg_ok=0
    ser1=99
    ser2=99
    ser3=99
    spd=jointer[2]
    
    while loop_leg==1:
        os.system('cls')
        print "Leg Testing"
        print "WARNING! ENSURE SUFFICIENT SPACE FOR TEST"
        print ("Selected Leg: "+cur)
        print "\nEnter Selection:"
        print "1.)Select Leg\n2.)Set individual angles\n3.)Single Leg Sweep\n0.)Back"
        sel_leg=input()
        os.system('cls')
                
        
        if sel_leg==1:
            print ("Joint Selection. Currenlty set as: "+cur)
            print "Enter Leg (LF,LM,LB,RF,RM,RB)"
            cur=raw_input().upper()
            
            if   cur == 'LF':
                ser1=jointer[3]
                ser2=jointer[4]
                ser3=jointer[5]
                leg_ok=1
            elif cur == 'LM':
                ser1=jointer[6]
                ser2=jointer[7]
                ser3=jointer[8]
                leg_ok=1
            elif cur == 'LB':
                ser1=jointer[9]
                ser2=jointer[10]
                ser3=jointer[11]
                leg_ok=1
            elif cur == 'RF':
                ser1=jointer[12]
                ser2=jointer[13]
                ser3=jointer[14]
                leg_ok=1
            elif cur == 'RM':
                ser1=jointer[15]
                ser2=jointer[16]
                ser3=jointer[17]
                leg_ok=1
            elif cur == 'RB':
                ser1=jointer[18]
                ser2=jointer[19]
                ser3=jointer[20]
                leg_ok=1
            else:
                raw_input("Unknown Entry!")

            if leg_ok==1:
                raw_input("Leg "+cur+" selected.")
            
            os.system('cls')


        elif sel_leg==2:
            test_run=1

            portno='COM'+str(jointer[0])
            baud=jointer[1]
            scr=serial.Serial(portno,baud)
            
            while test_run==1:
                print ("Testing movement of leg "+cur)
                ang1=str(raw_input("Please enter desired angle for J1(500-2000):"))
                cmd1='#'+str(ser1)+'P'+str(ang1)
                ang2=str(raw_input("Please enter desired angle for J2(500-2000):"))
                cmd2='#'+str(ser2)+'P'+str(ang2)
                ang3=str(raw_input("Please enter desired angle for J3(500-2000):"))
                cmd3='#'+str(ser3)+'P'+str(ang3)+'S'+spd

                command=cmd1+cmd2+cmd3

                
                scr.write(command+'\r')
                time.sleep(2)
                chk=raw_input("Press enter to insert new angle or N to exit: ").upper()
                if chk=='N':
                    test_run=0
                    scr.close()
                os.system('cls')
                

        elif sel_leg==3:

            if leg_ok==0:
                raw_input("LEG NOT SELECTED! PLEASE ENTER A USABLE LEG")
                os.system('cls')
                
            elif leg_ok==1:
                test_run=1
                portno='COM'+str(jointer[0])
                baud=jointer[1]
                scr=serial.Serial(portno,baud)

                while test_run==1:
                    print ("Testing movement of leg "+cur)
                    ang1=str(raw_input("Please enter desired MAX angle (500-2000):"))
                    ang2=str(raw_input("Please enter desired MIN angle (500-2000):"))
                    cmd1='#'+str(ser1)+'P'+str(ang1)
                    cmd2='#'+str(ser2)+'P'+str(ang1)
                    cmd3='#'+str(ser3)+'P'+str(ang1)+'S'+spd
                    command1=cmd1+cmd2+cmd3
                    cmd1='#'+str(ser1)+'P'+str(ang2)
                    cmd2='#'+str(ser2)+'P'+str(ang2)
                    cmd3='#'+str(ser3)+'P'+str(ang2)+'S'+spd
                    command2=cmd1+cmd2+cmd3
                
                    for x in range(0,3):
                        scr.write(command1+'\r')
                        time.sleep(2)
                        scr.write(command2+'\r')
                        time.sleep(2)

                    chk=raw_input("Press enter to insert new angle or N to exit: ").upper()
                    if chk=='N':
                        test_run=0
                        scr.close()
                    os.system('cls')  
            


        

        elif sel_leg==0:
            raw_input ("Returning to previous menu. Press any key to continue.")
            loop_leg=0

        else:
                raw_input("Unknown Entry!")


    
        
  
  
          
    
