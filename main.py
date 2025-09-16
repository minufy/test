print("WOW")

class WOW:
    def __init__(self):
        self.wow = "WOW"
    
    def print_wow(self):
        print(self.wow)

class Amazing(WOW):
    def __init__(self):
        super().__init__()

    def print_amazing(self):
        print("amazing! " + self.wow)

wow = WOW()
wow.print_wow()
amazing = Amazing()
amazing.print_amazing()