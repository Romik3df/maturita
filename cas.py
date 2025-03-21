

class Time:
    def __init__(self, hours, minutes):
        self.__hours = hours % 24
        self.__minutes = minutes % 60
        self.__normalize()
    
    def __normalize(self):
        extra_hours = self.__minutes // 60
        self.__minutes %= 60
        self.__hours = (self.__hours + extra_hours) % 24
    
    def display(self):
        print(f"{self.__hours:02}:{self.__minutes:02}")
    
    def getTime(self):
        return f"{self.__hours:02}:{self.__minutes:02}"
    
    def add(self, h, m):
        self.__hours = (self.__hours + h) % 24
        self.__minutes += m
        self.__normalize()
    

def createTime(time, h, m):
    new_hours = (time._Time__hours + h) % 24
    new_minutes = time._Time__minutes + m
    return Time(new_hours, new_minutes)

if __name__ == "__main__":
    t = Time(10, 30)
    t.display()  # Očakávaný výstup: 10:30
    print(t.getTime())  # Očakávaný výstup: "10:30"
    
    t.add(2, 45)  # Posun o 2 hodiny a 45 minút
    t.display()  # Očakávaný výstup: 13:15

