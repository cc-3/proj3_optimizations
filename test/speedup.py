from subprocess import run
from subprocess import PIPE

def execute(cmd=[], shell=False, dir='.', input=None, encoding='ascii', timeout=5):
    return run(cmd, shell=shell, stdout=PIPE, stderr=PIPE, input=input, cwd=dir, timeout=timeout)

def mean(script, runs=3):
    out = 0
    for i in range(runs):
        task = execute(cmd=['./%s' % script, 'benchmark'], timeout=180)
        out += int(task.stdout.decode().strip().split('\n')[-1].split(' ')[0].strip())
    return out / runs

execute(cmd=['make', 'clean'])
execute(cmd=['make'])
a = mean('optimized')
b = mean('baseline')
print('approx speedup: %dX' % (round(b / a)))
