class Computer:

    # the Computer class has the following attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # the constructor creates a new Computer instance with the given attributes
    def __init__(self, desc:str, processor:str, capacity:int, mem:int, OS:str, year:int, pr:int):
        self.description = desc
        self.processor_type = processor
        self.hard_drive_capacity = capacity
        self.memory = mem
        self.operating_system = OS
        self.year_made = year
        self.price = pr
    
    # the update_com method updates the computer's operating system to the given OS
    def update_com(self, new_os: str):
        self.operating_system = new_os

    # the print_com method returns a string representation of the computer's details
    def print_com(self):
        return(f'description: {self.description}, processor_type: {self.processor_type}, hard_drive_capacity: {str(self.hard_drive_capacity)}, memory: {str(self.memory)}, operating_system: {self.operating_system}, year_made: {str(self.year_made)}, price: {str(self.price)}')
