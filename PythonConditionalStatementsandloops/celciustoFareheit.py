user_input = int(input("enter a number in celciues"))

cel = 60 
fahr = 140

def converttemp(cell):
    Fahren =  cell * (9/5) + 32
    print(Fahren)
    return Fahren 
    
converttemp(user_input)