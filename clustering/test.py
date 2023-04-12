import subprocess
import os
import json
join = os.path.join

dummy = open(join('..', '..', 'NeuralCodeSum', 'data', 'python', 'dummy.code'), 'r')
code = open(join('..', '..', 'NeuralCodeSum', 'data', 'python', 'sample.code'), 'w')

l = []
res_list = []
error_list = []
for i, line in enumerate(dummy.readlines()):
    l.append(line.strip())
    
    if (i+1) % 128 == 0 or i == 478:
        code.write('\n'.join(l))
        code.flush()
        subprocess.run(["bash","../../NeuralCodeSum/scripts/generate.sh","0","code2jdoc","sample.code"])
        res = json.load(open(join('..', '..', 'NeuralCodeSum', 'tmp', 'code2jdoc_beam.json'), 'r'))
        res_list.append(res)

        open(join('..', '..', 'NeuralCodeSum', 'tmp', 'code2jdoc_beam.json'), 'w').close()
        open(join('..', '..', 'NeuralCodeSum', 'data', 'python', 'sample.code'), 'w').close()

        if len(res) != len(l):
            print(f'From {i-127} to {i} there is a problem')
            error_list.append((i-127, i))
        l = []


# Dump res_list to a file
json.dump(res_list, open(join(os.getcwd(), 'res_list.json'), 'w'))

# Dump error_list to a file
json.dump(error_list, open(join(os.getcwd(), 'error_list.json'), 'w'))
print(error_list)