**1. What is localhost/127.0.0.1?**

- **localhost** is a hostname that refers to the current device used to access it. It is used to establish an IP connection to the same machine or computer being used by the end-user.

- **127.0.0.1** is the loopback IP address in IPv4. It is typically mapped to "localhost" in the `/etc/hosts` file on Unix-like systems. When you ping or send data to 127.0.0.1, you're communicating with your own device.

**2. What is 0.0.0.0?**

- **0.0.0.0** is a non-routable meta-address used to designate an invalid, unknown, or non-applicable target. In the context of servers and networking:

  - **Listening Address:** When a server listens on 0.0.0.0, it means it listens on all available IPv4 addresses on the local machine.

  - **Routing:** In routing tables, it can denote the default route.

**3. What is /etc/hosts?**

- The **`/etc/hosts`** file is a plain text file in Unix-like operating systems that maps hostnames to IP addresses. Before querying DNS, the system checks this file to resolve hostnames. This can be used for:

  - Defining hostnames for local network machines.

  - Overriding DNS entries.

  - Blocking malicious sites by mapping them to 127.0.0.1.

**4. How to Display Your Machine’s Active Network Interfaces**

To display active network interfaces on various operating systems:

- **Linux:**
  
  - **ifconfig (deprecated in some distributions):**
    ```bash
    ifconfig
    ```
  
  - **ip (recommended):**
    ```bash
    ip addr show
    ```
  
  - **Displaying only active (up) interfaces:**
    ```bash
    ip -o link show | awk '$9 == "UP" {print $2}'
    ```

- **macOS:**
  
  - **ifconfig:**
    ```bash
    ifconfig
    ```
  
  - **Networksetup:**
    ```bash
    networksetup -listallhardwareports
    ```

- **Windows:**
  
  - **Command Prompt:**
    ```cmd
    ipconfig
    ```
  
  - **PowerShell:**
    ```powershell
    Get-NetAdapter
    ```
  
  - **For detailed information:**
    ```powershell
    Get-NetIPConfiguration
    ```

These commands will provide information about the network interfaces, their statuses, IP addresses, and other relevant details.