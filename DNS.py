import subprocess

# Function to set DNS addresses statically
def set_dns(interface_name, dns1, dns2):
    try:
        subprocess.run(f'netsh interface ip set dns "{interface_name}" static {dns1} primary', shell=True, check=True)
        subprocess.run(f'netsh interface ip add dns "{interface_name}" {dns2} index=2', shell=True, check=True)
        print(f"DNS set to {dns1} and {dns2} for {interface_name}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Function to clear DNS settings and set to automatic
def clear_dns(interface_name):
    try:
        subprocess.run(f'netsh interface ip set dns "{interface_name}" dhcp', shell=True, check=True)
        print(f"DNS settings cleared for {interface_name}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Main program
def main():
    dns_options = {
        1: ("Shecan(185)", "185.51.200.2", "178.22.122.100"),
        2: ("Shecan(178)", "178.22.122.100", "185.51.200.2"),
        3: ("Electro", "78.157.42.100", "78.157.42.101")
    }

    wifi_name = str(input(f"Enter your Wi-Fi name in network connections: "))

    dns_server = int(input("Choose DNS provider:\n1. Shecan(185)\n2. Shecan(178)\n3. Electro\n0. Clear DNS\n"))

    if dns_server in dns_options:
        set_dns(f"{wifi_name}", *dns_options[dns_server][1:])
    elif dns_server == 0:
        clear_dns(f"{wifi_name}")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
