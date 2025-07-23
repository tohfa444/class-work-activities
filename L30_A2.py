class bird:
    
    def __init__(self):
        print("Bied is ready")

    def whoisthis(self):
        print("Bird")

    def swin(self):
        print("Swin faster")
    
class penguin(bird):

    def __init__(self):

        super().__init__()
        print("Penguin is ready")

    def whoisthis(self):
        print("Peanguin")

    def run(self):
        print("Run faster")

peggy = penguin()
peggy.whoisthis()
peggy.swin()
peggy.run()
