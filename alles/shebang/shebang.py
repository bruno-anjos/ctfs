#!/usr/bin/python3 -u
import os
import secrets

NOBODY = 65534
NOGROUP = 65534

# if the string contains a dot it exits
def check_input(data):
    if b'.' in data:
        os._exit(1)


def main():
    # does nothing
    os.open('/bin/bash', os.O_RDONLY)
    
    # opens flag and duplicates the file descriptor 
    fd = os.open('./flag', os.O_RDONLY)
    os.dup2(fd, 9)

    # creates path with /tmp and 16 random bytes
    path = os.path.join('/tmp', secrets.token_hex(16))

    # prints prompt ??
    print("#!/d", end="")

    # reads 16 bytes from stdin
    data = os.read(0, 0x10)
    
    # closes stdin
    os.close(0)

    # checks if contains dot
    check_input(data)

    # creates /tmp/RANDOM
    fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o777)

    # writes the prompt and whatever i gave it as input to the file
    os.write(fd, b'#!/d' + data)
    os.close(fd)

    pid = os.fork()
    if pid == 0:
        # if child
        # sets gid for current process
        os.setresgid(NOGROUP, NOGROUP, NOGROUP)
        # sets uid for current process
        os.setresuid(NOBODY, NOBODY, NOBODY)
        try:
            # try to execute /tmp/RANDOM file
            os.execv(path, [path])
        except:
            os._exit(-1)
    else:
        # waits for child and deletes file
        os.waitpid(pid, 0)
        os.unlink(path)


if __name__ == '__main__':
    main()
