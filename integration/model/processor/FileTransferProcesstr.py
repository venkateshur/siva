import os
import subprocess


def unix_transfer(path, host, port, user_name, password, input_file, output_file):
    p = subprocess.Popen(["scp", input_file, user_name + ":" + password + "@" + host + ":" + port + ":" + path + "/" + output_file])
    return os.waitpid(p.pid, 0)




