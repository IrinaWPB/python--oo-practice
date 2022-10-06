"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create new generator from start"""
        self.start = self.next = start
    
    def __repr__(self):
        """Debugging message"""
        return f"Serial Generator start={self.start} next={self.next}"

    
    def generate(self):
        """Incrementing generator by 1, return """
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets starting point"""
        self.next = self.start

