def read_write_file(filepath, mode, a=[]):
    if mode == 'r':
        with open(filepath, mode) as read_rec:
            a = read_rec.readlines()
        return a
    elif mode == 'w':
        with open(filepath, mode) as add_rec:
            add_rec.writelines(a)
    else:
        return 'wrong mode selected. either r or w'


# print(__name__)
# if __name__ == '__main__':
#     print('hello')