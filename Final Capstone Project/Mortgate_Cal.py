mortage_amount = int(input("How much is your mortage: "))
mortage_length = int(input("How many months will it take: "))
int_rate = .12
def cal_mort(amount,length):
    pay_without_int = amount / length
    pay_wit_int = pay_without_int * int_rate + pay_without_int
    print("This is what you pay with out interest: ",pay_without_int,"This is pay with interest per month: " ,pay_wit_int)

cal_mort(mortage_amount,mortage_length) 


    
    