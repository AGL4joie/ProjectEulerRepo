
class ClassName:
    """Question is: """
    # Class attributes (shared by all instances)
    class_attribute = "Some value"

    def __init__(self, param1, param2):
        """
        The constructor method, called when a new object is created.
        'self' refers to the new instance of the class.
        """
        self.param1 = param1  # Instance attribute
        self.param2 = param2  # Instance attribute

    def instance_method(self, arg1):
        """
        An instance method (a function defined within the class).
        """
        # Access instance attributes using 'self'
        return f"Method called with {arg1} and {self.param1}"
    
# Create an instance (object) of the class
my_object = ClassName("value one", "value two")

# Access attributes
print(f"Parameter 1: {my_object.param1}")

# Call a method
result = my_object.instance_method("extra argument")
print(f"Method result: {result}")