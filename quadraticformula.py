import math
from matplotlib import pyplot as plt
import numpy as np

#Works only with int numbers
#Leave 1 if no cofficient.
#print("\n")
print("Enter a: Coefficient of the x² term")
a = int(input())
if a == 0:
    raise Exception("The equation is linear because a = 0.")
print("Enter b: Coefficient of the x term.")
b = int(input())
print("Enter c: Constant term.")
c = int(input())



D = int(b ** 2 - 4 * a * c)




if a <0:
    ae = f"({a})"
else:
    ae = a

if b <0:
    be = f"({b})"
else:
    be = b

if c <0:
    ce = f"({c})"
else:
    ce = c

exp = str(ae) + "x²+ " + str(be) + "x + " + str(ce) + " = 0"
print(f"\n Expression: \n {exp}")

print(f"\n D : \n {be}² - 4 • {ae} • {ce} = {D} \n")


#
# def simplifyfraction(numberone: int,numbertwo: int):
#     simplifiedone, simplifiedtwo = numberone // math.gcd(numberone, numbertwo), numbertwo // math.gcd(numberone, numbertwo)
#     return "".join([str(simplifiedone),"/", str(simplifiedtwo)])


def simplify(number: int): # simplify by finding largest perfect square factor
    if math.sqrt(number) % 1 == 0: #If the discriminant is a square number
        return "".join(["√", str(number)])

    max_i = 0
    for i in range(1, number):
        if number % i == 0 and math.sqrt(i) % 1 == 0 and max_i < i:
            max_i = i
    #print(max_i)
    if max_i > 1:
        simplified = "".join([str(int(math.sqrt(max_i))), "√", str(int(number / max_i))]) # example 5√2 from √50
        return simplified
    else:
        return "".join(["√", str(number)]) #√17

minusB = -b
twoA = 2 * a
# √±
if D > 0:
    rootd = math.sqrt(D)


    print("There are two roots.")

    simplifiedD = simplify(D)
    print(f"    -{be} ± {simplifiedD}")
    print(f"x = ---------------------")
    print(f"            2 • {ae}")


    print(f"    |(-{be}+{rootd})/2 • {ae} = {minusB + rootd}/{twoA}= {(minusB + rootd) / twoA}")
    print(f"x = |")
    print(f"    |(-{be}-{rootd})/2 • {ae} = {minusB - rootd}/{twoA}= {(minusB - rootd) / twoA}")

elif D == 0:
    print("There is one root.")

    print(f"x = -{be}/ (2 • {ae}) = {minusB}/{twoA} = {minusB/twoA}")

else:
    print("The expression is incorrect.")

x = np.array(range(-10, 12))


plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(color="gray", alpha=1, linestyle='--')

plt.plot(x, (a * x) ** 2 + (b * x) + c)
plt.plot(x, x*0) #line, at the points of intersection we have x

plt.title(exp)

plt.show()