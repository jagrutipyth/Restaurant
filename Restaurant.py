class Restaurant:
    '''Main class Restaurant is added'''
    def __init__(self, name, city):
        self.__name = name
        self.__city = city

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def coupan(self, customer):
        self.__customer = customer
        print(f"{self.__name} from {self.__city} has got {self.__customer}")

    def amount_of_oil(self, item, oil_packet=1):
        self.__oil_packet = oil_packet
        self.__item = item
        if oil_packet == 1:
            print(f"Oil packet for 1 batch of {self.__item} is 1")
        else:
            print(f"Oil packet requied for 1 batch are {self.__oil_packet}")


class IcecreamStand(Restaurant):
    '''child class of Restaurant is created'''

    def __init__(self, fruit, name='Haldiram', city='Pune', position='left_corner'):
        self.__fruit = fruit
        self.__position = position
        super().__init__(name, city) #can also use *parentclass.*
        self.about_icecream = About_icecream() #instance as a attribute is used About_icecream is a different class

    def get_flavour(self):
        return self.__flavour

    def set_flavour(self, flavour):
        self.__flavour = flavour

    def about_icecream_stand(self):
        print(f"Icecreamstand is in {self.__position}")

    def amount_of_oil(self):  #method overrriding
        print("Icecream doesnt need oil for making.")


class About_icecream:
    '''independent class is created and is used as instance in child class'''

    def __init__(self, fruit='mango', milkmaid=2, batch=1, fruit_quantity=3):
        self.__milkmaid = milkmaid
        self.__batch = batch
        self.__fruit = fruit
        self.__fruit_quantity = fruit_quantity

    def get_milkmaid(self):
        return self.__milkmaid

    def set_milkmaid(self, milkmaid):
        self.__milkmaid = milkmaid

    def get_fruit(self):
        return self.__fruit

    def set_fruit(self, fruit):
        self.__fruit = fruit

    def icecream_material(self):

        fruit_list = ['Banana', 'Mango', 'Coconut', 'Strawberry', 'Grape', 'Orange']
        print(fruit_list)
        x = input(f"please choose fruit from the list:")
        x = x.title()#Capitalizes 1st letter
        if x in fruit_list:
            if x == 'Mango':
                x += 'es'
                return(f"for {self.__batch} of icecream we need {self.__fruit_quantity} {x} ")
            elif x == 'Strawberry':
                x = x[:-1]
                x = x + 'ies'
                print(f"for {self.__batch} of icecream we need {self.__fruit_quantity} {x} ")
            else:
                x += 's'
                print(f"for {self.__batch} of icecream we need {self.__fruit_quantity} {x} ")
        else:
            print("Fruit is not avilable")
        # print(f"for {self.__batch} of icecream we need {self.__fruit_quantity}{self.__fruit} ")


z = IcecreamStand('Mango')
print(z.about_icecream.icecream_material())
