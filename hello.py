from datetime import datetime

# Example script
message = f"Hello script ran at {datetime.now()}\n"

# Print to console
print(message)

# Save to a log file
with open("hello.log", "a") as f:
    f.write(message)
