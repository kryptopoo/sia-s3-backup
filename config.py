#!/usr/bin/env python3

import json
import os

import restic

import os

RESTIC_CONFIG_FILE = 'config.restic.txt'
S3_CONFIG_FILE = 'config.s3.json'


def load_config():
    password_file = os.path.join(os.getcwd(), RESTIC_CONFIG_FILE)
    restic_password = ""
    restic.password_file = password_file
    with open(password_file) as f:
        restic_password = f.read()
    

    # setting up s3
    s3_config = {}
    with open(S3_CONFIG_FILE) as s3_config_file:
        s3_config = json.load(s3_config_file)
    restic.repository = s3_config['url']

    # set environment for restic
    os.environ['AWS_ACCESS_KEY_ID'] = s3_config['accessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = s3_config['secretAccessKey']
    os.environ['RESTIC_PASSWORD'] = restic_password
    os.environ['RESTIC_REPOSITORY'] = s3_config['url']

    # restic.binary_path = 'c:\\restic\\restic_0.16.2_windows_amd64.exe'


def main():
    access_key_id = input("Enter Access Key ID: ")
    secret_access_key = input("Enter Secret Access Key: ")
    endpoint = input("Enter SIA S3 endpoint: ")
    bucket = input("Enter SIA bucket: ")
    restic_password = input("Enter restic password: ")

    # s3 config
    s3_config = {
        "accessKeyId": access_key_id,
        "secretAccessKey": secret_access_key,
        "url": "s3:" + endpoint + "/" + bucket
    }
    json_s3_config = json.dumps(s3_config, indent=4)
    with open(S3_CONFIG_FILE, "w") as outfile:
        outfile.write(json_s3_config)

    # restic config
    password_config = open(RESTIC_CONFIG_FILE, "w")
    password_config.write(restic_password)
    password_config.close()

    # init repo
    load_config()
    restic.init()

    print('Config done!')


if __name__ == '__main__':
    main()
