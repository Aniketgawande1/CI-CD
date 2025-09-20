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

    from unittest.mock import patch
    import builtins

    def custom_open(path, mode='r', *args, **kwargs):
        if path == "log.txt":
            return open(test_file, mode, *args, **kwargs)
        return builtins.open(path, mode, *args, **kwargs)

    with patch("builtins.open", new=custom_open):
        hello.log_message(msg)

    # Check contents
    with open(test_file) as f:
        content = f.read()
    assert msg in content
