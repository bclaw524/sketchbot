import serial
import sys
import time
import os
import memory as mem
import arr
import move as mov
import static

def start(): 
    
    loop_m=1

    while loop_m==1:
        os.system('cls')
        print "\nSKETCHBOT SOFTWARE VER 2.6"
        print "--------------------------\n"
        print "Enter selection number:\n"
        print "1.)Initialize System\n2.)Test System\n0.)Exit Program\n"
        sel_main=input()
        

        if sel_main==1:
            loop_c1=1
            while loop_c1==1:
                os.system('cls')
                print "Initialize System"
                print "-----------------\n"
                print "Enter selection:"
                print "1.)Initialize Port and Baud rate\n2.)Initialize Legs\n3.)Initialize angle\n4.)Reset Default\n5.)Set to Default Stance\n0.)Back"
                sel_init=input()

                if sel_init==1:
                    print "Initializing port/baud rate"
                    loop_c1=1
                    mem.pab()
                    
                
                elif sel_init==2:
                    print "Initializing legs"
                    mem.leg()
                    loop_c1=1
                    
                elif sel_init==3:
                    print "Initializing motors"
                    mem.angle()
                    loop_c1=1
                elif sel_init==4:
                    print "\nReseting Configuration Values:\n"
                    mem.reset()
                    loop_c1=0
                elif sel_init==5:
                    print "\nReseting Robot Stance:\n"
                    mem.stance()
                    loop_c1=0
                elif sel_init==0:
                    loop_c1=0
                else:
                    print "Unknown input. Enter the selection number"
                    loop_c1=1

                
        elif sel_main==2:
            loop_c2=1
            while loop_c2==1:
                os.system('cls')
                print "Testing System"
                print "--------------\n"
                print "Enter selection:"
                print "1.)Test Joint\n2.)Test Leg\n3.)Test Pattern1\n4.)Test Pattern2\n0.)Back"
                sel_test=input()

                if sel_test==1:
                    print "Initializing Joint Test"
                    loop_c2=1
                    mov.joint()

                elif sel_test==2:
                    print "Initializing Leg Test"
                    loop_c2=1
                    mov.leg()

                elif sel_test==3:
                    print "Initializing Patern Test"
                    loop_c2=1
                    static.pattern1()

                elif sel_test==0:
                    loop_c2=0
                    static.pattern2()           
                                    
                else:
                    print "Unknown input. Enter the selection number"
                    loop_c2=1

        
start()
        
