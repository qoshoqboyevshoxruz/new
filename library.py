from mailbox import linesep

class Library:
    def __init__(self,id,name,author,count,price):
        self.id=id
        self.name=name
        self.author=author
        self.count=count
        self.price=price

    def yozsin(self):
        with open('library.txt','a') as f:
            f.write(f"{self.id}, {self.name}, {self.author}, {self.count}, {self.price}")
    def oqish():
        with open('library.txt','r') as f:
            for i in f.read().split('\n')[1:]:
                 if len(i)!=0:
                   n=i.split(',')
                   print(f"Id:{n[0]}, Name:{n[1]}, Author:{n[2]}, Count:{n[3]}, Price:{n[4]}")

    def ayir_count(id):
        with open('library.txt', 'r') as f:
            qatorlar = f.readlines()

        with open('library.txt', 'w',encoding='utf-8') as f:
            for i in qatorlar:

                n=i.split(',')
                ochir=0
                if n[0] == id:
                    ochir=1
                    counti=int(n[3])-1
                    print(f"Sizning kitobingiz-> NOMI: {n[1]}, Author{n[2]},Price: {n[4]}")
                    f.write(f"{n[0]},{n[1]},{n[2]},{counti},{n[4]}\n")
                else:
                    f.write(i)
            if ochir==0:
                print("ID boyicha kitob topilmadi")



    def ochir(Id):
        with open('library.txt', 'r',encoding='utf-8') as f:
            qatorlar = f.readlines()

        with open('library.txt', 'w') as f:
            for i in qatorlar:
                ochir=0
                if i.split(',')[0]!= Id:
                    f.write(i)
                else:
                    ochir=1

            if ochir==1:
                print("Id boyicha ochirildi")
            else:
                print("Id xato kiritildi")


def menu():
    print("[1]Kitob qoshish")
    print("[2]Kitob royhatni korish")
    print("[3]Kitob olish")
    print("[4]Kitobni royhatdan ochirish")


while 1:
    menu()
    num=int(input(">>>"))
    if num==1:
        id=input("id: ")
        name=input("Name: ")
        author=input("Author: ")
        count=input("Count: ")
        price=input("Price:")
        kitob=Library(id,name,author,count,price)
        Library.yozsin(kitob)
    elif num==2:
        Library.oqish()
    elif num==3:
        id=input('Id:')
        Library.ayir_count(id)
    elif num==4:
        Id=input("Id:")
        Library.ochir(Id)




