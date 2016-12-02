# coding: utf-8

import subprocess

def main():
    for n_units in [10, 100, 200, 500, 1000, 1200, 1500, 2000, 3000]:
        print('** units: {}'.format(n_units))
        print(subprocess.call(['python', 'mnist.py', '-u {}'.format(n_units)]))
        print('')

if __name__ == '__main__':
    main()
