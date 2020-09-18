class Restaurant:
    def __init__(self,customer,money):
        self.customer = customer
        self.__money = money

    def coupan(self):

        print(f"Hello, {self.customer},please pay {self.__money} and take your coupan")


class IcecreamStand(Restaurant):
    '''Using this class to show inheritence & polymorphism'''
    def __init__(self,customer,money):
        super().__init__(customer,money)

    def coupan(self):
        #self.coupan = coupan
        #coupan = self.coupan

        answer = (input("Do you have coupan?('Yes/No'): ").title())
        if answer == 'Yes':
            print(f"Hi {self.customer},please give your coupan.")
        else:
            super().coupan() #here calling coupan method from parent class - Restaurant

z = IcecreamStand('Jagruti',20)
print(z.coupan())
