class Fruit():
    def __init__(self, name, calory):
        self.name = name
        self.calory = calory

    def get_name(self):
        return self.name
    
    def get_calory(self):
        return f"This {self.name} has {self.calory} calories"