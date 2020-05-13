""""Write a Python program to find those ,numbers which are divisible by 7 and multiple of 5
 between 1500 and 2700 (both included)"""
divis_list = list(range(1500,2701))
#print(divis_list)
 
def divbyseven(sample):
    divine_list = []
    for x in sample:
        if x % 7 == 0 and x% 5 == 0:
            divine_list.append(x)
    print(divine_list)
    return divine_list

     
divbyseven(divis_list)
