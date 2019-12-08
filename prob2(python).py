import numpy as np
def f(p1,p2,p3):
    A=np.array([[p1[0],p1[1],1],
               [p2[0],p2[1],1],
               [p3[0],p3[1],1]])
    B=np.array([[0-p1[0]**2-p1[1]**2],
               [0-p2[0]**2-p2[1]**2],
               [0-p3[0]**2-p3[1]**2]])
    V=np.linalg.solve(A,B)
    h=-V[0]/2
    k=-V[1]/2
    C=np.array([h,k])
    R=(((V[0]/2)**2+((V[1]/2))**2-(V[2])))**( 1/2)
    return C, R, V;
