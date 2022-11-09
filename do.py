"""
Intended to simulate some usage in order to be picked up by the sensor
"""
import string
import os
import random
import time

TEST = "test.txt"
TEST2 = "test2.txt"
TEST3 = "test3.txt"

# number of chars to write to files
SIZE = 10000

# time to wait between creation and deletion of files in seconds
WAIT_TIME = 10

TEST_FILES = [TEST, TEST2, TEST3]


def write():

    for file_name in TEST_FILES:
        file = open(file_name, 'w')


        for _ in range(SIZE):
            chars = string.ascii_letters + "\n" + " "
            char = random.choice(chars)
            file.write(char)


        file.close()




def clean():
    for file_name in TEST_FILES:
        os.remove(file_name)

def do():
    """
    Writes the files, waits, then deletes the files
    """
    write()
    time.sleep(WAIT_TIME)
    clean()
    time.sleep(WAIT_TIME)

def main():
    while 1:
        do()   



if __name__ == "__main__":
    main()