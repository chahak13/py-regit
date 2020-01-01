import os
import zlib
import hashlib

def initialize_pyregit():
    print(os.getcwd())
    if os.path.exists(os.path.join(os.getcwd(), '.pyregit')):
        raise Exception('PyRegit has already been initialised. Aborting init command')
    # Create .pyregit, .pyregit/objects and .pyregit/logs directories
    os.makedirs(os.path.join(os.getcwd(), '.pyregit'))
    os.makedirs(os.path.join(os.getcwd(), '.pyregit', 'objects'))
    os.makedirs(os.path.join(os.getcwd(), '.pyregit', 'logs'))
    os.makedirs(os.path.join(os.getcwd(), '.pyregit', 'refs'))
    return

def stage():
    pass

def compress(filepath, filename):
    with open(os.path.join(filepath, filename), 'rb') as f:
        file_content = f.read()
    compressed_content = zlib.compress(file_content)
    return compressed_content

def cat_file(filepath, filename):
    with open(os.path.join(filepath, filename), 'rb') as f:
        compressed_bytes = f.read()
    decompressed_bytes = zlib.decompress(compressed_bytes)
    decompressed_string = decompressed_bytes.decode()
    print(decompressed_string)
    return

def sha1_hash(filepath, filename):
    with open(os.path.join(filepath, filename), 'rb') as f:
        file_bytes = f.read()
    hash_obj = hashlib.sha1()
    hash_obj.update(file_bytes)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    # initialize_pyregit()
    compress(os.getcwd(), 'README.md')
