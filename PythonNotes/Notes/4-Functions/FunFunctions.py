# FunFunctions.py

'''
Function Declaration Template
def <functionName>(<arg1>: <arg1Type>, <...>) -> <returnType>:
    <functionBody>
'''

# Example:
def factorial(number: int) -> int:
    product = number
    for i in range(2, number):
        product *= i

    return product

print(factorial(4)) # Returns 24

# Example of a Util class
class Utils:
    # Mark methods as @staticmethod
    @staticmethod
    def Hello():
        print("Hello")

    @staticmethod
    def World():
        print("World") 

    banana = "apple"

Utils.Hello()
print(Utils.banana)
