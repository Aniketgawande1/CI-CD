from datetime import datetime

# Main script
message = f"Hello! Script ran at {datetime.now()}"
print(message)

# Append to log file
with open("hello.log", "a") as f:
    f.write(message + "\n")
