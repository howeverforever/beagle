import beagle as bg
import argparse
import sys
import time
import csv
import threading
import socket
import pickle
from glob import glob


class Beagle(object):

    def __init__(self, axis_10):
        self._axis_10 = axis_10
        self._mpu = bg.MPU()
        self.__load_config()

    def __load_config(self):
        config = glob('config.sock')[0]
        with open(config, 'r') as f:
            self._ip_addr = f.readline()[:-1]
            self._port = int(f.readline()[:-1])

    def capture_sensor(self):
        ts = time.time()
        st = bg.get_datetime(ts).strftime('%Y-%m-%d_%H%M%S')

        threads = {}
        try:
            threads['local'] = threading.Thread(target=self.__send_to_local, args=(st,))
            threads['remote'] = threading.Thread(target=self.__send_to_remote, args=(st,))

            for key, thread in threads.items():
                thread.daemon = True
                thread.start()

            while True:
                time.sleep(100)

        except (KeyboardInterrupt, SystemExit):
            pass

    def __get_raw_data_row(self):
        ts = time.time()
        accel = self._mpu.mpu_read_accel()
        gyro = self._mpu.mpu_read_gyro()

        row = [ts]
        if self._axis_10:
            temp = self._mpu.mpu_read_temp()
            row += [temp]

        row += [accel['ax'], accel['ay'], accel['az']]
        row += [gyro['gx'], gyro['gy'], gyro['gz']]

        if self._axis_10:
            mag = self._mpu.mpu_read_mag()
            row += [mag['mx'], mag['my'], mag['mz']]

        return row

    def __send_to_local(self, st):
        start_st = st
        sys.stdout.write('[%s] Start reading sensor data to local...\n' % st)
        sys.stdout.flush()

        try:
            with open(st + '.csv', 'w') as f:
                writer = csv.writer(f)
                if self._axis_10:
                    writer.writerow(['timestamp', 'temp',
                                     'imu_ax', 'imu_ay', 'imu_az',
                                     'imu_gx', 'imu_gy', 'imu_gz',
                                     'imu_mx', 'imu_my', 'imu_mz'])
                else:
                    writer.writerow(['timestamp',
                                     'imu_ax', 'imu_ay', 'imu_az',
                                     'imu_gx', 'imu_gy', 'imu_gz'])

                data_rows = 0
                while True:
                    try:
                        row = self.__get_raw_data_row()
                        writer.writerow(row)

                        data_rows += 1
                        if data_rows % 10000 == 0:
                            ts = time.time()
                            st = bg.get_datetime(ts).strftime('%Y-%m-%d_%H%M%S')
                            sys.stdout.write('[%s] %6d rows have been collected.\n' % (st, data_rows))
                            sys.stdout.flush()

                    except (KeyboardInterrupt, TypeError):
                        break

                f.close()

                ts = time.time()
                st = bg.get_datetime(ts).strftime('%Y-%m-%d_%H%M%S')
                sys.stdout.write('[%s] \"%s\" was saved.\n' % (st, start_st + '.csv'))
                sys.stdout.flush()

        except IOError:
            sys.stderr.write('Failed to build CSV.\n')
            sys.stderr.flush()

    def __send_to_remote(self, st):
        sys.stdout.write('[%s] Start reading sensor data to remote...\n' % st)
        sys.stdout.flush()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self._ip_addr, self._port))

        sys.stdout.write('connect successful\n')
        sys.stdout.flush()

        data_rows = 0
        while True:
            try:
                row = self.__get_raw_data_row()
                send_data = pickle.dumps(row)
                sock.sendall(send_data)

                data_rows += 1
                if data_rows % 10000 == 0:
                    ts = time.time()
                    st = bg.get_datetime(ts).strftime('%Y-%m-%d_%H%M%S')
                    sys.stdout.write('[%s] %6d rows have been collected.\n' % (st, data_rows))
                    sys.stdout.flush()

            except (KeyboardInterrupt, TypeError):
                sock.send('Q'.encode())
                break

        sock.close()


def main():
    parser = argparse.ArgumentParser(description='Collect data from BeagleBone Blue')
    parser.add_argument('-6', help='6 Axis', action='store_true')
    parser.add_argument('-10', help='10 Axis', action='store_true')

    args = vars(parser.parse_args())
    axis_10 = args['10']

    bg_ = Beagle(axis_10)
    bg_.capture_sensor()

    return 0


if __name__ == '__main__':
    main()
