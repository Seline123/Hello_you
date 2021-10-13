import time
while True:

    score = 0
    print ("Hello you, I am Seline")
    print ("who are you?")

    time.sleep(2.0)

    username = input("enter name:")

    print("Hello " + username)

    answer1 = "hoeveel huisdieren heb ik?"

    time.sleep(2.0)

    print(answer1)
    print ("a = 0" + " b = 1" + " c = 2")

    time.sleep(2.0)

    answer = input("enter answer:")

    if answer == "b":
        print ("dit is goed, ik heb 1 hond!")
        score += 1

    if answer == "c":
        print ("dit is fout, volgende keer beter")

    if answer == "a":
        print ("dit is fout, volgende keer beter")

    time.sleep(2.0)

    answer2 = "waar woon ik?"


    print(answer2)

    time.sleep(2.0)

    print ("a = Amsterdam" + " b = Haarlem" + " c =  Heemstede")

    time.sleep(2.0)

    answer2 = input("enter answer:")

    if answer2 == "b":
        print ("dit fout, volgende keer beter")

    if answer2 == "a":
        print ("dit is goed. Ik woon in Amsterdam")
        score += 1
    if answer2 == "c":
        print ("dit is fout, volgende keer beter")

    time.sleep(2.0)

    answer2 = "Hoe oud ben ik?"


    print(answer2)

    time.sleep(2.0)

    print ("a = 10 tot en met 14" + " b = 15" + " c =  16 of ouder")

    time.sleep(2.0)

    answer3 = input("enter answer:")

    if answer3 == "a":
        print ("dit is fout, volgende keer beter")

    if answer3 == "c":
        print ("dit is fout, volgende keer beter")

    if answer3 == "b":
        print ("dit is goed. Ik ben 15 jaar oud!")
        score += 1

    time.sleep(2.0)
    print ("your score is:")
    print (score)
    if score == 3:
        print("the perfect score")

    if score == 2:
        print("almost the perfect score, try again")

    if score == 1:
        print("not the worst score, try again")

    if score == 0:
        print("the worst score, try again and see if you have a better score")
    

    if score == 3:
        answer1 = "Waar zit ik op school?"

        time.sleep(2.0)

        print(answer1)
        print ("a = Rotterdam" + " b = Haarlem" + " c = Amsterdam")

        time.sleep(2.0)

        answer = input("enter answer:")

        time.sleep(2)


        if answer == "a":
            print ("dit is fout, volgende keer beter")
            

        if answer == "b":
            print ("dit is fout, volgende keer beter")

        if answer == "c":
            print ("dit is goed, ik zit op het Mediacollege amsterdam")
            score += 1

        print (score)
        if score == 3:
            print ("well done, but you did not reach the top, try again")
        if score == 4:
            print ("well done, you have reached the top")
        
        
        print("Do you want to restart")
        
        answer4 = input("Yes/No:")
        if answer4 == "yes":
            continue

        if answer4 == "No":
            break
        time.sleep(2.0)
    

    print("Do you want to restart")
        
    answer4 = input("Yes/No:")
    if answer4 == "yes":
        continue

    if answer4 == "No":
        break
    time.sleep(2.0)

    
            

   