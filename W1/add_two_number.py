import sys

def ADD(sys_args):
    a,b=0,0
    for arg in sys_args:
        if '-a=' in arg:
            a = int(arg.split('=')[1]) 
        elif '-b' in arg:
            b = int(arg.split('=')[1])
    return a+b 

if __name__ == '__main__':
    print(ADD(sys.argv))