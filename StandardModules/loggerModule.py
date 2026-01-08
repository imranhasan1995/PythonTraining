import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel (level=logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Example usage
def calculate_sum(a, b):
   logger.debug(f"Calculating sum of {a} and {b}")
   result = a + b
   logger.info(f"Sum calculated successfully: {result}")
   return result

# Main program
if __name__ == "__main__":
   logger.info("Starting the program")
   result = calculate_sum(10, 20)
   logger.info("Program completed")