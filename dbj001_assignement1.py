#Assignment 1

#Oppgave 1
import math
print("Ved å bruke binary søk vil maks antall steg være følgende:")
print("Oxford English dictionary:", math.ceil(math.log(171476, 2)))
print("Korean dictionary:", math.ceil(math.log(1100373, 2)))
print("Italian dictionary", math.ceil(math.log(260000, 2)))

#Oppgave 2
class House:
    def __init__(self, owner="landlord"):
        self.owner = owner

    def printWelcome(self,):
        print("Welcome", self.owner, " !")

#Oppgave 3
#Denne klassen konstruerer en node som inneholder data, og viser til neste node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


#Testdata
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")

node1.next = node2
node2.next = node3
node3.next = node4


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        self.head = node1
        while self.head:
            print(self.head.data)
            self.head = self.head.next


testListe = LinkedList()
testListe.printList()



