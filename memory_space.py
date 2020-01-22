import win32serviceutil
import win32service
import win32event
import servicemanager
import psutil


DISK = "C:"

free = psutil.disk_usage(DISK).free/(1024*1024*1024)
print(f"{free:.4} Gb free on disk {DISK}")

   
DISK = "D:"


free = psutil.disk_usage(DISK).free/(1024*1024*1024)
print(f"{free:.4} Gb free on disk {DISK}")
while free >= 131:
    if free > 133:
        print("Места стало больше")
        break
def main():
    

input('Press ENTER to exit')