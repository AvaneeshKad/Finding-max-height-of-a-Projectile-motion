import math

#Making lists first

V = [10, 20, 30, 40, 50] #m/s
A = [30, 45, 60] #deg
P = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]] #table


#Pseudocode :-
#The list is ready
#Now, using the formula of H_max, compute the values
#Use of for loop to calculate the values on the table
#Enter those values in the 2-D list created already (P)
# Print in a table format

for i in range(len(A)):
    for k in range(len(V)):
        H_max = ((V[k] ** 2 ) * (math.sin(A[i])** 2)) / (2 * 9.81)
        P[i][k] = H_max #Subsituiting value inside the 2D lsit


#Printing in a table format using '\t' (Tab) in the print statement
print("\t{0}\t{1}\t{2}\t{3}\t{4}".format(V[0], V[1], V[2], V[3], V[4]))
for j in range(len(A)):
    print("{0}\t{1:0.2f}\t{2:0.2f}\t{3:0.2f}\t{4:0.2f}\t{5:0.2f}".format(A[j], P[j][0], P[j][1],P[j][2],P[j][3], P[j][4]) )                 


                                                







                                                
