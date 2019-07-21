class InvalidOutFormat (Exception):
    """ 
    Raised if the format selected for output file
    is not valid
    """
    @classmethod
    def print_description(cls):
        print("Error: The output format selected is not valid ")