import psutil
import time

def bytes_to_gb(bytes):
    return bytes / (1024 ** 3)

def system_health_monitor():
    while True:
        print("===== System Health Monitor =====")
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_percent}%")
        
        # Memory usage
        mem = psutil.virtual_memory()
        print(f"Memory Usage: {mem.percent}% ({bytes_to_gb(mem.used):.2f} GB / {bytes_to_gb(mem.total):.2f} GB)")
        
        # Disk usage
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}% ({bytes_to_gb(disk.used):.2f} GB / {bytes_to_gb(disk.total):.2f} GB)")

        print("\nUpdating in 5 seconds...\n")
        time.sleep(5)

if __name__ == "__main__":
    system_health_monitor()
