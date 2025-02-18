import os
import subprocess

from pupdb import rest

def start_http_server():
    """ Python wrapper around start_http_server script. """
    
    dirpath = os.path.dirname(rest.__file__)
    subprocess.call(
        'env PYTHONPATH={} {}/start_http_server'.format(
            dirpath, dirpath), shell=True
    )

    # In địa chỉ sau khi khởi động server
    print("Server is running at http://127.0.0.1:4000")
    print("Click here to open: http://127.0.0.1:4000")

if __name__ == "__main__":
    start_http_server()
