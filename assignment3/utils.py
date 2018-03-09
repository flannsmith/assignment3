import requests
def parseFile(input):

    if input.startswith('http'):
        # use requests
        N, instructions = None, []
        response = requests.get(input)
        with open('input.txt', 'w') as fout:
            fout.writelines(response.text)
        fout.close()
        with open('input.txt', 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        # haven't written the code yet...
        return N, instructions
    return


