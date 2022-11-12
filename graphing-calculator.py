from contextlib import nullcontext
from statistics import LinearRegression, linear_regression
from tkinter import Variable
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
operator1 = [1]
operator2 = [2]
operator3 = [3]
data_point_list_x = []
data_point_list_y = []
addition = ['+']
subtraction = ['-']
multiplication = ['*']
division = ['/']
exponentiation = ['^']
stop = ['done']
ys = []

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
if int(operation) in operator1 or operator2 or operator3:
    if operation == 1:
        print("Enter the x value, then the y value after pressing enter each time")
        print("up to 10 data points are allowed")
        print("if you want to stop entering data points, type 'done'")
        input("Press enter to continue...")
        number = 0
        i = 1
        while i < 11:
            number = int(number) + 1
            data_point_x = input("Enter the x value for your first data point: ")
            try:
                data_point_x = float(data_point_x)
            except ValueError:
                print("You have to type a number!")
                exit()

            data_point_list_x.append(data_point_x)
            data_point_y = input("Enter the y value for your first data point: ")
            try:
                data_point_y = float(data_point_y)
            except ValueError:
                print("You have to type a number!")
                exit()
            
            data_point_list_y.append(data_point_y)
            stop1 = input("Press enter to continue or done to stop...")
            if stop1 in stop:
                i = 11
            i = int(i) + 1
            
            
        print("The data points you entered: ")
        print(data_point_list_x)
        print(data_point_list_y)

        input("Press enter to continue...")





        def estimate_coef(x, y):
            # number of observations/points
            n = np.size(x)

            # mean of x and y vector
            m_x = np.mean(x)
            m_y = np.mean(y)

            # calculating cross-deviation and deviation about x
            SS_xy = np.sum(y*x) - n*m_y*m_x
            SS_xx = np.sum(x*x) - n*m_x*m_x

            # calculating regression coefficients
            b_1 = SS_xy / SS_xx
            b_0 = m_y - b_1*m_x

            return (b_0, b_1)


        def plot_regression_line(x, y, b):
            # plotting the actual points as scatter plot
            plt.scatter(x, y, color="m",
                        marker="o", s=30)

            # predicted response vector
            y_pred = b[0] + b[1]*x

            # plotting the regression line
            plt.plot(x, y_pred, color="g")

            # putting labels
            plt.xlabel('x')
            plt.ylabel('y')

            # function to show plot
            plt.show()


        def main():
            # observations / data
            x = np.array(data_point_list_x)
            y = np.array(data_point_list_y)

            # estimating coefficients
            b = estimate_coef(x, y)
            element = "Estimated coefficients:\nb_0 = {} \
                \nb_1 = {}".format(b[0], b[1])
            print(element)
            with open('Log.txt', 'a') as f:
                f.write(element)

            # plotting regression line
            plot_regression_line(x, y, b)


        if __name__ == "__main__":
            main()
        

    elif operation == 2:
        print("Enter a function solving for y")
        print("Put NO spaces in the function")
        print("If x has no coefficient, put 1")
        print("Example: y=2x+3")
        input("Press enter to continue...")
        function = input("Type in your function: ")
        
        # 100 linearly spaced numbers
        x = np.linspace(-5,5,100)

        # the function, which is y = x^2 here
        try:
            'y' and '=' in function
            
        except:
            print("Enter a valid function try again ")
            exit()
            
        def operatorReaction(x):
            if function[4] in addition:
                y_value = x + float(function[4:])
                ys.append(y_value)
                
            elif function[4] in subtraction:
                y_value = x - float(function[4])
                ys.append(y_value)
            
            elif function[4] in multiplication:
                y_value = x * float(function[4])
                ys.append(y_value)
                
            elif function[4] in division:
                y_value = x / float(function[4])
                ys.append(y_value)
            
            elif function[4] in exponentiation:
                y_value = x ** float(function[4])
                ys.append(y_value)
                
            else:
                print("Enter a valid function try again! ")
                exit()
                
        
        try:
            float(function[2])
        except:
            print("Enter a valid function try again. ")
            exit()
        
        x = float(function[2])*x
        posOfX = function.rfind('x')
        #coefficient = function[posOfX - 1]
        
        operatorReaction(x)
        #print(x)
        #print(ys)

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        vector = np.vectorize(np.int_)
        xr = np.array(x)
        xs = xr.astype(float)
        yr  =np.array(ys)
        y = yr.astype(float) 
        ys = np.reshape(y , (100, 1))
        plt.plot(xs ,ys, 'r')

        # show the plot
        plt.show()
            

else:
    print("You have to type an operation!?")
    exit()
