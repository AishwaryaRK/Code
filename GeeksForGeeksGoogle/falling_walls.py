def get_collapsing_bricks(wall, i, j):
    wall[i][j] = 0
    queue = []
    collapsing_bricks = []

    queue = get_immediate_connected_bricks(i, j, wall, queue)

    while len(queue) != 0:
        brick = queue.pop(0)
        connected_bricks, is_connected_to_ground = get_connected_bricks(brick, wall)
        if not is_connected_to_ground:
            collapsing_bricks.append(connected_bricks)

    return collapsing_bricks


def get_connected_bricks(brick, wall):
    connected_bricks = []
    queue = []
    queue.append(brick)
    is_connected_to_ground = False

    while len(queue) != 0:
        brick = queue.pop(0)
    connected_bricks.append(brick)

    if brick(0) == len(wall):
        is_connected_to_ground = True

        immediate_connected_bricks = []
        immediate_connected_bricks = get_immediate_connected_bricks(i, j, wall, immediate_connected_bricks)

        for brick in immediate_connected_bricks:
            if brick not in connected_bricks:
                queue.append(brick)

    return connected_bricks, is_connected_to_ground


def get_immediate_connected_bricks(i, j, wall, queue):
    if i - 1 >= 0 and wall[i - 1][j] == 1:
        queue.append((i - 1, j))
    if i + 1 < len(wall) and wall[i + 1][j] == 1:
        queue.append((i + 1, j))
    if j - 1 >= 0 and wall[i][j - 1] == 1:
        queue.append((i, j - 1))
    if j + 1 < len(wall[0]) and wall[i][j + 1] == 1:
        queue.append((i, j + 1))

    return queue
