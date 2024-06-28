import time

def read_battery_status(file_path):
    """
    Reads the battery status from the specified file.

    :param file_path: Path to the battery status file.
    :return: Battery charge level as an integer percentage.
    """
    try:
        with open(file_path, 'r') as file:
            capacity = file.read().strip()
            return int(capacity)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading battery status: {e}")
        return None

def print_battery_status(charge_level):
    """
    Prints the battery status to the console.

    :param charge_level: Current battery charge level as an integer percentage.
    """
    if charge_level is not None:
        print(f"Battery level: {charge_level}%")

# Example usage
BATTERY_FILE_PATH = '/sys/class/power_supply/BAT0/capacity'  # Example path for Linux

try:
    while True:
        charge_level = read_battery_status(BATTERY_FILE_PATH)
        print_battery_status(charge_level)
        time.sleep(60)  # Check every 60 seconds

except KeyboardInterrupt:
    print("Exiting...")