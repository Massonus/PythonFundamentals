class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Create obj: {self.real}+{self.imag}j")
    
    def __del__(self):
        print(f"Deleting obj: {self.real}+{self.imag}j")

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))
 
###################################

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(8, 9)


# c2 = ComplexNumber(78, 8)
c1.getData()
c2.getData()



 
# c2 = ComplexNumber(5,7)
# c2.getData()

# ############################# 
# del ComplexNumber.getData

# c1.getData()

# c2.getData()

########################### 
# del c1

# print(c1)

