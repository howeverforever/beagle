import os
import sys
import posixpath


def create_local_host():
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


def main():
    create_remote_host()
    sys.stdout.write('[BeagleBone] setup done!\n')
    sys.stdout.flush()


if __name__ == '__main__':
    main()
