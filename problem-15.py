#!/usr/bin/python

square_grid_size = 20

def get_next_points(current_points):
    new_points = []
    for point in current_points:
        # get down point if in bounds
        if point[1]+1 <= square_grid_size:
            point_down = [point[0], point[1]+1]
            new_points.append(point_down)
        # get right point if in bounds
        if point[0]+1 <= square_grid_size:
            point_right = [point[0]+1, point[1]]
            new_points.append(point_right)
    return new_points

if __name__ == '__main__':

    # starting point is a tuple
    starting_point = (0,0)

    # keep points in a list of tuples
    current_points = [starting_point]

    path_length = square_grid_size * 2
    for i in xrange(0,path_length):
        # print current_points
        current_points = get_next_points(current_points)

    print len(current_points)
