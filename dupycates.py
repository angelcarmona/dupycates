import hashlib
import os


def file_as_bytes(file):
    with file:
        return file.read()


def main():
    hashes = {}
    rootdir = '.'

    for subdir, _, files in os.walk(rootdir):
        for file in files:
            filename = os.path.join(subdir, file)

            k = hashlib.md5(file_as_bytes(open(filename, 'rb'))).hexdigest()

            if k not in hashes:
                hashes[k] = [filename]
            else:
                hashes[k].append(filename)

    for k, v in list(hashes.items()):
        if len(v) == 1:
            del hashes[k]

    print(hashes)


if __name__ == '__main__':
    main()
