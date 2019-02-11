# a, ., b, .., .., c

# ///

def simplify_path(path):
    path_directories = path.split("/")
    simplified_path = "/"
    stack = []
    i = 1
    for directory in path_directories:
        if directory != '':
            if directory == '..':
                stack.pop()
            elif directory == '.':
                continue
            else:
                stack.append(directory)

    for directory in stack:
        simplified_path += directory + '/'

    return simplified_path


# print(simplify_path("/a/./b/../../c/"))
print(simplify_path("/a/./b/../../c/a/"))
