class Calculate():
    def __init__(self,age,credit,micromorts):
        self.age = age
        self.million = credit
        self.micrimorts = micromorts

    def calc(self):
        chance_alive = int(1)
        MICROMORTS = {a: 1.10409**(a-20) for a in range(20,100)}
        START_KF = 0.05
        m = self.micrimorts
        for item in MICROMORTS.items():
            if item[0] == self.age:
                m += item[1]
                for j in range(365):
                    chance_alive *= (1000000-m)/1000000
                m = self.micrimorts

        Chance = round((1-chance_alive)*100, 2)
        KF = Chance/START_KF
        return self.million*0.0012*KF