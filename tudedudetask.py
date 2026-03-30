while(True):
    score=int(input())
    if score>90 :
        print("Grade=A")
    elif score>79 and score<90 :
        print("Grade=B")
    elif score>69 and score<80:
        print("Grade=C")
    elif score>59 and score<70:
        print("Grade=D")
    else:
        print("Grade=F")
    print("If you want to exit press 0")
    if score==0:
        break


 

