#ROCK_PAPER_SCISSORS

import random

l1=['r','p','s']

print("\t\t\t\t\t______Rock,Paper,Scissors Game______\n\n\n")
print("r for Rock\np for Paper\ns for Scissors\n")

hp=0
cp=0
lives=10

i=1
while i<=10:
    comp=random.choice(l1)
    man=input("Rock,Paper,Scissors:")
    print("Your guess",man,"and Computer guess",comp,"\n")

    while True:
        if man==comp:
            print("Tie Both 0 point to each\n")
        elif man=='s' and comp=='p':
            print("Human wins 1 point\n")
            hp+=1
        elif man=='p' and comp=='s':
            print("Computer wins 1 poit\n")
            cp+=1
        elif man=='p' and comp=='r':
            print("Human wins 1 point\n")
            hp+=1
        elif man=='r' and comp=='p':
            print("Computer wins 1 point\n")
            cp+=1
        elif man=='r' and comp=='s':
            print("Human wins 1 point\n")
            hp+=1
        elif man=='s' and comp=='r':
            print("Computer wins 1 point\n")
            cp+=1
        print("Computer point is",cp,"and","Your point is",hp,"\n")
        break
    if lives>=0:
        lives-=1
        print(lives,"is left out of 10\n")
    if i==10:
        print("\t\t\t_____Game Over_____\n")
        if hp>cp:
            print("\t\t    You win and Computer loose")
            print("\t\tYour point is",hp,"and","Computer point is",cp,"\n") 
        elif hp==cp:
            print("\t\t            Game is Drow")
            print("\t\tYour point is",hp,"and","Computer point is",cp,"\n")
        else:
            print("\t\t    Computer win and You loose")
            print("\t\tYour point is",hp,"and","Computer point is",cp,"\n")
    i=i+1