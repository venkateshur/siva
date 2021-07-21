import os
import subprocess
from ftplib import FTP
from pathlib import Path


#def unix_transfer(path, host, port, user_name, password, input_file, output_file):
#    p = subprocess.Popen(["scp", input_file, user_name + ":" + password + "@" + host + ":" + port + ":" + path + "/" + output_file])
#    return os.waitpid(p.pid, 0)


def unix_transfer(path, host, port, user_name, password, input_file):
    file_path = Path(input_file)
    with FTP(host + ":" + port + ":" + path + "/", user_name, password) as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_path.name}', file)




