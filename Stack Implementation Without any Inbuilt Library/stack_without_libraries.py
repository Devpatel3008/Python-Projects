class data_structure_stack:
    stack = []
    def push(p):
        value = input("\nEnter a value that you want to enter in a stack : ")
        p.stack.append(value)

    def pop(p):
        if(len(p.stack) == 0):
            print("\nStack is Empty...can not complete pop operation.")
        print(f"\nPop : {p.stack[-1]}")
        p.stack.pop()
    
    def print_stack(p):
        flag = True
        for i in reversed(p.stack):
            if flag == True: 
                flag = False
                print(f"\n|{i}| <-- Top Element")
            else:
                print(f"|{i}|")
                
    def main(p):
        flag = True
        while(flag): 
            print("\n*****Stack Operations*****\n1. Push\n2. Pop\n3. Print\n4. Exit\n")
            selection = int(input("Enter a selection : "))
            if selection == 1:
                p.push(p)
            elif selection == 2:
                p.pop(p)
            elif selection == 3:
                p.print_stack()
            elif selection == 4:
                flag = False
            else:
                print("Invalid Choice")

if __name__ == '__main__':
    p = data_structure_stack
    flag = True
    while(flag):
        try:  
            p.main(p)
            flag = False
        except Exception as e:
            print(e)
        
        
    