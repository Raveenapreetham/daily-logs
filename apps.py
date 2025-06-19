import bussiness as bus

def user_info(name,account_no,balance=0):
     
     user_list=[]

     if name and account_no and balance !=0:
          user_list.append([name,account_no,balance])
     else:
          user_list.append([name,account_no,balance])
     return user_list[0]    

def return_deposite(total_balance, amount):

     result= bus.deposite_calc(total_balance, amount) 

     return result

def return_withdraw(total_balance, amount):

     result= bus.withdraw_calc(total_balance, amount) 

     return result


def main():

    name = input("Enter your name : ")

    account_no = int(input("Enter your account number : "))
    
    question_1 = input("Do you want to enter your balance[y/n] :").lower()

    if question_1 == 'y':
        balance = int(input("Enter your balance : "))

        print(f'User infos : {user_info(name, account_no, balance)}')
    else:
        print(f'User infos : {user_info(name, account_no)}')

    question_2 = input("Do you want to deposite [y/n] : ").lower()

    if question_2 == 'y' and question_1 == 'y':
        deposite_amount = int(input("Enter the amount you want to deposite : "))

        print(f'Total balance : {return_deposite(total_balance = balance,amount = deposite_amount)}')

    elif question_2 == 'y' and question_1 == 'n':
        balance         = int(input("Enter your balance : "))

        deposite_amount = int(input("Enter the amount you want to deposite : "))

        print(f'Total balance : {return_deposite(balance, deposite_amount)}')


    question_3 = input("Do you want to withdraw[y/n] :").lower()

    if question_3 == 'y' and question_1 == 'y':

        withdraw_amount = int(input("Enter the amount you want to withdraw : "))

        print(f'Total balance : {return_withdraw(total_balance = balance,amount = withdraw_amount )}')

    elif question_3 == 'y' and question_1 == 'n':
        balance         = int(input("Enter your balance : "))

        withdraw_amount = int(input("Enter the amount you want to withdraw : "))

        print(f'Total balance : {return_withdraw(balance, withdraw_amount)}')

if __name__ =='__main__':
 main()

