import subprocess
import sys

# Run a shell command safely
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to run command. Are you running as Administrator?")
        input("Press Enter to exit...")
        sys.exit(1)

# List available network interfaces
def list_interfaces():
    try:
        result = subprocess.run(
            'netsh interface show interface',
            capture_output=True, text=True, shell=True
        )
        lines = result.stdout.splitlines()
        interfaces = []
        for line in lines[3:]:  # skip table headers
            parts = line.split()
            if len(parts) >= 4:
                interfaces.append(parts[-1])  # last column is interface name
        return interfaces
    except Exception as e:
        print(f"❌ Could not fetch interfaces: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

# Set DNS servers
def set_dns(interface_name, dns1, dns2):
    execute_command(f'netsh interface ip set dns "{interface_name}" static {dns1} primary')
    execute_command(f'netsh interface ip add dns "{interface_name}" {dns2} index=2')
    print(f"✅ DNS set to {dns1}, {dns2} for {interface_name}")

# Clear DNS (set to automatic)
def clear_dns(interface_name):
    execute_command(f'netsh interface ip set dns "{interface_name}" dhcp')
    print(f"✅ DNS settings cleared for {interface_name}")

def main():
    print("⚠️  ALERT: Run this program as Administrator!\n")

    # DNS options embedded in the code
    dns_options = [
        ("Shecan(185)", "185.51.200.2", "178.22.122.100"),
        ("Shecan(178)", "178.22.122.100", "185.51.200.2"),
        ("Electro", "78.157.42.100", "78.157.42.101"),
        ("Cloudflare", "1.1.1.1", "1.0.0.1"),
        ("OpenDNS", "208.67.222.222", "208.67.220.220"),
        ("CleanBrowsing", "185.225.168.168", "185.228.169.168"),
        ("Alternate DNS", "76.76.19.19", "76.223.122.150"),
        ("Quad9", "9.9.9.9", "149.112.112.112"),
        ("AdGuard DNS", "176.103.130.130", "176.103.130.131"),
        ("OpenNIC", "46.151.208.154", "128.199.248.105"),
        ("DNS Watch", "84.200.69.80", "84.200.70.40"),
        ("Verisign", "64.6.64.6", "64.6.65.6"),
        ("Safe DNS", "195.46.39.39", "195.46.39.40"),
        ("Yandex DNS", "77.88.8.8", "77.88.8.1"),
        ("Google Public DNS", "8.8.8.8", "8.8.4.4"),
        ("Comodo Secure", "8.26.56.26", "8.20.247.20"),
        ("Neustar DNS", "156.154.70.5", "156.154.71.5"),
        ("Host Iran", "172.29.2.100", "172.29.0.100"),
        ("Gozar DNS", "185.55.225.25", "185.55.225.26"),
        ("DYN DNS", "216.146.35.35", "216.146.36.36"),
        ("Shatel DNS", "85.15.1.15", "85.15.1.14"),
        ("Radar Game DNS", "10.202.10.10", "10.202.10.11"),
        ("Pishgaman DNS", "5.202.100.100", "5.202.100.101"),
        ("403 Online DNS", "10.202.10.202", "10.202.10.102"),
        ("Bogzar DNS", "185.55.226.26", "185.55.225.25")
    ]

    # Choose interface
    interfaces = list_interfaces()
    if not interfaces:
        print("❌ No interfaces found.")
        input("Press Enter to exit...")
        sys.exit(1)

    print("Available interfaces:")
    for i, iface in enumerate(interfaces, 1):
        print(f"{i}. {iface}")

    try:
        iface_choice = int(input("Select an interface: "))
        interface_name = interfaces[iface_choice - 1]
    except (ValueError, IndexError):
        print("❌ Invalid interface choice.")
        input("Press Enter to exit...")
        sys.exit(1)

    # Display numbered DNS menu
    print("\nAvailable DNS providers:")
    for i, (name, _, _) in enumerate(dns_options, 1):
        print(f"{i}. {name}")
    print("0. Clear DNS")

    try:
        dns_choice = int(input("Choose DNS provider: "))
    except ValueError:
        print("❌ Invalid input.")
        input("Press Enter to exit...")
        sys.exit(1)

    if dns_choice == 0:
        clear_dns(interface_name)
    else:
        try:
            dns_name, dns1, dns2 = dns_options[dns_choice - 1]
            set_dns(interface_name, dns1, dns2)
        except IndexError:
            print("❌ Invalid DNS choice.")
            input("Press Enter to exit...")
            sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
