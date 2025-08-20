import subprocess
import json
import os

# Run a shell command safely
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to run command. Are you running as Administrator?")

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
                interfaces.append(parts[-1])  # last column is the name
        return interfaces
    except Exception as e:
        print(f"❌ Could not fetch interfaces: {e}")
        return []

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

    # Load DNS options from JSON
    if not os.path.exists("dns.json"):
        print("❌ dns.json not found! Please create it.")
        return

    try:
        with open("dns.json", "r") as f:
            dns_options = json.load(f)
    except json.JSONDecodeError:
        print("❌ dns.json is not valid JSON.")
        return

    # Choose interface
    interfaces = list_interfaces()
    if not interfaces:
        print("❌ No interfaces found.")
        return

    print("Available interfaces:")
    for i, iface in enumerate(interfaces, 1):
        print(f"{i}. {iface}")

    try:
        iface_choice = int(input("Select an interface: "))
        interface_name = interfaces[iface_choice - 1]
    except (ValueError, IndexError):
        print("❌ Invalid interface choice.")
        return

    # Choose DNS
    print("\nAvailable DNS providers:")
    for i, (name, addrs) in enumerate(dns_options.items(), 1):
        print(f"{i}. {name}")
    print("0. Clear DNS")

    try:
        dns_choice = int(input("Choose DNS provider: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    if dns_choice == 0:
        clear_dns(interface_name)
    else:
        try:
            dns_name = list(dns_options.keys())[dns_choice - 1]
            dns1, dns2 = dns_options[dns_name]
            set_dns(interface_name, dns1, dns2)
        except (IndexError, ValueError):
            print("❌ Invalid DNS choice.")

if __name__ == "__main__":
    main()
