# System defined exception
try:
    raise MemoryError("memory error")
except MemoryError as e:
    print(e)
    
# User defined exception
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("Accident occured. Take detour")
        
try:
    raise Accident("crash between two cars")
except Accident as e:
    e.handle()