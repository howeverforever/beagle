import sys


def create_remote_host():
    sys.stdout.write('What\'s the position of this sensor?\n')
    sys.stdout.write('%16s: ' % '[0: left, 1:right]')
    sys.stdout.flush()
    position = input()
    label = 'L' if position == 0 else 'R'

    sys.stdout.write('Input the information about remote machine:\n')
    sys.stdout.write('%16s: ' % '[ip_address]')
    sys.stdout.flush()
    ip_addr = input()
    sys.stdout.write('%16s: ' % '[port]')
    sys.stdout.flush()
    port = input()

    filename = 'config.sock'
    with open(filename, 'w') as f:
        f.write(ip_addr + '\n')
        f.write(port + '\n')
        f.write(label + '\n')


def main():
    create_remote_host()
    sys.stdout.write('[BeagleBone] setup done!\n')
    sys.stdout.flush()


if __name__ == '__main__':
    main()
