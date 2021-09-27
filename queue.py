import streamlit as st

class Node:
    def __init__(self, name, num):
        self.customerDetails = [name, num]
        self.nextNode = None


class Queue: 
      
    def __init__(self): 
        self.firstNode = self.LastNode = None
        self.size = 0
  
    def isEmpty(self): 
        return self.firstNode == None
      
    # Method to add an item to the queue 
    def enqueue(self, name, num): 
        newNode = Node(name, num) 
          
        if self.LastNode == None: 
            self.firstNode = self.LastNode = newNode
            self.size = self.size + 1
     
            return

        self.LastNode.nextNode = newNode
        self.LastNode = newNode 
        self.size = self.size + 1
  
    # Method to remove an item from queue 
    def dequeue(self): 
          
        if self.isEmpty(): 
            print("Nothing to dequeue.")
            return
        removeNode = self.firstNode
        self.firstNode = removeNode.nextNode
        self.size = self.size - 1

        if self.firstNode == None: 
            self.LastNode = None

    def traverse(self):
        currentNode = self.firstNode
        while currentNode is not None:
            print (currentNode.customerDetails)
            currentNode = currentNode.nextNode
        
    def getFirstElement(self):
        
        if self.isEmpty(): 
            print("Empty Queue Now.")
            return
        
        return self.firstNode.customerDetails
      

ticketSystem = Queue()


ticketNo = 1000


while True:
    st.write('Welcome to the RBA Ticket Booking System. You will be served soon.')
    st.write('For Customer: Press 1 to queue.')
    st.write('For Customer Care Consultant: Press 2 to serve the next customer.')
    st.write('For Customer Care Consultant: Press 3 to get the list of customers in the waiting queue.')

    st.write('Press x to end the system. ')
    step = input("\nPlease enter the number.\n\n")
    if step.lower() == 'x':
        st.write('Thank you for using our service. ')
        break
    try:
        step = int(step)

        if step!= 1 and step!=2 and step!=3:
            st.write('\nYou have entered an undefined numb')


        elif step==1:
          
            
            customerName = input("\nPlease enter your name.\n\n")
            ticketNo = ticketNo + 1
            ticketSystem.enqueue(customerName, ticketNo)
            waitingTime = 2*ticketSystem.size

            print("\nDear {}. Your ticket no is {}.".format(customerName,ticketNo))
            print("Your estimated waiting time is {} minutes.\n\n".format(waitingTime))

        elif step==2:
            counterNo = input("\nPlease enter your counterNo.\n\n")

            if ticketSystem.size >0:
                print("No # {} , counter {}".format(ticketSystem.getFirstElement()[1],counterNo))

                ticketSystem.dequeue()
            else:
                print("No one in the queue now.")
        
        else:
            ticketSystem.traverse()
         
    
    except ValueError:
        print("\nPlease enter a number.\n\n")
