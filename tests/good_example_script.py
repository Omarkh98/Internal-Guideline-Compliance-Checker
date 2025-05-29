# good_example_script.py

def calculate_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def greet_user(name: str) -> None:
    """
    Prints a greeting message.

    Args:
        name (str): Name of the user.
    """
    # Using logging instead of print for production
    import logging
    logging.info(f"Hello, {name}!")

def main():
    """
    Main entry point of the script.
    """
    result = calculate_fibonacci(10)
    greet_user("Alice")
    # You can add more logic here

if __name__ == '__main__':
    main()