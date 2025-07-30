""" 47. CPU Count Finder

Write a Python program to find out the number of CPUs used. """

import os

try:
    import psutil
except ImportError:
    print("Installing psutil module...")
    os.system("pip install psutil")
    import psutil


def count_cpus():
    """Display detailed CPU information."""
    try:
        logical_cpus = os.cpu_count()
        physical_cpus = psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq()

        print(f"🧠 Logical CPUs (Threads): {logical_cpus}")
        print(f"🧩 Physical CPUs (Cores): {physical_cpus}")
        if cpu_freq:
            print(f"⚡ CPU Frequency: {cpu_freq.current:.2f} MHz")
            print(f"🔝 Max Frequency: {cpu_freq.max:.2f} MHz")
        print(f"📊 CPU Usage Per Core: {psutil.cpu_percent(percpu=True)}")
        print(f"📈 Total CPU Usage: {psutil.cpu_percent()}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    count_cpus()
