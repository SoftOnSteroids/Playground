import threading
import time, random

def f(line):
    """
    A function that performs a CPU-bound operation.

    Parameters:
    - line (str): The line to be executed.

    Returns:
    None
    """
    # Your CPU-bound operation here
    print(f"Executing: {line}")
    time.sleep(4**random.random())
    print(f"Finish excecutong: {line}")


def parallel_f(lines):
    """
        Executes a list of functions in parallel using multiple threads.

        Args:
            lines (List[str]): A list of strings representing the lines to be processed.

        Returns:
            None
    """
    threads = []
    for line in lines:
        thread = threading.Thread(target=f, args=(line,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Usage
lines = ["a", "b", "c"]  # Your list of input strings
parallel_f(lines)

print(lines)
print(type(lines))
print(lines.__repr__())
print(type(lines.__repr__()))
print(eval(lines.__repr__()))
print(type(eval(lines.__repr__())))
print(type(lines.__str__()))
