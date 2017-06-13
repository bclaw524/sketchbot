def init():
    global config
    config = []


def joint_display():

    with open("config.txt", "r") as doc:
        legger=[]
        for line in doc:
            legger.append(line.strip())
            
    print "Servo Port Values"
    print "----------------\n"
    print ("LF: J1-"+legger[3]+" J2-"+legger[4]+" J3-"+legger[5])
    print ("LM: J1-"+legger[6]+" J2-"+legger[7]+" J3-"+legger[8])
    print ("LB: J1-"+legger[9]+" J2-"+legger[10]+" J3-"+legger[11])
    print ("RF: J1-"+legger[12]+" J2-"+legger[13]+" J3-"+legger[14])
    print ("RM: J1-"+legger[15]+" J2-"+legger[16]+" J3-"+legger[17])
    print ("RB: J1-"+legger[18]+" J2-"+legger[19]+" J3-"+legger[20])
    print "----------------\n"
