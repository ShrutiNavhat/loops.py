i=1
while i<=5:
    a=int(input("enter the number : "))
    if a==7:
        print("you win the game")
        break
    elif a>7:
        print("your guess is greater")
    elif a<7:
        print("your guess is lasser") 
    i=i+1
if a==7:
    print("you win the game")
else:
    print("you loses the game")

        



