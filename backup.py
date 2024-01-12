#!/usr/bin/env python3

import argparse
import time
import traceback

import restic
import schedule

from logger import logger, configure_logging
from utils import format_integer, human_size, human_time
from config import load_config


def backup(backup_paths, exclude_patterns, exclude_files):
    try:
        logger.info('Backup processing...')
        load_config()
        restic.unlock()
        backup_result = restic.backup(paths=backup_paths,
                                      exclude_patterns=exclude_patterns,
                                      exclude_files=exclude_files)

        # log backup result
        logger.info('Backup processed %s files (%s) in %s.',
                    format_integer(backup_result['total_files_processed']),
                    human_size(backup_result['total_bytes_processed']),
                    human_time(backup_result['total_duration']))
        logger.info('Backup done!')

    except Exception as e:
        logger.error('Backup failed: %s %s', str(e),
                     traceback.print_exception(e))


def main(args):
    # configure logging
    configure_logging()

    # load s3 and restic config
    load_config()

    # log version info
    version_info = restic.version()
    logger.info('Backing up with restic version %s (%s/%s/go%s)',
                version_info['restic_version'], version_info['architecture'],
                version_info['platform_version'], version_info['go_version'])

    # process backup
    logger.info('Backup starting...')

    if args.interval == 0:
        backup(args.backup_path, args.exclude, args.exclude_file)
    else:
        schedule.every(int(args.interval)).seconds.do(backup, backup_paths=args.backup_path,
                                                      exclude_patterns=args.exclude, exclude_files=args.exclude_file)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Sia S3 Backup',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--backup-path', required=True,
                        help='backup paths', action='append', default=[])
    parser.add_argument(
        '--interval', help="auto backup with interval (in second)", default=0)
    parser.add_argument('--exclude-file', action='append', default=[])
    parser.add_argument('--exclude', action='append', default=[])

    main(parser.parse_args())
