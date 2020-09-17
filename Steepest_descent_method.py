#Install "sympy" library in your machine before running this program
from sympy import *
#Steepest descent
x,y,a,z= symbols('x y a z') #z incase you have a three variable equation
grad = [] #To store the gradient
s = [] #To store the direction of the slope
temp = [] #Temporary variable
initial = [] #To store the initial answer to check with the final
result = [] #To store the final answer
n = 0 
decimals = 5 #Set the precision of your output here
variable = int(input("Enter the number of variables in the equation: "))
equa = input("Enter the expression: ") 
equation = sympify(equa) #Converting the input string to a mathematical expression
precision = int(input("Answer precision ? "))
decimals = precision
if(variable == 2):
    xi = float(input("Enter initial x coordinates: "))
    yi = float(input("Enter initial y coordinates: "))
    while(True):
         n+=1
         x_previous = xi
         y_previous = yi
         grad.append(diff(equation,x).subs([(x,xi),(y,yi)])) #To push the gradient wrt x in the list
         grad.append(diff(equation,y).subs([(y,yi),(x,xi)])) #To push the gradient wrt y in the list
         s.append(-grad[0]) #To push the x-coord of S-direction in the list
         s.append(-grad[1]) #To push the y-coord of S-direction in the list
         temp.append(xi + (a*s[0])) #To push the x-coord of xi equation in the list
         temp.append(yi + (a*s[1])) #To push the y-coord of yi equation in the list
         alphaEq = equation.subs([(x,temp[0]),(y,temp[1])]) #For brevity
         tempEq = Eq(diff(alphaEq,a),0) #Substituting and differentiating the eq with unknown alpha and equating with 0
         alpha = list(solveset(tempEq,a)) #Solving for alpha 
         xi = round(xi + (alpha[0]*s[0]),decimals) #Calculating the new x-coords
         yi = round(yi + (alpha[0]*s[1]),decimals) #Calculating the new y-coords
         result.append(diff(equation,x).subs([(x,xi),(y,yi)]))
         result.append(diff(equation,y).subs([(x,xi),(y,yi)]))
         print("""
                Iteration no. {3}
                    gradient : {4}
                    x is : {0}
                    y is : {1}
                    a is : {2}

         """.format(xi,yi,round(alpha[0],decimals),n,grad))
         if((result[0]==0) and (result[1]==0)):
            #print("Exit by 1") #To let the user know which condition caused it to stop
            break
         elif((x_previous==xi) and (y_previous==yi)):
            #print("Exit by 2") 
            break    
         # elif(n>19): #Incase you want to set a limit to the number of iterations
         #    break   
         grad.clear()   #Clearing all the lists
         result.clear()
         s.clear()
         temp.clear()   
elif(variable == 3):
    xi = float(input("Enter initial x coordinates: "))
    yi = float(input("Enter initial y coordinates: "))
    zi = float(input("Enter initial z coordinates: "))
    while(True):
         n+=1
         x_previous = xi
         y_previous = yi
         z_previous = zi
         grad.append(diff(equation,x).subs([(x,xi),(y,yi),(z,zi)])) #To push the gradient wrt x in the list
         grad.append(diff(equation,y).subs([(x,xi),(y,yi),(z,zi)])) #To push the gradient wrt y in the list
         grad.append(diff(equation,z).subs([(x,xi),(y,yi),(z,zi)])) #To push the gradient wrt z in the list
         s.append(-grad[0]) #To push the x-coord of S-direction in the list
         s.append(-grad[1]) #To push the y-coord of S-direction in the list
         s.append(-grad[2]) #To push the z-coord of S-direction in the list
         temp.append(xi + (a*s[0])) #To push the x-coord of xi equation in the list
         temp.append(yi + (a*s[1])) #To push the y-coord of yi equation in the list
         temp.append(zi + (a*s[2])) #To push the z-coord of zi equation in the list
         alphaEq = equation.subs([(x,temp[0]),(y,temp[1]),(z,temp[2])]) #For brevity
         tempEq = Eq(diff(alphaEq,a),0) #Substituting and differentiating the eq with unknown alpha and equating with 0
         alpha = list(solveset(tempEq,a)) #Solving for alpha 
         xi = round(xi + (alpha[0]*s[0]),decimals) #Calculating the new x-coords
         yi = round(yi + (alpha[0]*s[1]),decimals) #Calculating the new y-coords
         zi = round(zi + (alpha[0]*s[2]),decimals) #Calculating the new z-coords
         result.append(diff(equation,x).subs([(x,xi),(y,yi),(z,zi)]))
         result.append(diff(equation,y).subs([(x,xi),(y,yi),(z,zi)]))
         result.append(diff(equation,z).subs([(x,xi),(y,yi),(z,zi)]))
         print(result)
         print("""
                Iteration no. {4}
                    gradient : {5}
                    x is : {0}
                    y is : {1}
                    z is : {2}
                    a is : {3}

         """.format(xi,yi,zi,round(alpha[0],decimals),n,grad))
         if(((result[0]==0) and (result[1]==0)) and (result[2]==0)):
            print("Exit by 1") #To let the user know which condition caused it to stop
            break
         elif(((x_previous==xi) and (y_previous==yi)) and (z_previous==zi)):
            print("Exit by 2") 
            break    
         # elif(n>19): #Incase you want to set a limit to the number of iterations
         #    break   
         grad.clear()   #Clearing all the lists
         result.clear()
         s.clear()
         temp.clear()              


