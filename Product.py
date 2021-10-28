class Product:
    def __init__(self, volume, price):
        self.volume = volume
        self.price = price
        
    def __str__(self):
        return f"{self.volume}, {self.price}"
        