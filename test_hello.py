import hello
from datetime import datetime

def test_greet_default():
    # Default greeting
    assert hello.greet() == "Hello, World!"

def test_greet_custom_name():
    # Custom greeting
    assert hello.greet("Aniket") == "Hello, Aniket!"

def test_log_message(tmp_path):
    # Test that log_message writes to a file
    test_file = tmp_path / "test.log"
    msg = f"Test message at {datetime.now()}"
    
    # Temporarily patch the open() to write to test_file
    import builtins
    open_backup = builtins.open
    builtins.open = lambda path, mode='r': open(test_file, mode)
    
    hello.log_message(msg)
    
    # Restore open()
    builtins.open = open_backup

    # Check contents
    with open(test_file) as f:
        content = f.read()
    assert msg in content
