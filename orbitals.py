import numpy
import math
import matplotlib.pyplot as plt

import scipy.special
from scipy.special import sph_harm


#get quantum numbers

n,l,m=input("input n , l , m: ").split(",")
n,l,m=int(n),int(l),int(m)


#find hydrogen wave function

def hydrogen_wf(n,l,m,X,Y,Z):
    R = numpy.sqrt(X**2+Y**2+Z**2)
    Theta = numpy.arccos(Z/R)
    Phi = numpy.arctan2(Y,X)
    
    rho = 2.*R/n
    s_harmonic=sph_harm(m, l, Phi, Theta)                                          #spherical harmonic part
    lagguere = scipy.special.genlaguerre(n-l-1,2*l+1)(rho)                         #lagerre polynomial
    
    Radial = numpy.sqrt((2./n)**3*math.factorial(n-l-1)/(2.*n*math.factorial(n+l)))#radial formula
    wf = Radial*numpy.exp(-rho/2.)*rho**l*s_harmonic*lagguere                      #combining spherical harmonics and radial 
    wf = numpy.nan_to_num(wf)
    return wf
  
# range of diffrent x-y-z 
dz=0.5
zmin=-10
zmax=10

x = numpy.arange(zmin,zmax,dz)
y = numpy.arange(zmin,zmax,dz)
z = numpy.arange(zmin,zmax,dz)
elements = []
probability = []

#find probability for diffrent x-y-z and n , l , m that we have as inputes
for ix in x:
    for iy in y:
        for iz in z:
            #Serialize into 1D object
            elements.append(str((ix,iy,iz)))
            probability.append(abs(hydrogen_wf(n,l,m,ix,iy,iz))**2)                  #(wave function)^2=probability 


#normalizing probability 
probability = probability/sum(probability)

#coordinates 
coord = numpy.random.choice(elements, size=100000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = numpy.matrix(elem_mat)
x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]


#Plotting
fig = plt.figure(figsize=(10,10))
my_cmap = plt.get_cmap('hsv')
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.05, s=2, cmap = my_cmap)
ax.set_title(f"Hydrogen orbital witn n={n} , l={l} , m={m}")
plt.show()
