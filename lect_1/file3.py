class CastomClass:

    def __init__(self, par1):
        self.par1 = par1
        self.par2 = None

    def mymethod(self):
        self.par2 = 10



instance = CastomClass(10)
print(instance.par1)
# instance.mymethod()
print(instance.par2)