
---

# Fast Proxy Checker (Python3)

## Overview

**Fast Proxy Checker** is a Python3-based tool designed to check the validity of HTTP, SOCKS4, and SOCKS5 proxies. The tool allows you to validate proxies by checking whether they are active, and categorizes them based on the proxy type (HTTP, SOCKS4, SOCKS5). The script uses a multithreaded approach to speed up the checking process.

It outputs the active proxies into separate files:
- `http_active.txt` for active HTTP proxies
- `socks4_active.txt` for active SOCKS4 proxies
- `socks5_active.txt` for active SOCKS5 proxies

This tool is fast and easy to use, making it ideal for those who need to verify a large list of proxies in a short time.

## Features

- **Proxy Type Checking**: Supports HTTP, SOCKS4, and SOCKS5 proxies.
- **Threaded Execution**: Utilizes multiple threads for faster checking.
- **Real-time Progress**: Displays real-time progress and current IP being checked.
- **Output to Files**: Active proxies are saved to separate output files.
- **Colorful Terminal Output**: Uses `colorama` for colored output to highlight successful and failed proxies.
  
---

## Prerequisites

Make sure you have Python 3 and the necessary libraries installed before running the script.

### Install Dependencies

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/fast-proxy-checker.git
   cd fast-proxy-checker
   ```

2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Proxy Checker Script

To start the proxy checker script, run the following command:

```bash
python3 new.py
```

### Select Proxy Type

Once the script starts, you will see a banner with the following prompt:

```
Select Proxy Type to Check:
[1] HTTP
[2] SOCKS4
[3] SOCKS5
[4] Exit
```

Choose the proxy type by entering `1`, `2`, or `3`. If you choose `4`, the script will exit.

### Provide Proxy List File

After selecting the proxy type, the script will ask for the file path of your proxy list:

```
Enter the file path (e.g., list.txt): http.txt
```

Make sure your proxy list file is in the format `IP:PORT` (e.g., `31.59.13.252:6522`).

### Real-Time Progress

The script will begin checking the proxies and display a progress bar with the following information:

```
Checking HTTP Proxies:   1%|█                                                                            | 45/3134 [00:01<01:20, 38.42it/s, Checking=31.59.13.252:6522]
```

- **Progress Bar**: Shows the percentage of proxies checked.
- **Current Proxy**: Displays the current proxy being checked.
- **Speed**: Displays the speed at which proxies are being checked.

### Output Files

- **`http_active.txt`**: Contains active HTTP proxies.
- **`socks4_active.txt`**: Contains active SOCKS4 proxies.
- **`socks5_active.txt`**: Contains active SOCKS5 proxies.

---

## Example Output

When running the script, you will see output similar to the following:

```
  RRRR    AAAAA  JJJJJ  SSSSS  EEEEE  CCCCC
  R   R  A     A    J   S      E      C
  RRRR   AAAAAAA    J   SSSSS  EEEE   C
  R  R   A     A    J       S  E      C
  R   R  A     A  JJJJJ  SSSSS  EEEEE  CCCCC

    Fast Proxy Checker and Validator by RajExploit404

Select Proxy Type to Check:
[1] HTTP
[2] SOCKS4
[3] SOCKS5
[4] Exit

Enter your choice (1/2/3): 1
Enter the file path (e.g., list.txt): http.txt

Checking HTTP Proxies:   1%|█                                                                            | 45/3134 [00:01<01:20, 38.42it/s, Checking=31.59.13.252:6522]
```

### Example Active Proxies Output

After checking, the script will save active proxies in the corresponding output file (e.g., `http_active.txt`), which will look like this:

```
31.59.13.252:6522
192.168.1.1:8080
...
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes

- Make sure to provide the correct file path to your proxy list.
- Proxies in the list should be in the format `IP:PORT` (e.g., `31.59.13.252:6522`).
- You can increase or decrease the number of threads used for checking by modifying the `ThreadPoolExecutor` settings in the script.

---

Feel free to modify or extend the functionality of the script to fit your needs. Enjoy using **Fast Proxy Checker**!
