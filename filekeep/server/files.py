import os

def read_path(path):
    entry = None
    entries = []

    def get_entry(path):
        stat = os.lstat(path)
        return {
            'is_dir': os.path.isdir(path),
            'size': stat.st_size,
            'mtime': stat.st_mtime_ns,
        }

    if os.path.exists(path):
        entry = get_entry(path)
        if entry['is_dir']:
            for name in os.listdir(path):
                e = get_entry(os.path.join(path, name))
                e['name'] = name
                entries.append(e)
        return entry, entries

    return None, None
