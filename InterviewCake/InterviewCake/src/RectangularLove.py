def rectangular_intersection(rectangle1, rectangle2):
    minY = rectangle1["bottom_y"] if rectangle1["bottom_y"] <= rectangle2["bottom_y"] else rectangle2["bottom_y"]
    minX = rectangle1["left_x"] if rectangle1["left_x"] <= rectangle2["left_x"] else rectangle2["left_x"]
    maxY = rectangle2["bottom_y"] if rectangle2["bottom_y"] > rectangle1["bottom_y"] else rectangle1["bottom_y"]
    maxX = rectangle2["left_x"] if rectangle2["left_x"] > rectangle1["left_x"] else rectangle1["left_x"]
    return {
        # coordinates of bottom-left corner
        'left_x': maxX,
        'bottom_y': maxY,
        # width and height
        #  'width': maxX+m
        'height': 4
    }


rectangle1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,
    # width and height
    'width': 10,
    'height': 4,
}

rectangle2 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,
    # width and height
    'width': 10,
    'height': 4,
}

rectangular_intersection(rectangle1, rectangle2)
