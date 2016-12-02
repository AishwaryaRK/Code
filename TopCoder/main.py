import sys

# list to find the value of roman numerals
romdig = {
    'v': 5,
    'i': 1,
    'x': 10,
    'l': 50,
    'c': 100,
    'd': 500,
    'm': 1000
}
galalist={} # stores the intergalactic units and their corresponding roman values
metlist={}  # stores the metals and their corresponding values

# function to parse the input lines
def parse(word):
    line=word.lower().split(None)
    if   line[1] == "is": # matching the first kind of input
        key = line[0]
        val = romdig[line[2]]
        galalist.update({key:val})

    elif len(line)==6 and line[5]=="credits": # matching the second kind of input
    #rom1,rom2 indicate the corresponding roman literals
        rom1=galalist[line[0]]
        rom2=galalist[line[1]]
        if rom1<rom2:
            num=rom2-rom1
        else:
            num=rom2+rom1
        metal=line[2]
        metval=int(line[4])/num
        metlist.update({metal:metval})
     #data1,data2,data3,num,num1,num3 are used for mathametical calulations
    elif line[0]=="how" and line[1]=="much" and line[2]=="is": # matching the third kind of input
                data1=galalist[line[3]]
                data2=galalist[line[4]]
                if data1<data2:
                    num1=data2-data1
                else:
                    num1=data2+data1
                data3=galalist[line[5]]
                data4=galalist[line[6]]
                if data3<data4:
                    num2=data4-data3
                else:
                    num2=data4+data3
                answer=num1+num2
                print(line[3:7],'is',answer)

    elif line[0]=="how" and line[1]=="many" and line[2]=="credits": # matching the fourth kind of input
                data1=galalist[line[4]]
                data2=galalist[line[5]]
                data3=metlist[line[6]]
                if data1<data2:
                    num=data2-data1

                else:
                     num=data2+data1
                credit=num*data3
                print(line[4:7],'is',credit,'credits')

    else :
        print("I have no idea what you are talking about")



run= True
while run:
    for line in sys.stdin:
        if line == 'quit\n':
             run = False
             break
        else:
            parse(line)


