class CircularDependencyException(Exception):
    def __init__(self, message="Circular dependency detected"):
        self.message = message
        super().__init__(self.message)