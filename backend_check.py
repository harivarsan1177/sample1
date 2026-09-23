import time

print("Starting Backend Check...")

# Simulate the required 4-second delay
time.sleep(4)

# Generate the result file
with open("backend_report.txt", "w") as file:
    file.write("Backend Check Completed Successfully.\n")
    file.write(f"Timestamp: {time.ctime()}\n")

print("Backend Check completed and report generated.")
