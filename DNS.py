import subprocess

# Function to execute command
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Function to set DNS addresses statically
def set_dns(interface_name, dns1, dns2):
    execute_command(f'netsh interface ip set dns "{interface_name}" static {dns1} primary')
    execute_command(f'netsh interface ip add dns "{interface_name}" {dns2} index=2')
    print(f"DNS set to {dns1} and {dns2} for {interface_name}")

# Function to clear DNS settings and set to automatic
def clear_dns(interface_name):
    execute_command(f'netsh interface ip set dns "{interface_name}" dhcp')
    print(f"DNS settings cleared for {interface_name}")


# Main program
def main():
    dns_options = {
        1: ("Shecan(185)", "185.51.200.2", "178.22.122.100"),
        2: ("Shecan(178)", "178.22.122.100", "185.51.200.2"),
        3: ("Electro", "78.157.42.100", "78.157.42.101"),
        4: ("Cloudflare", "1.1.1.1", "1.0.0.1"),
        5: ("OpenDNS", "208.67.222.222", "208.67.220.220"),
        6: ("CleanBrowsing", "185.225.168.168", "185.228.169.168"),
        7: ("Alternate DNS", "76.76.19.19", "76.223.122.150"),
        8: ("Quad9", " 9.9.9.9", "149.112.112.112"),
        9: ("AdGuard DNS", "176.103.130.130", "176.103.130.131"),
        10: ("OpenNIC", "46.151.208.154", "128.199.248.105"),
        11: ("DNS watch", "84.200.69.80", "84.200.70.40"),
        12: ("Verisign", "64.6.64.6", "64.6.65.6"),
        13: ("Safe DNS", "195.46.39.39", "195.46.39.40"),
        14: ("Yandex DNS", "77.88.8.8", "77.88.8.1"),
        15: ("Google Public DNS", "8.8.8.8", "8.8.4.4"),
        16: ("Comodo Secure", "8.26.56.26", "8.20.247.20"),
        17: ("Neustar DNS", "156.154.70.5", "156.154.71.5"),
        18: ("Host Iran", "172.29.2.100", "172.29.0.100"),
        19: ("Gozar DNS", "185.55.225.25", "185.55.225.26"),
        20: ("DYN DNS", "216.146.35.35", "216.146.36.36"),
        21: ("Shatel DNS", "85.15.1.15", "85.15.1.14"),
        22: ("Radar Game DNS", "10.202.10.10", "10.202.10.11"),
        23: ("Pishgaman DNS", "5.202.100.100", "5.202.100.101"),
        24: ("403 Online DNS", "10.202.10.202", "10.202.10.102"),
        25: ("Bogzar DNS", "185.55.226.26", "185.55.225.25"),
    }

    print(f"!!!ALERT: MAKE SURE YOU ARE RUNNING THE PROGRAM AS AN ADMINISTRATOR!!!\n")

    print(f"!!!ALERT: MAKE SURE YOUR NETWORK CONNECTION NAME IS Wi-Fi!!!'\n")

    # Display all DNS options to the user
    for key, value in dns_options.items():
        print(f"{key}. {value[0]}")
    print("0. Clear DNS")

    dns_server = int(input("Choose DNS provider: "))

    if dns_server in dns_options:
        set_dns(f"Wi-Fi", *dns_options[dns_server][1:])
    elif dns_server == 0:
        clear_dns(f"Wi-Fi")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()