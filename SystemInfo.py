# Importing the library & module 
import subprocess 
import os
import speedtest
import psutil
import pyautogui
import sys
import platform
import multiprocessing
from screeninfo import get_monitors
import uuid
import requests
###########################################
print("1 -- All Installed software’s list")
Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
a = str(Data) 
# try block 
try: 
	# arrange the string 
	for i in range(len(a)): 
		print(a.split("\\r\\r\\n")[6:][i]) 
except IndexError as e: 
	print("All Done")
###################################################
print("2 -- Internet Speed")
def get_internet_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        return download_speed, upload_speed

    except Exception as e:
        return f"Error retrieving internet speed: {e}"

if __name__ == "__main__":
    download_speed, upload_speed = get_internet_speed()
    print("Download Speed:", download_speed, "Mbps")
    print("Upload Speed:", upload_speed, "Mbps")
####################################################
print("3 -- Screen resolvution")
def get_screen_resolution():
    width, height = pyautogui.size()
    return width, height

if __name__ == "__main__":
    width, height = get_screen_resolution()
    print(f"Screen resolution: {width}x{height}")
####################################################
print("4 -- CPU model")
def get_cpu_model():
    try:
        return platform.processor()
    except Exception as e:
        return f"Error retrieving CPU model: {e}"

if __name__ == "__main__":
    cpu_model = get_cpu_model()
    print("CPU Model:", cpu_model)
 ###################################################
print("5 -- No of core and threads of CPU")
def get_cpu_cores_threads():
    try:
        num_cores = os.cpu_count()  # Returns the number of logical CPUs
        num_threads = multiprocessing.cpu_count()  # Returns the number of threads

        return num_cores, num_threads
    except Exception as e:
        return f"Error retrieving CPU information: {e}"

if __name__ == "__main__":
    cores, threads = get_cpu_cores_threads()
    print("Number of CPU Cores:", cores)
    print("Number of CPU Threads:", threads)
 ####################################################
print("7 -- RAM Size ( In GB )")
# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
#####################################################
print("8 -- Screen size ( In inch)")

def get_screen_size():
    try:
        monitors = get_monitors()
        if monitors:
            # Assuming the first monitor is the primary one
            primary_monitor = monitors[0]
            width_mm, height_mm = primary_monitor.width, primary_monitor.height
            diagonal_size = (width_mm**2 + height_mm**2)**0.5 / 25.4  # Convert to inches
            return round(diagonal_size, 2)
        else:
            return "Screen size information not available."

    except Exception as e:
        return f"Error retrieving screen size: {e}"

if __name__ == "__main__":
    screen_size = get_screen_size()
    print("Screen Size:", screen_size, "inch")
###########################################################
print("9 -- Wifi/Ethernet mac address")
def get_mac_addresses():
    try:
        # Get the MAC address of the first network interface (usually Ethernet)
        ethernet_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])

        # Get the MAC address of the Wi-Fi interface
        # Note: This may not work on all systems, and the interface name may need adjustment
        try:
            wifi_mac = ':'.join(['{:02x}'.format((uuid.UUID(int=uuid.getnode()).node >> elements) & 0xff) for elements in range(5, -1, -1)])
        except Exception as e:
            wifi_mac = f"Error retrieving Wi-Fi MAC address: {e}"

        return ethernet_mac, wifi_mac

    except Exception as e:
        return f"Error retrieving MAC addresses: {e}"

if __name__ == "__main__":
    ethernet_mac, wifi_mac = get_mac_addresses()
    print("Ethernet MAC Address:", ethernet_mac)
    print("Wi-Fi MAC Address:", wifi_mac)
###############################################################
print("10 -- Public IP address")
def get_public_ip():
    try:
        # Use ipinfo.io service to get public IP address
        response = requests.get('https://ipinfo.io')
        if response.status_code == 200:
            return response.json().get('ip', 'Unable to retrieve public IP')
        else:
            return f"Error: {response.status_code} - Unable to retrieve public IP"

    except Exception as e:
        return f"Error retrieving public IP address: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print("Public IP Address:", public_ip)
#############################################################
print("11 -- Windows version")
def get_windows_version():
    try:
        return platform.version()

    except Exception as e:
        return f"Error retrieving Windows version: {e}"

if __name__ == "__main__":
    windows_version = get_windows_version()
    print("Windows Version:", windows_version)