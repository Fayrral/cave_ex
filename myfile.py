
# f = open('myfile.txt', 'w', encoding="utf-8")

with open('myfile.txt', 'w', encoding="utf-8") as f:
    write_data = f.write('Hello World')
    print(write_data)
