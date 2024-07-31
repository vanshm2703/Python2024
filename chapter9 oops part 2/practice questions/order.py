#create a class called order which stores item and its price

#     use dunder function __gt__() to convey that:
# order1>order2 if price of order>price of order 2

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,oder2):#dunder function
        return self.price>oder2.price

        

oder1=order("pan",700)
oder2=order("spoon",100)

print(oder1>oder2)

