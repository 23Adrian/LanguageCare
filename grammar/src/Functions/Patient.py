class Patient():

    def __init__(self, weight, height ):
        self.weight = weight



    def BMIImperial(weight, height):
        w = weight*.45
        l = height*.025

        l = l*l

        bmi = w / l

        print("this person's bmi is" + bmi)

        if(bmi < 18):
            print("Patient is under weight")
            return bmi

        if(bmi < 25):
            print("Patinet has a normal weight")
            return bmi
        if(bmi < 30):
            print(("Patient is over weight"))
            return bmi

        if(bmi > 30):
            print("Patient is obese and needs help")
            return bmi

    def BMIMetric(weight , height):

        bmi = weight/(height*height)
        print("This person's bmi is" + bmi)
        if (bmi < 18):
            print("Patient is under weight")
            return bmi

        if (bmi < 25):
            print("Patinet has a normal weight")
            return bmi
        if (bmi < 30):
            print(("Patient is over weight"))
            return bmi

        if (bmi > 30):
            print("Patient is obese and needs help")
            return bmi



    def get__bmi(self):
        return  self.weight

