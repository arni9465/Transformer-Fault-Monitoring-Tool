
import csv
import os
from datetime import datetime

RATED_CURRENT = 100
MAX_TEMPERATURE = 90
WARNING_TEMPERATURE = 75
VOLTAGE_MIN = 390
VOLTAGE_MAX = 440
CURRENT_WARNING = 80
CURRENT_CRITICAL = 100

FILE_NAME = "transformer_data.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Timestamp", "Voltage", "Current",
                "Temperature", "Load_Percentage",
                "Status", "Alerts"
            ])


def monitor_transformer(voltage, current, temperature):
    alerts = []
    load = (current / RATED_CURRENT) * 100

    if voltage < VOLTAGE_MIN:
        alerts.append("Low voltage")
    elif voltage > VOLTAGE_MAX:
        alerts.append("High voltage")

    if current > CURRENT_CRITICAL:
        alerts.append("Overcurrent")
    elif current > CURRENT_WARNING:
        alerts.append("High current")

    if temperature >= MAX_TEMPERATURE:
        alerts.append("Overheating")
    elif temperature >= WARNING_TEMPERATURE:
        alerts.append("High temperature")

    if any(a in ["Overcurrent", "Overheating"] for a in alerts):
        status = "CRITICAL"
    elif alerts:
        status = "WARNING"
    else:
        status = "NORMAL"

    return load, status, alerts


def save_reading(voltage, current, temperature,
                 load, status, alerts):

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            voltage,
            current,
            temperature,
            round(load, 2),
            status,
            "; ".join(alerts) if alerts else "None"
        ])


def view_history():
    if not os.path.exists(FILE_NAME):
        print("No monitoring history available.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        print("\n----- TRANSFORMER MONITORING HISTORY -----")

        for row in reader:
            print(" | ".join(row))


def main():
    initialize_file()

    print("=" * 50)
    print("     TRANSFORMER FAULT MONITORING SYSTEM")
    print("=" * 50)

    while True:
        print("\n1. Enter Transformer Readings")
        print("2. View Monitoring History")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            try:
                voltage = float(input("Voltage (V): "))
                current = float(input("Current (A): "))
                temperature = float(input("Temperature (C): "))

                if min(voltage, current, temperature) < 0:
                    print("Invalid readings. Negative values not allowed.")
                    continue

                load, status, alerts = monitor_transformer(
                    voltage, current, temperature
                )

                print("\n----- MONITORING REPORT -----")
                print(f"Voltage: {voltage:.2f} V")
                print(f"Current: {current:.2f} A")
                print(f"Temperature: {temperature:.2f} C")
                print(f"Load: {load:.2f}%")
                print(f"Status: {status}")

                if alerts:
                    print("Alerts:", ", ".join(alerts))
                else:
                    print("No abnormal conditions detected.")

                save_reading(
                    voltage, current, temperature,
                    load, status, alerts
                )

                print("\nReading saved successfully.")

            except ValueError:
                print("Please enter valid numerical readings.")

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("Monitoring system closed.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()