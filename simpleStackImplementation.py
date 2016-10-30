class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def isEmpty(self):
        return self.top<0
    
    def push(self, item):
        self.top+=1
        #print(self.top)
        if len(self.stack)<self.top+1:
            self.stack.append(item)
        else:
            self.stack[self.top]=item
        
    def peek(self):
        return self.stack[self.top]
        
    def pop(self):
        if self.isEmpty()==False:
            x = self.stack[self.top]
            self.top-=1
            return x
        else:
            return None
            
if __name__=='__main__':
    stack = Stack()
    stack.push(4)
    stack.push(1)
    stack.push(3)
    print(stack.pop())
    stack.push(8)
    print(stack.pop())