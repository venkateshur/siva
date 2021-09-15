from contextlib import contextmanager
import shutil
import os

@contextmanager
def network_share_auth(share, username=None, password=None, drive_letter='P'):

    """Context manager that mounts the given share using the given
    username and password to the given drive letter when entering
    the context and unmounts it when exiting."""

    #cmd_parts = ["NET USE %s: %s" % (drive_letter, share)]
    cmd_parts = ["mount -t smbfs"]

    #if password:
    #    cmd_parts.append(password)
    #    cmd_parts = ["mount -t smbfs"]
    if password:
        cmd_parts.append("-o password=%s,user=%s %s %s" % (password, username, share, drive_letter))
    os.system(" ".join(cmd_parts))

    if username:
        cmd_parts.append("/USER:%s" % username)
    os.system(" ".join(cmd_parts))
    try:
        yield
    finally:
        os.system("NET USE %s: /DELETE" % drive_letter)


with network_share_auth(r"\\ComputerName\ShareName", username, password):
    shutil.copyfile("foo.txt", r"P:\foo.txt")


def network_share_auth1(share, username=None, password=None, drive_letter='/mnt/P'):

    """Context manager that mounts the given share using the given
    username and password to the given drive letter when entering
    the context and unmounts it when exiting."""

    cmd_parts = ["smbmount %s %s" % (share, drive_letter)]

    if password:
        cmd_parts.append("-o password=%s,username=%s" % (password, username))
    os.system(" ".join(cmd_parts))
    try:
        yield
    finally:
        os.system("umount %s" % drive_letter)
        
with network_share_auth(r"//ComputerName/ShareName", username, password):
    shutil.copyfile("foo.txt", r"/mnt/P/foo.txt")
