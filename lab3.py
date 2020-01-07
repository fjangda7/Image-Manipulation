import utilities


def rotate_90_degrees(image_array, direction=1):

    # 1 for clock_wise. -1 for anticlockwise

    number_of_rows = len(image_array)
    new_image = []

    number_of_columns = len(image_array[0])

    #rotate clockwise
    if direction == 1: 

        image_array.reverse()

        for column in range(number_of_columns):
            new_pixel = []

            for row in range(number_of_rows):
                new_pixel.append(image_array[row][column])

            new_image.append(new_pixel)
    
    #rotate counter clockwise or, clockwise 3 times 
    else: 
    
        #reverse order
        for column in range(number_of_columns - 1, -1, -1):
            new_pixel = []

            for row in range(number_of_rows):
                new_pixel.append(image_array[row][column])

            new_image.append(new_pixel)

    return new_image

#utilities.write_image(rotate_90_degrees(utilities.image_to_list("surprised_pikachu.png"), -1), "ccwsurprised_pikachu.png")
#utilities.write_image(rotate_90_degrees(utilities.image_to_list("surprised_pikachu.png"), 1), "cwsurprised_pikachu.png")

#utilities.write_image(rotate_90_degrees(utilities.image_to_list("robot.png"), -1), "ccwrobot.png")
#utilities.write_image(rotate_90_degrees(utilities.image_to_list("robot.png"), 1), "cwrobot.png")

#utilities.write_image(rotate_90_degrees(utilities.image_to_list("square.jpg"), -1), "ccwsquare.png")
#utilities.write_image(rotate_90_degrees(utilities.image_to_list("square.jpg"), 1), "cwsquare.png")

def flip_image(image_array, axis=0):
    number_of_rows = len(image_array)
    new_image = []

    number_of_columns = len(image_array[0])

    if axis == -1: 
        #flip along x = y

        for column in range (number_of_columns -1, -1, -1):

            new_row = []

            for row in range (number_of_rows -1, -1, -1):

                new_row.append(image_array[row][column])

            new_image.append(new_row)

    elif axis == 0: 
        #flip along y

        for row in range(number_of_rows):

            new_row = []

            for column in range (number_of_columns -1, -1, -1):

                new_row.append(image_array[row][column])

            new_image.append(new_row)
    else:
        #flip along x
        for row in range(number_of_rows -1, -1, -1): 
            new_image.append(image_array[row])


    return new_image

#utilities.write_image(flip_image(utilities.image_to_list("square.jpg"), 0), "ysquare.png")
#utilities.write_image(flip_image(utilities.image_to_list("square.jpg"), -1), "xysquare.png")
#utilities.write_image(flip_image(utilities.image_to_list("square.jpg"), 1), "xsquare.png")

#utilities.write_image(flip_image(utilities.image_to_list("robot.png"), 0), "yrobot.png")
#utilities.write_image(flip_image(utilities.image_to_list("robot.png"), -1), "xyrobot.png")
#utilities.write_image(flip_image(utilities.image_to_list("robot.png"), 1), "xrobot.png")

#utilities.write_image(flip_image(utilities.image_to_list("surprised_pikachu.png"), 0), "ysp.png")
#utilities.write_image(flip_image(utilities.image_to_list("surprised_pikachu.png"), -1), "xysp.png")
#utilities.write_image(flip_image(utilities.image_to_list("surprised_pikachu.png"), 1), "xsp.png")

def invert_grayscale(image_array):

    number_of_rows = len(image_array)
    number_of_columns = len(image_array[0])

    for row in range(number_of_rows):

        for column in range(number_of_columns):

                image_array[row][column] = 255 - image_array[row][column]

    return image_array

#utilities.write_image(invert_grayscale(utilities.image_to_list("graysquare.png")), "igsquare.png")
#utilities.write_image(invert_grayscale(utilities.image_to_list("grayrobot.png")), "igrobot.png")
#utilities.write_image(invert_grayscale(utilities.image_to_list("graysp.png")), "igsp.png")

def crop(image_array, direction, n_pixels):
    #remove n pixels from image array from the direction specified.

    number_of_rows = len(image_array)
    number_of_columns = len(image_array[0])

    new_image = []
    
    if direction == "left": 

        new_image = rotate_90_degrees(image_array, -1)
        new_image = crop(new_image, "down", n_pixels)
        new_image = rotate_90_degrees(new_image, 1)

    elif direction == "right":

        new_image = rotate_90_degrees(image_array, -1)
        new_image = crop(new_image, "up", n_pixels)
        new_image = rotate_90_degrees(new_image, 1)

    elif direction == "down":

        for row in range(number_of_rows - n_pixels):

           new_image.append(image_array[row])

    else: 

        for row in range(n_pixels, number_of_rows):

            new_image.append(image_array[row])

    return new_image

#file = 'robot.png'
#utilities.write_image(crop(utilities.image_to_list(file), "down", 150), 'cropdownrobot.png')
#utilities.write_image(crop(utilities.image_to_list(file), "up", 150), 'cropuprobot.png')
#utilities.write_image(crop(utilities.image_to_list(file), "left", 50), 'cropleftrobot.png')
#utilities.write_image(crop(utilities.image_to_list(file), "right", 50), 'croprightrobot.png')

#file = 'square.jpg'
#utilities.write_image(crop(utilities.image_to_list(file), "down", 150), 'cropdownsquare.png')
#utilities.write_image(crop(utilities.image_to_list(file), "up", 150), 'cropupsquare.png')
#utilities.write_image(crop(utilities.image_to_list(file), "left", 150), 'cropleftsquare.png')
#utilities.write_image(crop(utilities.image_to_list(file), "right", 150), 'croprightsquare.png')

#file = 'surprised_pikachu.png'
#utilities.write_image(crop(utilities.image_to_list(file), "down", 150), 'cropdownsp.png')
#utilities.write_image(crop(utilities.image_to_list(file), "up", 150), 'cropupsp.png')
#utilities.write_image(crop(utilities.image_to_list(file), "left", 50), 'cropleftsp.png')
#utilities.write_image(crop(utilities.image_to_list(file), "right", 50), 'croprightsp.png')

def rgb_to_grayscale(rgb_image_array):

    number_of_rows = len(rgb_image_array)
    number_of_columns = len(rgb_image_array[0])
    r = 0 
    g = 0 
    b = 0

    for row in range(number_of_rows):

        for column in range(number_of_columns):

            n = 0

            for pixel in rgb_image_array[row][column]:

                n += 1

                if n == 1: 
                    r = 0.2989*pixel 
                elif n == 2: 
                    g = 0.5870*pixel
                else: 
                    b = 0.1140*pixel
                
            rgb_image_array[row][column] = r + g + b

    return rgb_image_array

#utilities.write_image(rgb_to_grayscale(utilities.image_to_list("robot.png")), "grayrobot.png")
#utilities.write_image(rgb_to_grayscale(utilities.image_to_list("surprised_pikachu.png")), "graysp.png")
#utilities.write_image(rgb_to_grayscale(utilities.image_to_list("square.jpg")), "graysquare.png")

def invert_rgb(image_array):

    number_of_rows = len(image_array)
    number_of_columns = len(image_array[0])

    for row in range(number_of_rows):

        for column in range(number_of_columns): 

            n = 0

            for pixel in range(len(image_array[row][column])):

                n += 1

                value = image_array[row][column][pixel]

                if n != 4:
                    image_array[row][column][pixel] = 255 - value

    return image_array

#utilities.write_image(invert_rgb(utilities.image_to_list("surprised_pikachu.png")), "irgbsp.png")  
#utilities.write_image(invert_rgb(utilities.image_to_list("robot.png")), "irgbrobot.png")  
#utilities.write_image(invert_rgb(utilities.image_to_list("square.jpg")), "irgbsquare.png")  
