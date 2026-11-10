import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True
while is_running:
    guess=input("enter the number: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print(f"please enter the number between {lowest_num} and{highest_num}")
        elif guess<answer:
            print("too low!!")
        elif guess>answer:
             print("too high!! try again")
        else:
              print(f"correct!!! the number is {answer}")
              print(f"number of guesses: {guesses}")
              is_running=False 