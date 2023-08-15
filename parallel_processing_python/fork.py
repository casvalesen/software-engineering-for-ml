import os

'''

os.fork() is a method provided by the os module in Python, primarily used on Unix and Unix-like operating systems. It's used to fork the current process, creating a new child process.

When os.fork() is called, the current process (referred to as the parent process) is duplicated to create a new process (referred to as the child process). Both the parent and child processes then continue to execute from the point immediately following the os.fork() call.

The return value of os.fork() distinguishes between the two processes:

In the parent process, os.fork() returns the process ID (PID) of the child process.
In the child process, os.fork() returns 0.


'''



pid = os.fork()

if pid == 0:
    print("I am the child process, PID:", os.getpid())
else:
    print("I am the parent process, PID:", os.getpid(), "and my child is PID:", pid)