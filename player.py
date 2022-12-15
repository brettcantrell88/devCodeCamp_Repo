class Player:

    def __init__(self, cash_passed):
        self.name = ''
        self.cash = cash_passed
        print(self.cash)
        
    def set_name(self):
        self.name = input("Please enter a name: ")