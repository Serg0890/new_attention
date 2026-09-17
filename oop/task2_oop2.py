class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self) -> str:
        return f"{self.__class__.__name__}, model {self.model}."

    def operate(self):
        print("робот ездит")


class RobCleaner(Robot):

    def __init__(self, garbage=0, model="cleaner"):
        super().__init__(model)
        self.garbage = garbage

    def operate(self):
        self.garbage += 1
        print(f"робот {self} пылесосит, Наполнение мешка - {self.garbage}")



class RobSec(Robot):
    def __init__(self, alarm_sys,model="Security"):
        super().__init__(model)
        self.alarm_sys = alarm_sys

    def operate(self):
        print(f"Робот {self} охраняет дом при помощи {self.alarm_sys}")
    

class RobSwim(RobSec):
    def __init__(self, alarm_sys, model, depth):
        super().__init__(alarm_sys, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f"охрана ведется. на глубине {self.depth}")

clear_rob = RobCleaner()
clear_rob.operate()
clear_rob.operate()

sec_rob = RobSec("pandora")
sec_rob.operate()

swim_pool = RobSwim("pandora", "Guard", depth=5)
swim_pool.operate()
