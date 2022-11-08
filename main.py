#Variables
max = 1000000000
min = 1000

#Lists
seqs = []

#Generator
def gen():
    
    #declaring global variables
    global min,max,seqs

    #while loop
    while(min <= max):
        
        #local variables
        seq = str(min)
        x = 0
        sus = False
        p_n = ""
        tem = []

        #for loop
        for n in seq:

            #rules
            #-->no zeroes
            if(n == "0"):                        
                sus = True
                break
            #-->no repitions
            elif(n in tem):                      
                sus = True
                break
            elif(x > 0):
            #-->checks for middle dot
                if(int(n) == 5 or int(p_n) == 5):
                        pass
            #-->checks for consecutive numbers 
                elif((int(n)+int(p_n))%2 == 1):  
                    pass
            #-->checks for even numbers
                elif(int(n)%2 == 0 and int(p_n)%2 == 0):
                    tem1 = int((int(n)+int(p_n))*0.5)
                    if(tem1 == 5 and "5" in tem):
                        pass
                    elif(tem1 != 5):
                        pass
                    else:
                        sus = True
                        break
            #-->checks for odd numbers 
                elif(int(n)%2 == 1 and int(p_n)%2 == 1):                        
                    tem1 = int((int(n)+int(p_n))*0.5)
                    if(str(tem1) in tem):        
                        pass
                    else:
                        sus = True
                        break 
                else:
                    sus = True
                    break
            else:
                pass    
            tem.append(n)
            p_n = n
            x+=1

        if sus == False:
            seqs.append(seq)
            print(f"{round((min/max)*100,2)}"+"%")
        min += 1

#generates all the possible sequences/patterns
gen()
print("sequencing complete")

# saving the patterns
with open(f"output/_{len(seqs)} patterns.txt","w") as output:
    for n in seqs:
        output.write(f"{n} \n")
print(f"number of patterns found : {len(seqs)}")
