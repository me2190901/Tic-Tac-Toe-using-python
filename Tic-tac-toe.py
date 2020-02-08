def printpattern(pattern):         #print pattern
    for i in range(len(pattern)):
        for j in range(len(pattern)+1):
            print(pattern[i][j],end="")
        print()
def winnings(player,winning):     #check if winning condition is satisfied or not
    for i in range(len(winning)):
            if (winning[i][0] in player) and (winning[i][1] in player) and (winning[i][2] in player):
                return True
def changepattern(symbol,pattern,number): #change pattern to specified symbol
    if number==1:
        pattern[2][2]=symbol
    elif number==2:
        pattern[2][6]=symbol
    elif number==3:
        pattern[2][10]=symbol
    elif number==4:
        pattern[6][2]=symbol
    elif number==5:
        pattern[6][6]=symbol
    elif number==6:
        pattern[6][10]=symbol
    elif number==7:
        pattern[10][2]=symbol
    elif number==8:
        pattern[10][6]=symbol
    elif number==9:
        pattern[10][10]=symbol
def playgame():      #main game playing
    print("Welcome To Tic Tac Toe!")
    symbol1=input("Player1: Do You Want To Be X or O.\n").strip().upper()
    print("Player1 Will Go First!")
    if symbol1=="X":
        symbol2="O"
    else:
        symbol2="X"
    dividers=[" ","_","_","_"," ","_","_","_"," ","_","_","_"," "]
    elements=["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
    pattern=[dividers]+[elements[::]]+[elements[::]]+[elements[::]]+[dividers]+[elements[::]]+[elements[::]]+[elements[::]]+[dividers]+[elements[::]]+[elements[::]]+[elements[::]]

    winning=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]
    chances=9
    player1=[]
    player2=[]
    for i in range(1,10):
        changepattern(i,pattern,i)
    printpattern(pattern)
    while chances>0:
        if chances%2!=0:
            number=int(input("Player1:Choose Your Next Position: (1:9)\n").strip())
            player1.append(number)
            changepattern(symbol1,pattern,number)
            printpattern(pattern)
            if winnings(player1,winning):
                print("Congratulations Player1 You Have Won The Game!")
                return 0
        else:
            number=int(input("Player2:Choose Your Next Position: (1:9)\n").strip())
            player2.append(number)
            changepattern(symbol2,pattern,number)
            printpattern(pattern)
            if winnings(player2,winning):
                print("Congratulations Player2 You Have Won The Game!")
                return 0
        chances-=1
wanttoplay=True
while wanttoplay:
    playgame()
    want=input("Do you want to play again? Enter 'Yes' or 'No':\n").strip().upper()
    if want=="NO":
        wanttoplay=False