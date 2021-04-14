from scipy.stats import norm
from csv import writer
import random as rnd
import numpy as np


def generate_points(num_points, locx, scalex, locy, scaley, locz, scalez, shift):
    distribution_x = norm(locx, scalex)
    distribution_y = norm(locy, scaley)
    distribution_z = norm(locz, scalez)
    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)
    points = zip(x+shift, y+shift, z+shift)
    return points


def generate_cylinder(number_points:int=10000,r=100,h=300,shift=0):
    xx=[]
    yy=[]
    zz=[]
    while(len(xx) < number_points):
        x = rnd.uniform(-1,1)*r
        y = rnd.uniform(-1,1)*np.sqrt(r**2-x**2)
        z = rnd.uniform(-1,1)*h
        xx.append(x+shift)
        yy.append(y+shift)
        zz.append(z+shift)
    return zip(xx,yy,zz)

#def generate_tube(r,n=2000,h=100,cx=0,cy=0,cz=0):

#    dx = uniform.(cx-r,cx+2*r)
#    dy = uniform(cy-r,cy+2*r)
#    dz = uniform(cz, cz+h)

#    n_corrected = int(np.ceil(n*4/np.pi))
#    px = dx.rvs(size=n_corrected)
#    py = dy.rvs(size=n_corrected)
 #   pz = dz.rvs(size=n_corrected)

  #  points = list(zip(px,py,pz))
 #   def filter_distances(point):
 #       section = (point[0]-cs)


if __name__=='__main__':
    cloud1_points=generate_points(1000,0,100,0,100,0,1,750)
    cloud2_points=generate_points(1000,0,1,0,100,0,100,-750)
    cylinder_points=generate_cylinder(1000)
    with open('cloud_points.xyz','w',encoding='utf-8',newline='\n') as csvfile:

        csvwriter=writer(csvfile)
        for p1 in cloud1_points:
            csvwriter.writerow(p1)
        for p2 in cloud2_points:
            csvwriter.writerow(p2)
        for p3 in cylinder_points:
            csvwriter.writerow(p3)