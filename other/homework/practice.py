class Car():
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")


audi1 = Car("Audi", "Sedan", "A6")
audi1.start()
audi1.stop()
