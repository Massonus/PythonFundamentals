class ComplexNumber:
    
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
        
    def getData(self):
        return f"{self.real} + {self.imag}j"

ComplexNumber.attr = 899
# # Create a new ComplexNumber object
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber()
print(c1.getData())
print(c2.getData())

print(c1.attr, c2.attr)
 
# print(c1.getData())
# print(c2.getData())
# print(c1.attr)
# print(c2.attr)
c1.attr = 777
print(c1.attr)
print(c2.attr)


# Call getData() function
# Output: 2+3j
# print(c1.getData(), c1.attr)
 
# Create another ComplexNumber object
# and create a new attribute 'attr'
# c2 = ComplexNumber(5)
# print(c2.getData(), c2.attr)

# c2.attr = 10

# print(c2.getData())
# print("c2", c2.attr)
# print("c1", c1.attr)



# # # Output: (5, 0, 10)
# print((c1.real, c1.imag, c2.attr))
# print((c1.real, c1.imag, c1.attr))

# print((c2.real, c2.imag))
# print((c1.real, c1.imag))
 
# # but c1 object doesn't have attribute 'attr'
# # AttributeError: 'ComplexNumber' object has no attribute 'attr'

# # print(c1.attr)