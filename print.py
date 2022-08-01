with open('myfile.txt', 'r') as mf:
    lines = mf.readlines()
    for l in lines:
        print(l)
