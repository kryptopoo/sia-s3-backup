# SIA Auto Backup

This is a python program to back up data to SIA via S3-compatible gateway.

- Backs up specified paths to one or more backup locations
- Automatically progressing backups at a specified interval
- Restore data at a specific snapshot

### Pre-requisites

- [Sia renterd software](https://blog.sia.tech/zen-testnet-linux-install-guide-0a16adfc43da)
- [restic library/tool](https://restic.net)
- Python3.7 or above


[![Sia Auto Backup Demo](https://img.youtube.com/vi/feP1A6DXqsk/0.jpg)](https://youtu.be/feP1A6DXqsk)


## How to run

### Linux Ubuntu

#### Create a pip virtual environment

```bash
python3 -m venv venv && \
  . venv/bin/activate && \
  pip install --requirement requirements.txt
```

#### Configure S3 and restic

```bash
python3 congfig.py
```

#### Proceed backup

```bash
python3 backup.py --backup-path "/home/ubuntu/docs"
```

#### Proceed backup with schedule (`interval` is in seconds)

```bash
python3 backup.py --backup-path "/home/ubuntu/docs" --interval 60
```

#### Proceed restore

```bash
python3 restore.py
```

### Windows

TBD


### MAC

TBD

## References

https://blog.sia.tech/sia-innovate-and-integrate-christmas-2023-hackathon-9b7eb8ad5e0e