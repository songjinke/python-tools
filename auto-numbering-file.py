import os

DIR = '.'
EXTENSION = '.mp4'


def filecreationtime(file):
    stat_file = os.stat(DIR + "/" + file)
    return stat_file.st_ctime


def order_by_ctime(files):
    return sorted(files, key=lambda x: filecreationtime(x))


def rename(files):
    number = 1
    for filename in files:
        if os.path.splitext(filename)[1] != EXTENSION:
            continue

        oldpath = os.path.join(DIR, filename)
        newpath = os.path.join(DIR, format(number, '03d') + '-' + filename)
        os.rename(oldpath, newpath)
        number = number + 1


files = os.listdir(DIR)
files = order_by_ctime(files)
rename(files)
