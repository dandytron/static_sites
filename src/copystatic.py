import os
import shutil

def recursive_copy_static(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    for item in os.list.dir(source_path):
        from_path = os.path.join(source_path, item)
        to_path = os.path.join(destination_path, item)
        print(f" {from_path} -> {to_path}")
        if os.path.isfile(item):
            shutil.copy(from_path, to_path)
        else:
            from_path = os.path.join(source_path, item)
            os.mkdir(to_path)
            recursive_copy_static(from_path, to_path)