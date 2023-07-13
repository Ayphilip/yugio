
def factorial():
    print("Factorial \n")
    num = int(input("Input a number: "))
    default_number = 1
    for i in range(1, num+1):
        default_number = default_number * i
        print(default_number)
    print("The result is " + str(default_number))


def func(x, y):
    return (x * y)


def picards():
    print("Picards Method")
    x0 = float(input("Input the initial value of x(x0): "))
    xn = float(input("Input the final value of x(xn): "))
    h = float(input("Input the initial value of the range(h): "))
    while x0 < xn:
        y1 = (1 + (x0) + pow(x0, 2)/2)
        y2 = (1 + x0 + pow(x0, 2) + (pow(x0, 3)/6))
        y3 = (1 + x0 + pow(x0, 2) + (pow(x0, 3)/3) + (pow(x0, 4)/24))
        y4 = (1 + x0 + pow(x0, 2) + (pow(x0, 3)/3) +
              (pow(x0, 4)/12) + (pow(x0, 5)/120))
        y5 = (1 + x0 + pow(x0, 2) + (pow(x0, 3)/3) +
              (pow(x0, 4)/12) + (pow(x0, 5)/60) + (pow(x0, 6)/720))
        print(y1, y2, y3, y4, y5)
        x0 = x0 + h
    print("End of Iteration")


def euler():
    print("Euler's Method \n")

    x0 = float(input("Input the initial value of x(x0): "))
    y = float(input("Input the initial value of y(y0): "))
    h = float(input("Input the initial value of the range(h): "))

    x = float(input("Input the final stage of approximation needed: "))

    temp = 0

    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        print(y)
        x0 = x0 + h

    print("Approximate solution at x = ", x, " is ", "%.6f" % y)


def rungekutta():
    print("Runge Kutta Method\n")
    rk_method = input(
        "Kindly select which RK order(1-4) \n 1. First Order \n 2. Second Order \n 3. Third Order \n 4. Fourth Order \n you choose: ")
    if rk_method == "1":
        print("RK First Order Method \n")

        x0 = float(input("Input the initial value of x(x0): "))
        y = float(input("Input the initial value of y(y0): "))
        h = float(input("Input the initial value of the range(h): "))

        x = float(input("Input the final stage of approximation needed: "))

        temp = 0

        while x0 < x:
            temp = y
            y = y + h * func(x0, y)
            print(y)
            x0 = x0 + h

        print("Approximate solution at x = ", x, " is ", "%.6f" % y)
    if rk_method == "2":
        x0 = float(input("Input the initial value of x(x0): "))
        y = float(input("Input the initial value of y(y0): "))
        h = float(input("Input the initial value of the range(h): "))
        s1 = func(x0, y)
        s2 = func((x0 + h), (y + (h * s1)))
        print(s1, s2)
        x = float(input("Input the final stage of approximation needed: "))
        temp = 0
        while x0 < x:
            temp = y
            y = y + h * ((s1+s2)/2)
            print(y)
            x0 = x0 + h
        print("Approximate solution at x = ", x, " is ", "%.6f" % y)
    if rk_method == "3":
        x0 = float(input("Input the initial value of x(x0): "))
        y = float(input("Input the initial value of y(y0): "))
        h = float(input("Input the initial value of the range(h): "))
        s1 = func(x0, y)
        s2 = func((x0 + h), (y + (h * s1)))
        s3 = func((x0 + (h / 2)), (y + (h/2)(s1 + s2)/2))
        print(s1, s2, s3)
        x = float(input("Input the final stage of approximation needed: "))
        temp = 0
        while x0 < x:
            temp = y
            y = y + h * ((s1+s2+(4*s3))/6)
            print(y)
            x0 = x0 + h
        print("Approximate solution at x = ", x, " is ", "%.6f" % y)
    if rk_method == "4":
        x0 = float(input("Input the initial value of x(x0): "))
        y = float(input("Input the initial value of y(y0): "))
        h = float(input("Input the initial value of the range(h): "))
        s1 = func(x0, y)
        s2 = func((x0 + (h/2)), (y + ((h/2)*s1)))
        s3 = func((x0 + (h/2)), (y + ((h/2)*s2)))
        s4 = func((x0 + h), (y + (h*s3)))
        print(s1, s2, s3, s4)
        x = float(input("Input the final stage of approximation needed: "))
        temp = 0
        while x0 < x:
            temp = y
            y = y + h * ((s1+(2 * s2)+(2*s3) + s4)/6)
            print(y)
            x0 = x0 + h
        print("Approximate solution at x = ", x, " is ", "%.6f" % y)
    else:
        print("Wrong Input")
        rungekutta()


initial = input("Which differential method are you hoping to solve: \n 0. Factorial \n 1. Picards method \n 2. Euler's Method \n 3. Taylor's Series Method \n 4. Runge Kutta Method \n You choose: ")
if initial == "0":
    factorial()
if initial == "1":
    picards()
if initial == "2":
    euler()
if initial == "4":
    rungekutta()
else:
    print("Wrong Input")
