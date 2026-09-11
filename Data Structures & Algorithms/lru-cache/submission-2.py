#egati zadachata

class dll:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.capacity=capacity
        self.size=0
        self.LRU=dll(None)
        self.MRU=dll(None)
        self.LRU.next=self.MRU
        self.MRU.prev=self.LRU
    def update(self,b):
        d=self.MRU.prev
        a=b.prev
        c=b.next

        b.next=self.MRU
        self.MRU.prev=b
        d.next=b
        b.prev=d
        a.next=c
        c.prev=a
    def get(self, key: int) -> int:
        getnodewith=self.map
        if(key in self.map):
            b=getnodewith[key]
            if(not b is self.MRU.prev):
                self.update(b)

            return b.val[1]
        else:
            return -1
    def delete(self):
        tbdel=self.LRU.next
        self.LRU.next=tbdel.next
        tbdel.next.prev=self.LRU
        del self.map[tbdel.val[0]]
        return
    def addition(self,a):
        p=self.MRU.prev
        p.next=a
        a.prev=p
        a.next=self.MRU
        self.MRU.prev=a
        return
    def put(self, key: int, value: int) -> None:
        getnodewith=self.map
        if(key in self.map): #modification
            b=getnodewith[key]
            b.val=(key,value)
            if(not b is self.MRU.prev):
                self.update(b)
            
        else: # addition with possible deletion if out of capacity
            s=self.size
            if(s>=self.capacity):
                self.delete()
                a=dll((key,value))
                self.addition(a)
                self.map[key]=a
            else:
                a=dll((key,value))
                self.addition(a)
                self.map[key]=a
                
                self.size+=1
        return 
