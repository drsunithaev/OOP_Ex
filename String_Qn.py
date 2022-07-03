"""
String class to implement following string operations:
    replacing some character with another
    capitalize the string
    convert the string to lower case
    Split the string after converting to uppercase
    Slice the string
    reverse the string
"""
import logging
import log.log_file

class String_Class:
    def __init__(self, s):
        self.string = s

    def replace(self, old, new):
        """replacing old with new character"""
        try:
            logging.info(f"Replacing the character {old} with {new}")
            return self.string.replace(old,new)
        except Exception as e:
            logging.exception(e)


    def caps(self):
        """Capitalize the whole string"""
        try:
            logging.info("Capitalizing the string")
            return self.string.capitalize()
        except Exception as e:
            logging.exception(e)


    def lower(self):
        """convert the string to lower case"""
        try:
            logging.info("Converting the string to lower case")
            return self.string.lower()
        except Exception as e:
            logging.exception(e)

    def split_up(self, ch=' '):
        """Split the string after converting to uppercase"""
        try:
            logging.info("Converting the string to upper case and then splitting")
            return self.string.upper().split(sep =ch)
        except Exception as e:
            logging.exception(e)
    def slice(self, start, end, step):
        """Slicing the string with specified start and end indices"""
        try:
            logging.info(f"Slicing the string from {start} to {end} with step size{step}")
            return self.string[start:end:step]
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        """ Reversing the string"""
        try:
            logging.info("reversing the string")
            return self.string[-1:  :-1]
        except Exception as e:
            logging.exception(e)




