def rectangular_intersection(rectangle1, rectangle2):
    minY = rectangle1["bottom_y"] if rectangle1["bottom_y"] <= rectangle2["bottom_y"] else rectangle2["bottom_y"]
    minX = rectangle1["left_x"] if rectangle1["left_x"] <= rectangle2["left_x"] else rectangle2["left_x"]
    maxY = rectangle2["bottom_y"] if rectangle2["bottom_y"] > rectangle1["bottom_y"] else rectangle1["bottom_y"]
    maxX = rectangle2["left_x"] if rectangle2["left_x"] > rectangle1["left_x"] else rectangle1["left_x"]

    left_x = 0
    width = 0
    if (rectangle1["left_x"] <= rectangle2["left_x"] and rectangle1["left_x"] + rectangle1["width"] > rectangle2[
        "left_x"]) or (
                    rectangle2["left_x"] <= rectangle1["left_x"] and rectangle2["left_x"] + rectangle2["width"] >
                rectangle1[
                    "left_x"]):
        left_x = min(rectangle1["left_x"], rectangle2["left_x"])
        width = min((rectangle1["left_x"] + rectangle1["width"]), (rectangle2["left_x"] + rectangle2["width"])) - left_x

    bottom_y = 0
    height = 0
    if (rectangle1["bottom_y"] <= rectangle2["bottom_y"] and rectangle1["bottom_y"] > (
                rectangle2["bottom_y"] - rectangle2["height"])) or (
                    rectangle2["bottom_y"] <= rectangle1["bottom_y"] and rectangle2["bottom_y"] > (
                        rectangle1["bottom_y"] - rectangle1["height"])):
        bottom_y = min(rectangle1["bottom_y"], rectangle2["bottom_y"])
        height = bottom_y - min((rectangle1["bottom_y"] - rectangle1["height"]),
                                (rectangle2["bottom_y"] - rectangle2["height"]))

    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height,
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

print(rectangular_intersection(rectangle1, rectangle2))
