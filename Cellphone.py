class Celular:
    def __init__(self, brand, model, camera):
        self.brand = brand
        self.model = model
        self.camera = camera
    def call(self):
        print(f"You end the call with your: {self.brand}")
    def cut(self):
        print(f"You end your call in your: {self.model}")


smartphone_one = Celular("Samsung", "S20", "M23")

smartphone_one.call()