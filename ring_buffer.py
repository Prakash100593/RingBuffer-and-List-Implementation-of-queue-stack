
"""
Below program implements functionalities for ring buffer
where reaching max size we can perform
insert_keep_new and insert_keep_old

"""

class Node:
    '''
    Defines node class with data and next pointer
    '''
    __slots__ = "data","next"
    def __init__(self,data):
        self.data = data
        self.next = None

class ringbuffer:
    '''
    Implements inset_keep_new, insrt_keepold, rempveoldest,
    removenewest, size, capacity

    defines pointers for head, tail, size and capacity
    '''
    __slots__ = "head","tail","size","capacity"


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def capacity_check(self,maxsize):
        '''

        assigns maxsize
        :param maxsize: capacity - maximum size of buffer
        :return:
        '''
        self.capacity = maxsize


    def isempty(self):
        '''
        Check is list is empty
        :return: boolean value
        '''
        return self.head == None

    def __str__(self):
        '''
        overrides string method to print required list
        :return: List String
        '''
        if(self.isempty()):
            print("List is Empty")
        else:
            # node = Node(data)

            result = "List["
            temp = self.head
            counter=0
            if(self.head is not None):
                while(counter<self.size):
                     result =result + " " + str(temp.data)
                     temp = temp.next
                     counter = counter +1
                     if(temp==self.head):
                         break;

            # while counter < self.size :
                #     result =result + " " + str(temp.data)
                #     temp = temp.next
                #     counter = counter +1
                result += " ]"
            return result

    def insert_keep_new(self,data):
        '''

        Creates node for new data and inserts
        it in the oldes position in case of size
        more than capacity or else appends it to the end
        :param data: data to be entered
        :return: none
        '''
        newnode = Node(data)
        if(self.isempty()):
            self.head = newnode
            self.tail = newnode
            #self.tail.next = self.head
            self.size +=1
        else:
            if(self.size <= self.capacity):
                self.tail.next = newnode
                self.tail = newnode
                self.size += 1
            else:
                newnode.next = self.head.next
                self.tail.next = newnode
                self.tail = newnode
                self.head = self.head.next

    def insert_keep_old(self,data):

        '''

        Creates node for new data and inserts
        it in the newest position in case of size
        more than capacity or else appends it to the end
        :param data: data to be entered
        :return: none
        '''

        newnode = Node(data)
        if(self.isempty()):
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
            self.size += 1
        else:
            if(self.size<=self.capacity):
                self.tail.next = newnode
                self.tail = newnode
                self.size += 1
            else:
                self.tail.data = newnode.data

    def find(self,data):

        '''

        find checks if the value is present in
        the list
        :param data: data to be entered
        :return: bollean value
        '''


        found = False
        if(self.isempty()):
            print("List is Empty")
        else:
            # node = Node(data)
            temp = self.head
            node = Node(data)
            counter=0
            if(self.head is not None):
                while(counter<self.size):
                     if(temp.data==node.data):
                         found = True
                         break
                     temp=temp.next
        if(found):
            return node
        else:
            return None



    def size_check(self):
        return self.size

    def replace(self, cursor, data):


        '''
        if the data is present in the list
        it will replace the data of the old
        node with the new dara

        :cursor : Returns the node what find returns
        :param data: data to be entered
        :return: bollean value
        '''

        found = False
        if (self.isempty()):
            print("List is Empty")
        else:
            # node = Node(data)
            temp = self.head
            node = Node(data)
            counter = 0
            if (self.head is not None):
                while (counter < self.size):
                    if (temp.data == cursor.data):
                        temp.data = node.data
                        break
                    temp = temp.next


    def remove_oldest(self):


        '''
        removes the oldes data from the list
        '''

        if(self.isempty()):
            print('List is Empty, cannot remove from empty list')
            return None
        else:
            if(self.size<=self.capacity):
                deleted = self.head.data
                self.head = self.head.next
                self.size -=1
            else:
                deleted = self.head.data
                self.head = self.head.next
                self.tail.next = self.head
                self.size -= 1
            return deleted

    def remove_newest(self):

        '''
        removes the newest data from the list
        '''

        if(self.isempty()):
            print('List is Empty, cannot remove from empty list')
            return None
        else:
            if(self.size<=self.capacity):
                deleted = self.tail.data
                temp=self.head
                while(temp.next!=self.tail):
                    temp=temp.next
                self.tail= temp
                self.size -=1
            else:
                deleted = self.tail.data
                temp=self.head
                while(temp.next!=self.tail):
                    temp=temp.next
                self.tail= temp
                self.tail.next=self.head
                self.size -= 1

def main():
        list = ringbuffer()
        list.capacity_check(5)
        list.insert_keep_new(2)
        print(list)
        print(list.size_check());

        list.insert_keep_new(3)
        print(list)
        print(list.size_check());

        list.insert_keep_new(4)
        print(list)
        print(list.size_check());

        list.insert_keep_new(5)
        print(list)
        print(list.size_check());

        list.insert_keep_new(6)
        print(list)
        print(list.size_check());

        list.insert_keep_new(7)
        print(list)
        print(list.size_check());

        list.insert_keep_new(8)
        print(list)
        print(list.size_check());

        list.insert_keep_new(9)
        print(list)
        print(list.size_check());

        list.insert_keep_new(10)
        print(list)
        print(list.size_check());

        list.insert_keep_new(11)
        print(list)
        print(list.size_check());

        list.insert_keep_old(12)
        print(list)
        print(list.size_check());

        list.insert_keep_old(13)
        print(list)
        print(list.size_check());

        list.remove_newest()
        print(list)
        print(list.size_check());

        list.remove_oldest()
        print(list)
        print(list.size_check());

        cursor = list.find(8)
        print(cursor)
        list.replace(cursor,12)
        print(list)





if __name__== "__main__":
    main()
