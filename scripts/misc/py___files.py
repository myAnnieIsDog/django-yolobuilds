def run():
    from pprint import pprint 
    path = "test.csv"
    content = "Annie,Dog,Golden-Doodle\nBlue,Dog,Frenchie\nEliza,Cat,Long-Hair\nDoug,Cat,Short-Hair\n"
    # create(path)
    append(path, content)
    # write(path, content)
    for line in read(path):
        pprint(line)
    # pprint(f"Deleted: {delete(path)}")

def create(path):
    # Error if file already exists.
    try:
        with open(path, "x") as f: 
            f.close()
        return True
    except:
        return False


def append(path, content):   
    # Creates the file if it doesn't exist.
    with open(path, "a") as f:
        f.write(content)
        f.close()


def write(path, content):
    # OVERWRITES the file. Creates the file if it doesn't exist.
    try:
        with open(path, "w") as f:
            f.write(content)
            f.close()
            return True
    except:
        return False

def read(path):
    try:
        with open(path) as f:
            
            for line in f:
            content = f.read()
            f.close()
            return content
    except:
        return False


def delete(path):
    try:
        from os import remove
        from os.path import exists
        if exists(path):
            remove(path)
            return True
    except:
        return False


if __name__ == '__main__':
    run()

