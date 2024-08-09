Here's a summary of the key concepts related to PIDs, processes, and signals:

### What is a PID?
- **PID (Process Identifier)**: A PID is a unique number assigned by the operating system to each process when it is created. This number is used to identify and manage processes.

### What is a Process?
- **Process**: A process is an instance of a program that is being executed. It includes the program code and its current activity. A process has its own memory space and executes independently of other processes.

### How to Find a Process’ PID
- **Finding a Process' PID**: 
  - **Linux/Unix**: You can use the `ps` command to list processes and their PIDs. For example:
    ```bash
    ps aux | grep <process_name>
    ```
    Or, use the `pgrep` command:
    ```bash
    pgrep <process_name>
    ```
  - **Windows**: You can use the `Task Manager` to find the PID or use the `tasklist` command in the Command Prompt:
    ```cmd
    tasklist | findstr <process_name>
    ```

### How to Kill a Process
- **Killing a Process**: 
  - **Linux/Unix**: You can use the `kill` command followed by the PID to terminate a process:
    ```bash
    kill <PID>
    ```
    If the process doesn't terminate, you can use `kill -9 <PID>` to forcefully kill it.
  - **Windows**: You can use the `Task Manager` or the `taskkill` command:
    ```cmd
    taskkill /PID <PID>
    ```
    To forcefully kill the process, you can use:
    ```cmd
    taskkill /F /PID <PID>
    ```

### What is a Signal?
- **Signal**: A signal is a limited form of inter-process communication used in Unix, Unix-like, and other POSIX-compliant operating systems. A signal is essentially an asynchronous notification sent to a process to notify it of an event. Signals can be used to terminate a process, pause it, continue it, or handle other events.

### What are the 2 Signals That Cannot Be Ignored?
- **SIGKILL (Signal 9)**: This signal immediately terminates a process. It cannot be caught or ignored by the process.
- **SIGSTOP (Signal 19)**: This signal stops (pauses) a process, and it cannot be caught or ignored. Unlike `SIGKILL`, `SIGSTOP` does not terminate the process; it just pauses it until a `SIGCONT` (continue) signal is sent.

These concepts are essential for managing and interacting with processes in an operating system, particularly in Unix-like environments.