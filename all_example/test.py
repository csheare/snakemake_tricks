import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "data")
    parser.add_argument('-dataset', type=str, required=True)
    args = parser.parse_args()

    output = ''
    with open(f'{args.dataset}_input.txt', 'r') as f:
        output = f.readline()



    with open(f'{args.dataset}_output.txt', 'w') as f:
        f.write(output)