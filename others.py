def copy(link):
    f = open(link)
    file = f.read()
    f.close()
    return file


def print_hi(name):
    # Use Variables breakpoint in the code line below to debug your script.
    print('Hi, {name}'.format(name=name))  # Press Ctrl+F8 to toggle the
    #  breakpoint.
