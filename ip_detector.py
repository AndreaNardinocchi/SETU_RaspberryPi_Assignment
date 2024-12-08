import subprocess
from countdownSpeak import countdownSpeak


# Find IP address Function
def find_myLaptopIP_Address(target_IPs, ip_range="192.168.0.1/24"):
    result = subprocess.check_output(f"sudo nmap -sn {ip_range} | grep Nmap", shell=True)
    found_IPs=[]
    for IP in target_IPs: 
         if IP.lower() in str(result).lower():
             found_IPs.append(IP)         

    return found_IPs


# Test code
if __name__ == "__main__":
    # Example list of target IP addresses to search for on the network
    target_IPs = [
        "192.168.0.56",  # Replace with actual IP addresses you expect to find
        "11:22:33:44:55:66"
    ]

    print("Scanning network...Is Andrea on???")
    # Call the function to find the specified IP addresses
    found_devices = find_myLaptopIP_Address(target_IPs)

    # Display the result
    if found_devices:
        print(f"Found devices:{found_devices}...There you go, he is on!\nBeware Andrea, the countdown has just started...")
        countdownSpeak()
    else:
        print("No target IP addresses found on the network.")



