#解二次方程使用异常处理机制的升级版
import math
def main():
    print("This program finds the real solutions to a quadratic.\n")

    try:
        a,b,c = eval(input("Please input the params inorder(a,b,c):"))
        discRoot = math.sqrt(b**2-4*a*c)
        root1 = (-b+discRoot)/(2*a)
        root2 = (-b-discRoot)/(2*a)

        print("Root1 = ",root1)
        print("Root2 = ",root2)

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots")

        else:
            print("You give me the wrong digits")

    except NameError:
        print("\nYou don't give me three numbers")

    except TypeError:
        print("\nYour inputs were not all numbers.")

    except SyntaxError:
        print("\nPlease input the comma between numbers")

    except:
        print("\nSomething went wrong,sorry!")

main()
