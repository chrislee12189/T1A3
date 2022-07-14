class Rent:
    def __init__(self):
        self.rent_movie = {}
    
    def add_to_cart(self,name,length):
        self.name = name
        self.length = length 
        print(f"{self.name}: is loaned to you for: {self.length}")