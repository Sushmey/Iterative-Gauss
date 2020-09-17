ax = int(input("Value of the only purely numeric term in x "))
cyx = int(input("Coeffcient of y in equation of x "))
czx = int(input("Coeffcient of z in equation of x "))
dx = int(input("Denominator of equation of x "))
print() #Line break
ay = int(input("Value of the only purely numeric term in y "))
cxy = int(input("Coeffcient of x in equation of y "))
czy = int(input("Coeffcient of z in equation of y "))
dy = int(input("Denominator of equation of y "))
print() #Line break
az = int(input("Value of the only purely numeric term in z "))
cxz = int(input("Coeffcient of x in equation of z "))
cyz = int(input("Coeffcient of y in equation of z "))
dz = int(input("Denominator of equation of z "))
print() #Line break
xi = float(input("Value of x "))
yi = float(input("Value of y "))
zi = float(input("Value of z "))
n = int(input("Up to how many decimals ? "))
xf=yf=zf=0.0
i=0
while(True):
    xi = (ax+cyx*yi+czx*zi)/dx 
    yi = (ay+cxy*xi+czy*zi)/dy
    zi = (az+cxz*xi+cyz*yi)/dz
    if(xf==round(xi,n) and yf==round(yi,n) and zf==round(zi,n)):
        break
    xf = round(xi,n)
    yf = round(yi,n)
    zf = round(zi,n)
    i+=1
    print ("Iteration no. {}:".format(i)) 
    print("""
          x = {0}
          y = {1}
          z = {2}
    """.format(xf,yf,zf))
print() #Line break  
print("Final x is: {}".format(xf))
print("Final y is: {}".format(yf))
print("Final z is: {}".format(zf))