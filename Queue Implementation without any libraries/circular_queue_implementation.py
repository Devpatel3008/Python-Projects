class MyCircularQueue:
    
    def __init__(self, k: int):
        self.queue_size = k
        self.circular_que = [None]*k
        self.start = -1
        self.end = -1
    
    def enQueue(self) -> bool:      
                 
        if self.isEmpty():
            value = input("\nEnter element that you want to enter in a queue : ")
            self.start+=1
            self.end+=1
            self.circular_que[self.end] = value
            return True
        elif self.isFull():
            return False
        else:
            value = input("\nEnter element that you want to enter in a queue : ")
            if self.end == self.queue_size-1:
                self.end = -1
            self.end+=1
            self.circular_que[self.end] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.start == self.end:
            self.circular_que[self.start] = None
            self.start = -1
            self.end = -1
            return True
        else:
            self.circular_que[self.start] = None
            if self.start == self.queue_size-1:
                self.start = 0
            else:
                self.start+=1
            return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular_que[self.start]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular_que[self.end]

    def isEmpty(self) -> bool:
        if self.start == -1 and self.end == -1:
            return True
        return False
    
    def isFull(self) -> bool:
        if (self.start == 0 and self.end == self.queue_size - 1) or (self.start - self.end) == 1:
            return True
        return False
        
    def main(self):
        flag = True
        while(flag): 
            print('''\n*****Queue Operations*****\n1. Enter an element\n2. Delete an element\n3. Print Queue\n4. Get Front Element\n5.Get Last Element\n6. Check Queue is empty or not\n7. Check Queue is Full or not\n8. Reset Circular Queue Size\n9. Exit''')
            selection = int(input("\nEnter a selection : "))
            if selection == 1:
                if self.enQueue() == False:
                    print("You can not enter an element because Queue is full.")
            elif selection == 2:
                if self.deQueue() == False:
                    print("Queue is Empty....Can not delete an element")
            elif selection == 3:
                if self.isEmpty() == False:
                    for i in range(len(self.circular_que)):
                        pointer = '      '
                        if i == self.start:
                            pointer = 'Start '
                        elif i == self.end:
                            pointer = ' end  '
                        print(pointer, end = "")
                    print("\n")
                    for i in self.circular_que:
                        if i != None:
                            print("  " + i + "  ", end = " ")
                else:
                    print("Queue is Empty!!")
            elif selection == 4:
                result = self.Front()
                if result == -1:
                    print("Queue is Empty!!")
                else:
                    print(result)
            elif selection == 5:
                result = self.Rear()
                if result == -1:
                    print("Queue is Empty!!")
                else:
                    print(result)
            elif selection == 6:
                print(self.isEmpty())
            elif selection == 7:
                print(self.isFull())
            elif selection == 8:
                flag = False
                return 1
            elif selection == 9:
                flag = False
                return 2
            else:
                print("Invalid Choice")

if __name__ == '__main__':
    flag = True
    while(flag):
        try:  
            size = int(input("Size of Circular Queue :"))
            p = MyCircularQueue(size)
            value = p.main()
            if value == 2:
                flag = False
        except Exception as e:
            print(e)



