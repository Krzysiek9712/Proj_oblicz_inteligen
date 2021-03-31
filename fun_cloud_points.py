from scipy.stats import norm
from csv import writer


def generate_points_y(number_p:int=2000,location_y:int=0,scale_y:int=200,przesuniecie:int=0):
    x_points_d = norm(loc=0, scale=20)
    y_points_d = norm(loc=location_y, scale=scale_y)
    z_points_d = norm(loc=0.2, scale=0.05)

    x = x_points_d.rvs(size=number_p)
    y = y_points_d.rvs(size=number_p)
    z = z_points_d.rvs(size=number_p)

    points = zip(x+przesuniecie,y+przesuniecie,z+przesuniecie)
    return points

def generate_points_x(number_p:int=2000,location_x:int=0,scale_x:int=200,przesuniecie_x:int=0):
    x_points_d = norm(loc=location_x, scale=scale_x)
    y_points_d = norm(loc=0, scale=20)
    z_points_d = norm(loc=0.2, scale=0.05)

    x = x_points_d.rvs(size=number_p)
    y = y_points_d.rvs(size=number_p)
    z = z_points_d.rvs(size=number_p)

    points = zip(x+przesuniecie_x,y+przesuniecie_x,z+przesuniecie_x)
    return points

if(__name__ == '__main__'):
    cloud_points_y = generate_points_y(1500,0,200,750)
    cloud_points_x = generate_points_x(1500,0,200,-750)
    cloud_points_y2 = generate_points_y(1500, 0, 200, -150)

    with open('cloud_points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points_y:
            csvwriter.writerow(p)
        for py2 in cloud_points_y2:
            csvwriter.writerow(py2)
        for p_x in cloud_points_x:
            csvwriter.writerow(p_x)