import os

def test_hello_log():
    # Make sure hello.log exists after running hello.py
    os.system("python3 hello.py")  # Run the script
    assert os.path.exists("hello.log")  # Check log file created
    # Optionally, check that it contains "Hello!"
    with open("hello.log") as f:
        content = f.read()
    assert "Hello!" in content
