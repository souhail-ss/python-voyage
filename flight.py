class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float()):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration
    
    def __str__(self):
        return self.src_code + " -> " + self.dst_code
