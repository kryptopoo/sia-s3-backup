#!/usr/bin/env python3

import restic

from logger import logger, configure_logging
from config import load_config


def main():
    configure_logging()
    load_config()

    snapshots_result = restic.snapshots(group_by='host')
    snapshots = snapshots_result[0]["snapshots"]
    print("\nSnapshots:")
    for i in range(len(snapshots)):
        print(snapshots[i]["short_id"], "  ", snapshots[i]
              ["time"][0:19], "  ", snapshots[i]["paths"])

    restore_snapshot_id = input("\nChoose snapshot ID to restore: ")
    restore_target_dir = input("Enter target path: ")

    restic.restore(snapshot_id=restore_snapshot_id,
                   target_dir=restore_target_dir)
    print("Restore done!")


if __name__ == '__main__':
    main()
