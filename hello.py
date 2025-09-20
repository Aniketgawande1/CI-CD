from datetime import datetime

def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

def log_message(msg):
    """Print and append message to log file."""
    print(msg)
    with open("hello.log", "a") as f:
        f.write(msg + "\n")

if __name__ == "__main__":
    message = f"{greet()} script ran at {datetime.now()}"
    log_message(message)
