class Bus:

    def __init__(self, route, destination):
        self.route = route
        self.destination = destination
    
    drive = "Bum, Brum"    

    def drive_method(self, drive):
        print(f"Bus sound is{drive}")
