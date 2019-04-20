import subprocess
from subprocess import run
from subprocess import PIPE


def execute(cmd=[], shell=False, dir='.', input=None, encoding='ascii', timeout=5):
    return run(cmd, shell=shell, stdout=PIPE, stderr=PIPE, input=input, cwd=dir, timeout=timeout)


def mean(script, runs=3):
    out = 0
    for i in range(runs):
        task = execute(cmd=['./%s' % script, 'benchmark'], timeout=600)
        out += int(task.stdout.decode().strip().split('\n')[-1].split(' ')[0].strip())
    return out / runs


try:
    a = mean('optimized')
    b = mean('baseline')
    if a > b:
        print('approx speedup: 0X')
    else:
        print('approx speedup: %dX' % (round(b / a)))
except subprocess.TimeoutExpired:
    print('TIMEOUT')
except Exception:
    print('UNEXPECTED EXCEPTION')
