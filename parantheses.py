class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

x=str(input("Enter the Statement"))
s1=Stack()

u=0
d=0
for k in x:
    if k=='[' or k=='(' or k=='{':
        s1.push(k)
        d+=1

    elif k==']' or k==')' or k=='}':
        a=s1.pop()
        print(a,k)
        if (a=='(' and k==')') or (a=='[' and k==']') or (a=='{' and k=='}'):
            u+=1
            
        else:
            print("Not a Parantheses")

if u==d:
    print("This is a Parantheses")



