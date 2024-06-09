import calc
 
def test_add():
    if calc.add(1, 2) == 3:
        print("Test add(a, b) is Passed")
    else:
        print("Test add(a, b) is Failed")
        
def test_sub():
    if calc.sub(4, 2) == 2:
        print("Test sub(a, b) is Passed")
    else:
        print("Test sub(a, b) is Failed")
 
def test_mul():
    if calc.mul(2, 5) == 10:
        print("Test mul(a, b) is Passed")
    else:
        print("Test mul(a, b) is Failed")
 
def test_div():
    if calc.div(8, 4) == 2.0:
        print("Test div(a, b) is Passed")
    else:
        print("Test div(a, b) is Failed")       

test_add()
test_sub()
test_mul()
test_div()

