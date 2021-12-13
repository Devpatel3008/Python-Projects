class Queue:
    def __init__(self):
        self.queue = [] 
        self.start = -1
        self.end = -1
                
    def enQueue(self) -> bool:
        if self.start == -1:
            self.start += 1
        self.end += 1
        value = input("\nEnter element that you want to enter in a queue : ")
        self.queue.append(value)
        
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.start == 0 and self.end == 0:
            self.queue.pop(0)
            self.start = -1
            self.end = -1
            return True
        else:
            self.queue.pop(0)
            self.end -= 1
            return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[0] 
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[len(self.queue)-1] 
        
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def main(self):
        flag = True
        while(flag):
            print("\n*****Queue Operations*****\n1. Enter an element\n2. Delete an element\n3. Get Front Element\n4. Get Rear Element\n5. Check queue is empty or not\n6. Print Queue\n7. Exit")
            selection = int(input("\nEnter a selection : "))
            if selection == 1:
                self.enQueue()
            elif selection == 2:
                if self.deQueue() == False:
                    print("Queue is empty...can not delete an element")
            elif selection == 3:
                if self.Front() == -1:
                    print("Queue is empty...")
            elif selection == 4:
                if self.Rear() == -1:
                    print("Queue is empty...")
            elif selection == 5:
                if self.isEmpty():
                    print("Queue is Empty")
                else:
                    print("Queue is not Empty")
            elif selection == 6:
                if self.isEmpty() == False:
                    for i in range(len(self.queue)):
                        pointer = '      '
                        
                        if i == self.start:
                            if self.start == self.end:
                                pointer = 'Start & end'
                            else:
                                pointer = 'Start '
                        elif i == self.end:
                            pointer = ' end  '
                        print(pointer, end = "")
                    print("\n")
                    for i in self.queue:
                        print("  " + i + "  ", end = " ")
                else:
                    print("Queue is Empty!!")
            elif selection == 7:
                flag = False
            else:
                print("Invalid Input")
            
if __name__ == '__main__':
    try:  
        p = Queue()
        p.main()
    except Exception as e:
        print(e) 
            
            
            
                