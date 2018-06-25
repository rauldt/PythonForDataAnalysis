<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Name: Raul David Torres Aragon

"""

# import numpy
import numpy as np


# 2. create a 3x5 matrix with random numbers
A = np.random.random(15)
A.shape = (3,5)

# 3. find the size and length of A
print(A.size) #<-size
print(len(A)) #<-length

# 4. slice matrix to size (3,4)
A = A[:3,[0,1,2,3]]
A.shape
A = np.matrix(A)

# 5. find the transpose of A and assign it to B
B = A.T

# 6. find the minimum value in column 1 of matrix B
print(B[:3,[0]].min())

# 7. find the min and max for the entire matrix A
print(A.min())
print(A.max())

# 8. create a vector with four random numbers
X = np.random.random(4)

# 9-10. create a function and pass vector X and matrix A
def my_multiply(X, A):
    try:
        X*A
        return X*A
    except ValueError:
        print("ugh, looks like the matrices do not conform for multiplication")
   

my_multiply(X, A) 
X.shape = (4, 1)
D = my_multiply(A, X)
print(D)

# 11. Create a complex number Z with absolute and real parts not equal to 0
Z = complex(1,2) #1 + 2j
print(type(Z))
 
# 12. Show its real and imaginary parts as well as it;s absolute value
print(Z.imag)
print(Z.real)
print(np.absolute(Z))
 
# 13. multiply result D with the absolute value of Z and record it in C
C = D * np.absolute(Z)
 
# 14. Convert matrix B from a matrix to a string  
B = str(B)
print(type(B))
 
# 15. 
print("Raul Torres Aragon is done with HW2")
 
 
 
 
 
 
 
=======
# -*- coding: utf-8 -*-
"""
Name: Raul David Torres Aragon

"""

# import numpy
import numpy as np


# 2. create a 3x5 matrix with random numbers
A = np.random.random(15)
A.shape = (3,5)

# 3. find the size and length of A
print(A.size) #<-size
print(len(A)) #<-length

# 4. slice matrix to size (3,4)
A = A[:3,[0,1,2,3]]
A.shape
A = np.matrix(A)

# 5. find the transpose of A and assign it to B
B = A.T

# 6. find the minimum value in column 1 of matrix B
print(B[:3,[0]].min())

# 7. find the min and max for the entire matrix A
print(A.min())
print(A.max())

# 8. create a vector with four random numbers
X = np.random.random(4)

# 9-10. create a function and pass vector X and matrix A
def my_multiply(X, A):
    try:
        X*A
        return X*A
    except ValueError:
        print("ugh, looks like the matrices do not conform for multiplication")
   

my_multiply(X, A) 
X.shape = (4, 1)
D = my_multiply(A, X)
print(D)

# 11. Create a complex number Z with absolute and real parts not equal to 0
Z = complex(1,2) #1 + 2j
print(type(Z))
 
# 12. Show its real and imaginary parts as well as it;s absolute value
print(Z.imag)
print(Z.real)
print(np.absolute(Z))
 
# 13. multiply result D with the absolute value of Z and record it in C
C = D * np.absolute(Z)
 
# 14. Convert matrix B from a matrix to a string  
B = str(B)
print(type(B))
 
# 15. 
print("Raul Torres Aragon is done with HW2")
 
 
 
 
 
 
 
>>>>>>> ba0d9db88c50a39f425f6fd587bebe9f2a5e8b5f
 