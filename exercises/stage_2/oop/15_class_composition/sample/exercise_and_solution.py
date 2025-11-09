# Exercise: Class Composition (Has-A Relationship)
# Description: Create classes where one class contains objects of another class
#
# Tasks:
# 1. Create an Address class with __init__ constructor
# 2. Address should have: street, city, zip_code
# 3. Create a Company class with __init__ constructor
# 4. Company should have: name, address (an Address object)
# 5. Add a method to Company that displays full information including address
# 6. Create Address and Company objects to demonstrate composition
#
# Expected Output:
# Company: Tech Solutions Inc.
# Address: 123 Main Street, San Francisco, 94102
#
# Company: Creative Agency LLC
# Address: 456 Oak Avenue, New York, 10001

# Solution:

# Step 1: Create the Address class
class Address:
    def __init__(self, street, city, zip_code):
        # Initialize address properties
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def get_full_address(self):
        # Return formatted address
        return f"{self.street}, {self.city}, {self.zip_code}"


# Step 2: Create the Company class that contains an Address object
class Company:
    def __init__(self, name, address):
        # Initialize company properties
        self.name = name
        # address is an Address object (composition - Company HAS-A Address)
        self.address = address

    def display_info(self):
        # Display company information including address
        print(f"Company: {self.name}")
        # We can call methods on the address object
        print(f"Address: {self.address.get_full_address()}")


# Step 3: Create Address objects first
address1 = Address("123 Main Street", "San Francisco", "94102")
address2 = Address("456 Oak Avenue", "New York", "10001")

# Step 4: Create Company objects that contain Address objects
# This is composition: Company HAS-A Address
company1 = Company("Tech Solutions Inc.", address1)
company2 = Company("Creative Agency LLC", address2)

# Step 5: Display company information
company1.display_info()
print()  # Empty line for spacing
company2.display_info()
