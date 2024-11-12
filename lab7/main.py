import os, sys

def ex1(directory: str, extension: str) -> None:
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a directory")
    if extension.count('.') < 1 or extension.count('..') > 0 or len(extension) == 0:
        raise ValueError(f"'{extension}' is not a valid extension")

    try:
        for (root, dirs, files) in os.walk(directory):
             for file in files:
                 if file.endswith(extension):
                     try:
                         fullFileName = os.path.join(root, file)
                         fileContent = open(fullFileName, 'r')
                         for line in fileContent:
                             print(line.strip())
                         fileContent.close()
                     except PermissionError:
                         print("Unable to open and/or read file %s"%file)
    except PermissionError:
        print(f'Cannot access {directory}')

def ex2(directory: str) -> None:
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a directory")
    if not os.path.exists(directory):
        raise ValueError(f"'{directory}' does not exist")

    i = 0
    try:
        for (root, dirs, files) in os.walk(directory):
            for file in files:
                try:
                    fullFileName = os.path.join(root, file)
                    newFileName = fullFileName.split('.')[0]
                    fileExtension = '.' + fullFileName.split('.')[-1]
                    newFileName = newFileName + str(i) + fileExtension
                    os.rename(fullFileName, newFileName)
                    i += 1
                except PermissionError:
                    print("Unable to rename file %s"%file)
    except PermissionError:
        print(f'Cannot access {directory}')

def ex3(directory: str) -> None:
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a directory")
    if not os.path.exists(directory):
        raise ValueError(f"'{directory}' does not exist")

    fileSizeSum = 0
    try:
        for (root, dirs, files) in os.walk(directory):
            for file in files:
                fullFileName = os.path.join(root, file)
                try:
                    fileSizeSum += os.path.getsize(fullFileName)
                except OSError:
                    print("Unable to access file %s"%file)
    except PermissionError:
        print(f'Cannot access {directory}')

    print("Total bytes size is: %d"%fileSizeSum)

def ex4(directory: str) -> None:
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a directory")
    if not os.path.exists(directory):
        raise ValueError(f"'{directory}' does not exist")
    if len(os.listdir(directory)) == 0:
        raise ValueError(f"'{directory}' is empty")

    extensions = dict()
    try:
        for (root, dirs, files) in os.walk(directory):
            for file in files:
                fileExtension = '.' + file.split('.')[-1]
                extensions.update({fileExtension: [extensions.values()].count(fileExtension)})
    except PermissionError:
        print(f'Cannot access {directory}')

    for extension in extensions:
        print(extension)


def main():
    print("=======EX1=======")
    ex1(sys.argv[1], sys.argv[2])
    print("=======EX2=======")
    ex2(sys.argv[3])
    print("=======EX3=======")
    ex3(sys.argv[3])
    print("=======EX4=======")
    ex4(sys.argv[3])

if __name__ == '__main__':
    main()