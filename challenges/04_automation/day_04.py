"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""
import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
    print("🔥" * 30)
    print("⭐️ System Resource Monitor ⭐️")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"CPU USAGE: {cpu}")
    print(f"RAM USAGE: {ram.percent}% ( {round(ram.used / 1e9, 2)} GB used of {round(ram.total / 1e9, 2)} GB)")
    print(f"DISK USAGE: {disk.percent}% ( {round(disk.used / 1e9, 2)} GB used of {round(disk.total / 1e9, 2)} GB)")
    print("🔥" * 30)

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Monitoring Stopped.....")