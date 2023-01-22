import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "data")
    parser.add_argument('-file', type=str, required=True)
    args = parser.parse_args()

    output = ''
    with open(args.file, 'r') as f:
        output = f.readline()

 
    output_file = args.file.replace('input', 'output')
    with open('./{var}'.format(var=output_file), 'w') as f:
        f.write('{var} <> {var}'.format(var=output))
