questions = {"who used to call you when nobody was calling you: ":"A",
             "what do you see when u see a big bunda: ":"C",
             "what is called when stroke your pickel to max but stop: ":"A",
             "who threw their grandma off the wheelchair:":"B"}

options = [["A.John Pork","B. skibidi","C. gojo","D. quandale"],
           ["A.Ass","B.bakaa","C.Gyatt","D.ohio"],
           ["A.Edging","B.jelquing","C.stroking","D.Shitting"],
           ["A.pepe","B.Quandale dingle","C.Toji","D.cameraman"]]

def Brain_rot():

    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("----------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("enter (A,B,C or D):").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_answer(correct_guesses, guesses)

def check_answer(answer,guess):

    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0
    
def display_answer(correct_guesses, guesses):
    print("----------------------------------------")
    print("Results")
    print("----------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int(((correct_guesses/len(questions))*100))
    print("your score is: "+str(score)+"%")

def play_again():

    response = input(" do you want to play again(yes/no)").lower()
    if response == "yes":
        return True
    else:
        return False
    
Brain_rot()

while play_again():
    Brain_rot()

print("byeee")