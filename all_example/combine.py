import glob

data_output = glob.glob('./data_output/*')


with open('combo.txt', 'w') as fw:
    for file in data_output:
        with open(file, 'r') as fr:
            fw.write(*fr.readlines())

