import math
def gradient_descent(previous_x, previous_y, learning_rate, epoch):
    x_gd = []
    y_gd = []
    z_gd = []

    x_gd.append(previous_x)
    y_gd.append(previous_y)
    z_gd.append(func(previous_x, previous_y))

    # begin the loops to update x, y and z
    for i in range(epoch):
        current_x = previous_x - learning_rate*(2*previous_x/5. + previous_y/50.)
        x_gd.append(current_x)
        
        current_y = previous_y - learning_rate*(previous_x/50. + previous_y/5.)
        y_gd.append(current_y)

        z_gd.append(func(current_x, current_y))

        # update previous_x and previous_y
        previous_x = current_x
        previous_y = current_y

    return x_gd, y_gd, z_gd


def func(x,y):
    """
    Function to represent the function
    """
    return 2*pow(x,4)+pow(y,4)-2*pow(x,2)-2*pow(y,2)+4*math.sin(x*y)+5
