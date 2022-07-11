class Rent:
    def __init__(self):
        self.rent_movie = {}
    
    def add_to_cart(self,name,quantity):
        if name in self.rent_movie:
            self.rent_movie.append += quantity
        else:
            self.rent_movie.append[name] = quantity

    def total_cost(self):
        total = 0
        for name, quantity in self.rent_movie.items():
            price = 5
            total += price * quantity 
        return(f"Total Cost of your order is: ${total}")
