from contextlib import nullcontext
from statistics import LinearRegression, linear_regression
from tkinter import Variable
import numpy as np
import matplotlib.pyplot as plt
operator1 = [1]
operator2 = [2]
operator3 = [3]
stop = ['done']


print("Welcome to the graphing calculator!")
print("the following operations are supported:")
print("1. linear regression")
print("2. plot a graph")
print("3. graph a function")
input("Press enter to continue...")
operation = input("Enter in the operation you want to perform: ")
try:
    operation = int(operation)
except ValueError:
    print("You have to type a number!")
    exit()
if int(operation) in operator1:
    plt.figure(figsize=(10, 6))
    if operation == 1:
        print("Enter the x value, then the y value after pressing enter each time")
        print("up to 10 data points are allowed")
        print("if you want to stop entering data points, type 'done'")
        input("Press enter to continue...")
        dp1x = input("Enter the x value for your first data point: ")
        try:
            dp1x = float(dp1x)
            pass
        except ValueError:
            print("You have to type a number!")
            exit()
        dp1y = input("Enter the y value for your first data point: ")
        try:
            dp1y = float(dp1y)
        except ValueError:
            print("You have to type a number!")
            exit()
        stop1 = input("Press enter to continue or done to stop...")
        if stop1 in stop:
            dp2x = None
            dp3x = None 
            dp4x = None
            dp5x = None
            dp6x = None
            dp7x = None
            dp8x = None
            dp9x = None
            dp10x = None
            dp2y = None
            dp3y = None 
            dp4y = None
            dp5y = None
            dp6y = None
            dp7y = None
            dp8y = None
            dp9y = None
            dp10y = None
            pass
        


        else:
            dp2x = input("Enter the x value for your data point: ")
            try:
                dp2x = float(dp2x)
                pass
            except ValueError:
                print("You have to type a number!")
                exit()
            dp2y = input("Enter the y value for your data point: ")
            try:
                dp2y = float(dp2y)
            except ValueError:
                print("You have to type a number!")
                exit()
            stop2 = input("Press enter to continue or done to stop...")
            if stop2 in stop:
                dp3x = None 
                dp4x = None
                dp5x = None
                dp6x = None
                dp7x = None
                dp8x = None
                dp9x = None
                dp10x = None
                dp3y = None 
                dp4y = None
                dp5y = None
                dp6y = None
                dp7y = None
                dp8y = None
                dp9y = None
                dp10y = None
                pass

            else:
                dp3x = input("Enter the x value for your data point: ")
                try:
                    dp3x = float(dp3x)
                    pass
                except ValueError:
                    print("You have to type a number!")
                    exit()
                dp3y = input("Enter the y value for your data point: ")
                try:
                    dp3y = float(dp3y)
                except ValueError:
                    print("You have to type a number!")
                    exit()
                stop3 = input("Press enter to continue or done to stop...")
                if stop3 in stop:
                    dp4x = None
                    dp5x = None
                    dp6x = None
                    dp7x = None
                    dp8x = None
                    dp9x = None
                    dp10x = None
                    dp4y = None
                    dp5y = None
                    dp6y = None
                    dp7y = None
                    dp8y = None
                    dp9y = None
                    dp10y = None
                    pass

                else:
                    dp4x = input("Enter the x value for your data point: ")
                    try:
                        dp4x = float(dp4x)
                        pass
                    except ValueError:
                        print("You have to type a number!")
                        exit()
                    dp4y = input("Enter the y value for your data point: ")
                    try:
                        dp4y = float(dp4y)
                    except ValueError:
                        print("You have to type a number!")
                        exit()
                    stop4 = input("Press enter to continue or done to stop...")
                    if stop4 in stop:
                        dp5x = None
                        dp6x = None
                        dp7x = None
                        dp8x = None
                        dp9x = None
                        dp10x = None
                        dp5y = None
                        dp6y = None
                        dp7y = None
                        dp8y = None
                        dp9y = None
                        dp10y = None
                        pass

                    else:
                        dp5x = input("Enter the x value for your data point: ")
                        try:
                            dp5x = float(dp5x)
                            pass
                        except ValueError:
                            print("You have to type a number!")
                            exit()
                        dp5y = input("Enter the y value for your data point: ")
                        try:
                            dp5y = float(dp5y)
                        except ValueError:
                            print("You have to type a number!")
                            exit()
                        stop5 = input("Press enter to continue or done to stop...")
                        if stop5 in stop:
                            dp6x = None
                            dp7x = None
                            dp8x = None
                            dp9x = None
                            dp10x = None
                            dp6y = None
                            dp7y = None
                            dp8y = None
                            dp9y = None
                            dp10y = None
                            pass

                        else:
                            dp6x = input("Enter the x value for your data point: ")
                            try:
                                dp6x = float(dp6x)
                                pass
                            except ValueError:
                                print("You have to type a number!")
                                exit()
                            dp6y = input("Enter the y value for your data point: ")
                            try:
                                dp6y = float(dp6y)
                            except ValueError:
                                print("You have to type a number!")
                                exit()
                            stop6 = input("Press enter to continue or done to stop...")
                            if stop6 in stop:
                                dp7x = None
                                dp8x = None
                                dp9x = None
                                dp10x = None
                                dp7y = None
                                dp8y = None
                                dp9y = None
                                dp10y = None
                                pass

                            else:
                                dp7x = input("Enter the x value for your data point: ")
                                try:
                                    dp7x = float(dp7x)
                                    pass
                                except ValueError:
                                    print("You have to type a number!")
                                    exit()
                                dp7y = input("Enter the y value for your data point: ")
                                try:
                                    dp7y = float(dp7y)
                                except ValueError:
                                    print("You have to type a number!")
                                    exit()
                                stop7 = input("Press enter to continue or done to stop...")
                                if stop7 in stop:
                                    dp8x = None
                                    dp9x = None
                                    dp10x = None
                                    dp8y = None
                                    dp9y = None
                                    dp10y = None
                                    pass

                                else:
                                    dp8x = input("Enter the x value for your data point: ")
                                    try:
                                        dp8x = float(dp8x)
                                        pass
                                    except ValueError:
                                        print("You have to type a number!")
                                        exit()
                                    dp8y = input("Enter the y value for your data point: ")
                                    try:
                                        dp8y = float(dp8y)
                                    except ValueError:
                                        print("You have to type a number!")
                                        exit()
                                    stop8 = input("Press enter to continue or done to stop...")
                                    if stop8 in stop:
                                        dp9x = None
                                        dp10x = None
                                        dp9y = None
                                        dp10y = None
                                        pass

                                    else:
                                        dp9x = input("Enter the x value for your data point: ")
                                        try:
                                            dp9x = float(dp9x)
                                            pass
                                        except ValueError:
                                            print("You have to type a number!")
                                            exit()
                                        dp9y = input("Enter the y value for your data point: ")
                                        try:
                                            dp9y = float(dp9y)
                                        except ValueError:
                                            print("You have to type a number!")
                                            exit()
                                        stop9 = input("Press enter to continue or done to stop...")
                                        if stop9 in stop:
                                            dp10x = None
                                            dp10y = None
                                            pass

                                        else:
                                            dp10x = input("Enter the x value for your data point: ")
                                            try:
                                                dp10x = float(dp10x)
                                                pass
                                            except ValueError:
                                                print("You have to type a number!")
                                                exit()
                                            dp10y = input("Enter the y value for your data point: ")
                                            try:
                                                dp10y = float(dp10y)
                                            except ValueError:
                                                print("You have to type a number!")
                                                exit()
                                            pass
                                        


else:
    print("You have to type an operation!")
    exit()
print("The data points you entered: ")
print(dp2x,dp2y)
print(dp3x,dp3y)
print(dp4x,dp4y)
print(dp5x, dp5y)
print(dp6x, dp6y)
print(dp7x, dp7y)
print(dp8x, dp8y)
print(dp9x, dp9y)
print(dp10x,dp10y)
input("Press enter to continue...")


        
dp2x = float(dp2x)
dp2y = float(dp2y)
dp3x = float(dp3x)
dp3y = float(dp3y)
dp4x = float(dp4x)
dp4y = float(dp4y)
dp5x = float(dp5x)
dp5y = float(dp5y)
dp6x = float(dp6x)
dp6y = float(dp6y)
dp7x = float(dp7x)
dp7y = float(dp7y)
dp8x = float(dp8x)
dp8y = float(dp8y)
dp9x = float(dp9x)
dp9y = float(dp9y)
dp10x = float(dp10x)
dp10y = float(dp10y)



# def estimate_coef(x, y):
#     # number of observations/points
#     n = np.size(x)
  
#     # mean of x and y vector
#     m_x = np.mean(x)
#     m_y = np.mean(y)
  
#     # calculating cross-deviation and deviation about x
#     SS_xy = np.sum(y*x) - n*m_y*m_x
#     SS_xx = np.sum(x*x) - n*m_x*m_x
  
#     # calculating regression coefficients
#     b_1 = SS_xy / SS_xx
#     b_0 = m_y - b_1*m_x
  
#     return (b_0, b_1)
  
# def plot_regression_line(x, y, b):
#     # plotting the actual points as scatter plot
#     plt.scatter(x, y, color = "m",
#                marker = "o", s = 30)
  
#     # predicted response vector
#     y_pred = b[0] + b[1]*x
  
#     # plotting the regression line
#     plt.plot(x, y_pred, color = "g")
  
#     # putting labels
#     plt.xlabel('x')
#     plt.ylabel('y')
  
#     # function to show plot
#     plt.show()
  
# def main():
#     # observations / data
#     x = np.array([dp1x, dp2x, dp3x, dp4x, dp5x, dp6x, dp7x, dp8x, dp9x, dp10x])
#     y = np.array([dp1y, dp2y, dp3y, dp4y, dp5y, dp6y, dp7y, dp8y, dp9y, dp10y])
  
#     # estimating coefficients
#     b = estimate_coef(x, y)
#     print("Estimated coefficients:\nb_0 = {}  \
#           \nb_1 = {}".format(b[0], b[1]))
  
#     # plotting regression line
#     plot_regression_line(x, y, b)
  
# if __name__ == "__main__":
#     main()


    
    
    