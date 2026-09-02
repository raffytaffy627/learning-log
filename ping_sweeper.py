import subprocess

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
base_ip = "192.168.4"  # alsooo you can change this to match your actual network (see note :D below)

for i in range(1, 255):
    ip = f"{base_ip}.{i}"
    print(f"Scanning {ip}...", end="\r")  # shows current IP, overwrites each time
    if ping(ip):
        print(f"{ip} is alive" + " " * 20)  # extra spaces clear leftover text