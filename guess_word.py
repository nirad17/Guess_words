import time
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i=0
s=""
print("Hey YOU welcome to Word Guessing game!")
time.sleep(1)
name=input("Enter your name:")
time.sleep(2)
check=input("Hi {},do u want to play game now?\nY/N \n".format(name))
if check=="Y" or check=="y":
    print("Ok!\n Let's Start:)\n{}, think of any 5 letter word.".format(name))
    print("Waiting for 10 secs...")
    time.sleep(10)
    print("1 2 3 4 5")
    for k in range(0,26):
        i+=1
        if i%5==0:   
            print(alpha[k])
        else:
            print(alpha[k], end=" ")
    print("\nNow type your 5 digit number cooresponding to the number given to column of alphabet ")
    x1=input()
    print("1 2 3 4 5 6")
    for n in x1:
        if n=="1":
            print("A F K P U Z")
        elif n=="2":
            print("B G L Q V")
        elif n=="3":
            print("C H M R W")
        elif n=="4":
            print("D I N S X")
        elif n=="5":
            print("E J O T Y")

    x2=input("Now type your 5 digit number cooresponding to the number given to column of alphabet\n")
    for i in range(5):
        row=(int(x2[i])-1)*5
        column=row+int(x1[i])-1
        s=s+alpha[column]

    print("Let me think ",name)    
    time.sleep(2)
    print(name,", you guessed '{}'".format(s))
    time.sleep(2)
    print("Thanks for playing !")
    time.sleep(4)
    quit()
else:
    quit()