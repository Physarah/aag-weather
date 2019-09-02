#!/usr/bin/env python3
import time

from weather import AAGCloudSensor


def main(config_file=None, store_result=False, verbose=False, **kwargs):
    if config_file is None:
        print('Must pass config_file')
        return

    aag = AAGCloudSensor(config_file, **kwargs)

    while True:
        try:
            data = aag.capture(store_result=store_result)
            if verbose:
                print(f'{data!r}')

            time.sleep(60)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Read an AAG CloudWatcher")
    parser.add_argument('--config_file', required=True,
                        help='Config file that contains the AAG params.')
    parser.add_argument('--store-result', default=False, action='store_true',
                        help='If data entries should be saved to db, default False.')
    parser.add_argument('--db-file', default='weather.db', help='Name of sqlite3 db file to use.')
    parser.add_argument('--db-table', default='weather', help='Name of db table to use.')
    parser.add_argument('--serial_address', default=None,
                        help='USB serial address to use. If None, value from config will be used.')
    parser.add_argument('--verbose', action='store_true', default=False, help='Verbose.')

    args = parser.parse_args()

    main(**vars(args))
    print('Shutting down AAG reader')