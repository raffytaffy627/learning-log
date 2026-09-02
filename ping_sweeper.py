import subprocess
import time
import sys

def ping(ip):
    # "-c 1" means send just 1 ping packet (Linux/Mac syntax)
    # We check the return code: 0 means success (device responds with a ping basically)
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

# Sweeping a range of IPs on the local network
if len(sys.argv) > 1:
    base_ip = sys.argv[1]
else:
    base_ip = "192.168.4"
    print(f"No network specified, defaulting to {base_ip}.x")
    alive_ips = []  # empty list to collect results as we find them
start_time = time.time()

for i in range(1, 255):
    ip = f"{base_ip}.{i}"
    print(f"Scanning {ip}...", end="\r")
    if ping(ip):
        print(f"{ip} is alive" + " " * 20)
        alive_ips.append(ip)  # add this IP to our list

# After the loop finishes, save results and show a summary
with open("scan_results.txt", "w") as f:
    for ip in alive_ips:
        f.write(ip + "\n")

elapsed = time.time() - start_time
print(f"\nScan complete. {len(alive_ips)} devices found in {elapsed:.1f} seconds.")
print("Results saved to scan_results.txt")