
import random


def ShuffleCardPack(typeOfShuffle,arr):
    error=False
    if typeOfShuffle == 1:
        print("Fisher Yates shuffle selected...")
        arr=FisherYatesShuffle(arr)

    elif typeOfShuffle == 2:
        print("Riffle shuffle selected...")
        arr=RiffleShuffle(arr)
    elif typeOfShuffle == 3:
        print("No shuffle selected...")
    else:
        error = True
    while error:
        error=False
        try:
            typeOfShuffle=int(input("There was an error...\nPlease enter a number between 1 and 3\nEnter the type of shuffle: 1. Fisher Yates, 2. Riffle, 3. No shuffle:"))
        except (ValueError):
            error =True
        if error == False:
            if typeOfShuffle == 1:
                print("Fisher Yates shuffle selected...")
                arr=FisherYatesShuffle(arr)
            elif typeOfShuffle == 2:
                print("Riffle shuffle selected...")
                arr=RiffleShuffle(arr)
            elif typeOfShuffle == 3:
                print("No shuffle selected...")
            else:
                error = True
    return arr
def FisherYatesShuffle(arr):
    for x in range(0,51):
        index = random.randint(0,len(arr)-x)
        temp = arr[index]
        arr[index]=arr[x]
        arr[x]=temp
    return arr


def RiffleShuffle(arr):
    error=False
    try:
        amountOfRiffles=int(input("Enter the amount of riffles that you want to occur:"))
    except (ValueError):
            error = True
    if error == False:
        if amountOfRiffles<0:
            error=True
    while error:
        error=False
        try:
            amountOfRiffles=int(input("There was an error...\nEnter the amount of riffles that you want to occur:"))
        except (ValueError):
            error = True
        if error == False:
            if amountOfRiffles<0:
                error=True
    while amountOfRiffles>0:
        count=0
        count1=0
        count2=0
        arr1=[]
        arr2=[]
        for x in range(0,26):
            
            arr1+=[arr[x]]

        for y in range(26,52):
            arr2+=[arr[y]]


        while count2<26:
            if count%2==0:
                arr[count]=arr2[count1]
                count1+=1
            else:
                arr[count]=arr1[count2]
                count2+=1
            count+=1
        
        amountOfRiffles-=1
    return arr

arr=[]

value=1
for x in range(0,52):
    if (x+1)<14:
        if x+1==1:
            arr+=[["Ace","Diamonds"]]
        elif x+1==11:
            arr+=[["Jack","Diamonds"]]
        elif x+1==12:
            arr+=[["Queen","Diamonds"]]
        elif x+1==13:
            arr+=[["King", "Diamonds"]]
            value=0
        else:
            arr+=[[str(x),"Diamonds"]]

    elif (x+1)<27 and (x+1)>13:
        if x+1==14:
            arr+=[["Ace","Hearts"]]
        elif x+1==24:
            arr+=[["Jack","Hearts"]]
        elif x+1==25:
            arr+=[["Queen","Hearts"]]
        elif x+1==26:
            arr+=[["King", "Hearts"]]
            value=0
        else:
            arr+=[[str(value),"Hearts"]]
    elif x+1<40 and x+1>26:
        if x+1==27:
            arr+=[["Ace","Clubs"]]
        elif x+1==37:
            arr+=[["Jack","Clubs"]]
        elif x+1==38:
            arr+=[["Queen","Clubs"]]
        elif x+1==39:
            arr+=[["King", "Clubs"]]
            value=0
        else:
            arr+=[[str(value),"Clubs"]]
    else:
        if x+1==40:
            arr+=[["Ace","Spades"]]
        elif x+1==50:
            arr+=[["Jack","Spades"]]
        elif x+1==51:
            arr+=[["Queen","Spades"]]
        elif x+1==52:
            arr+=[["King", "Spades"]]
            value=0
        else:
            arr+=[[str(value),"Spades"]]
    value+=1

error=False
try:
    typeOfShuffle=int(input("Enter the type of shuffle: 1. Fisher Yates, 2. Riffle, 3. No shuffle:"))
except (ValueError):
    error =True
while error:
    error=False
    try:
        typeOfShuffle=int(input("Enter the type of shuffle: 1. Fisher Yates, 2. Riffle, 3. No shuffle:"))
    except (ValueError):
        error =True

arr=ShuffleCardPack(typeOfShuffle,arr)

try:
    people=int(input("Enter the amount of people being dealt for:"))
except (ValueError):
    error=True
if error == False and people<=0:
    error=True
try:
    cards=int(input("Enter the amount of cards each person gets:"))
except (ValueError):
    error =True
if error ==False and cards<=0:
    error=True
while error or cards*people>52:
    error=False
    print("There was an error...")
    try:
        people=int(input("Enter the amount of people being dealt for:"))
    except (ValueError):
        error =True
    if error == False and people<=0:
        error=True
    try:
        cards=int(input("Enter the amount of cards each person gets:"))
    except (ValueError):
        error = True
    if error == False and cards<=0:
        error=True
personCount=1
cardsDealt=0
cardCount=cards
while people>0:
    print("\nPerson "+str(personCount)+" has the:")
    while cards>0:
        print(arr[cardsDealt][0]+" of "+arr[cardsDealt][1])
        cardsDealt+=1
        cards-=1
    cards=cardCount
    people-=1
    personCount+=1

    
        



    
     
     
     
     
     
     
        
        
            
        
    
