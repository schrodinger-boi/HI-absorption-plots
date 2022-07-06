import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
z=[]
v=[]
v0=[]
###Data file in source3.txt
with open('source3.txt') as f:
	lines = f.readlines()
	x = [float(line.split()[0]) for line in lines]
	y = [float(line.split()[1]) for line in lines]

plt.plot(x, y)
plt.title("Flux density vs freq of continuum subtracted data")
plt.xlabel("Freq (MHz)")
plt.ylabel("Flux (Jy)")
plt.show()

for j in range(len(x)):
	m=0
	m=((1420.4057-float(x[j]))/float(x[j]))*300000
	v.append(m)
	a=0
	a=66900.32804952598-m
	v0.append(a)

for i in range(len(y)):	
	n=0
	n=-(np.log(1+(float(y[i])/0.56)))
	z.append(n)
	n=0
 
plt.plot(v, y)
plt.title("Flux density")
plt.xlabel("Velocity (Km/s)")
plt.ylabel("Flux")
plt.show()

plt.plot(v0, y)
plt.title("Flux density")
plt.xlabel("Velocity w.r.to rest frame velocity (Km/s)")
plt.ylabel("Flux")
plt.show()


zmx1=max(z)
print("max value of optical depth", zmx1)
ymin=min(y)
print("min peak value of absorption flux", ymin)

plt.plot(x, z)
plt.title("Optical depth spectra with source flux density 0.56")
plt.xlabel("Freq (MHz)")
plt.ylabel("Optical depth")
plt.show()

plt.plot(v, z)
plt.title("Intergated optical depth spectra with source flux density 0.56")
plt.xlabel("Velocity (Km/s)")
plt.ylabel("Optical depth")
plt.show()

plt.plot(v0, z)
plt.title("Intergated optical depth spectra with source flux density 0.32")
plt.xlabel("Velocity w.r.to rest frame velocity(Km/s)")
plt.ylabel("Optical depth")
plt.show()



from scipy.integrate import simps
from numpy import trapz
l=len(v)
print("l=", l)
d=(v[0]-v[l-1])/len(v)
v0=np.array(v0)
z=np.array(z)
###Following mask is chosen so as to include only the main absorption line feature
mask=np.logical_and(v0>-300,v0<=450)
print("area", np.sum(z[mask])*d)
print("d=", d)
area = trapz(y, dx=d)
print("area trapz=", area)
area = simps(y, dx=d)
print("area simps=", area)
