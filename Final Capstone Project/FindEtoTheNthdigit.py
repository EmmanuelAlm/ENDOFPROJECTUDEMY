#user_input = int(input("Enter how many e's do you want to that decimal place: "))
#e_list = []
#for inte in range(0,user_input):
#    e_list.append(inte)
nth = 'e'

def ask_e():
    global user_input
    user_input = int(input("Enter how many e's do you want to that decimal place: "))
    
if __name__ == "__main__":
    playing = True
    ask_e()
    while(playing):
        if user_input <=15:
            print('.',nth*user_input)
            ask_e()
        else: 
            print("too many eees: ")
            ask_e()
    


