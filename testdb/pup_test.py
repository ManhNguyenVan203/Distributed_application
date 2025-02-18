import sys
from pupdb.core import PupDB
import shutil

class PupDBWithReplication:
    def __init__(self, db_path):
        self.db = PupDB(db_path)
        self.db_path = db_path  # Lưu trữ đường dẫn cơ sở dữ liệu

    def replicate(self):
        replica_paths = ['replica1.json', 'replica2.json']
        for replica_path in replica_paths:
            shutil.copy(self.db_path, replica_path)  # Sử dụng self.db_path để copy tệp
            print(f"Database replicated to {replica_path}")

    def set(self, key, value):
        self.db.set(key, value)
        self.replicate()
        print(f"Set {key} to {value}")

    def get(self, key):
        value = self.db.get(key)
        print(f"Value for '{key}': {value}")
        return value

    def remove(self, key):
        self.db.remove(key)
        self.replicate()
        print(f"{key} removed")

db_with_replication = PupDBWithReplication('db.json')

def set_data():
    db_with_replication.set('test_key', 'test_value')

def get_data():
    db_with_replication.get('test_key')

def remove_data():
    db_with_replication.remove('test_key')

def list_keys():
    print(list(db_with_replication.db.keys()))

def run_function(func_name):
    functions = {
        'set_data': set_data,
        'get_data': get_data,
        'remove_data': remove_data,
        'list_keys': list_keys,
        'replicate': db_with_replication.replicate  
    }
    if func_name in functions:
        functions[func_name]()
    else:
        print(f"Function {func_name} not found.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_function(sys.argv[1])
    else:
        print("Please specify a function name to run.")
