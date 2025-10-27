# dat fiind calea unix
# transformați-o într-o cale de tip windows
'tmp/part1/part2/file.txt'.replace("/", "\\")


# transformați-o într-o cale de tip windows
# folosind split și join
path = 'tmp/part1/part2/file.txt'
subpath_list = path.split('/')
win_path = "\\".join(subpath_list)

