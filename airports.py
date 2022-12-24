class Airport:
    def __init__(self, name: str, code: str, lat: float, long: float):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long
        
    def __str__(self):
        return self.code + " "+ self.name
