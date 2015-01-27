from pylab import *
x, y = np.loadtxt('ebola.csv', delimiter=',', converters = {2: lambda s: float(s.strip() or 0)}, skiprows = 1, usecols=(1, 2), unpack=True)

for i in range(len(y)-1,0,-1):
  if (y[i] != 0.0):
    v = y[i]
  else:
    y[i] = v

x, z = np.loadtxt('ebola.csv', delimiter=',', converters = {3: lambda s: float(s.strip() or 0)}, skiprows = 1, usecols=(1, 3), unpack=True)
for i in range(len(z)-1,0,-1):
  if (z[i] != 0.0):
    v = z[i]
  else:
    z[i] = v

plot(x,y)
plot(x,z)
show()
