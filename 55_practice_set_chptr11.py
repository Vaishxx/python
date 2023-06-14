#create a class c2dvector and use it to create another class representing a 3d vector.
class C2d_vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f'{i}i+{j}j')
class C3d_vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        print(f'{i}i+{j}j+{k}k')
v2=C2d_vector(10,12) 
v3=C3d_vector(12,39,49)               