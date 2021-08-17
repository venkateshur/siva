from ftplib import FTP
from pathlib import Path
from contextlib import contextmanager
import shutil
import os


def unix_transfer(path, host, port, user_name, password, input_file):
    file_path = Path(input_file)
    with FTP(host + ":" + port, user_name, password) as ftp, open(file_path, 'rb') as file:
        ftp.dir(path)
        ftp.storbinary(f'STOR {file_path.name}', file)


@contextmanager
def network_share_auth(share, drive_letter, username=None, password=None):
    cmd_parts = ["smbmount %s %s" % (share, drive_letter)]

    if password:
        cmd_parts.append("-o password=%s,username=%s" % (password, username))
    os.system(" ".join(cmd_parts))
    try:
        yield
    finally:
        os.system("umount %s" % drive_letter)


def windows_share(computer_share_name, file_name, username, password, drive_letter):
    with network_share_auth(r"//" + computer_share_name, username, password):
        shutil.copyfile(file_name, r"{0}".format(drive_letter))
