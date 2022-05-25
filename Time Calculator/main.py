#import time_calculator 
from time_calculator import add_time

def main():
    print("******Welcome To Time Calculator******")
    No = int(input("Enter Number of time do you want to calculate : "))
    for i in range(No):
        print("Time Format : 11:11 AM")
        start = input("Enter time : ")
        print("Time Format : 11:11")
        duration = input("Enter Time you want to add :")
        print("Enter y fo yes")
        choice = input("Do you want to insert day like Monday : ")
        if choice == 'y':
            day = input("Enter Day : ")
            statement = add_time(start,duration,day)
            print(statement)
        else:
            statement = add_time(start,duration)
            print(statement)

main()