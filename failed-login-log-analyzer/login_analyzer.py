# Failed Login Log Analyzer
# This script reads a sample log file and finds failed login attempts.

import re

log_file = "sample.log"
failed_attempts = {}

try:
    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                if ip_match:
                    ip_address = ip_match.group(1)

                    if ip_address in failed_attempts:
                        failed_attempts[ip_address] += 1
                    else:
                        failed_attempts[ip_address] = 1

    print("Failed Login Summary")
    print("--------------------")

    for ip, count in failed_attempts.items():
        print("IP Address:", ip, "| Failed Attempts:", count)

        if count >= 3:
            print("Alert: Possible brute-force activity from", ip)

except FileNotFoundError:
    print("Error: sample.log file was not found.")

except Exception as error:
    print("Error:", error)