import re

def isValidPhoneNumber(phNo: str):
    # Check for Valid Phone Number
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    if not (Pattern.match(phNo)):
        return "Phone number is incorrect"


def isValidEmailId(email: str):
    # Check for Valid Emailid
    # Can be used to validate all the Email type fields
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email) == False):
        return "Email id is incorrect"


def isValidText(text: str):
    """Check if the string has only text"""
    # Check for Valid Text
    # Can be used to validate all the Text or Char type fields
    if(text.isalpha() == False):
        return "Entered value is incorrect"


def isValidNumber(pfno: str):
    # Check for Valid Number
    # Can be used to validate all the number type fields
    try:
        val = int(pfno)
    except ValueError:
        try:
            val = float(pfno)
        except ValueError:
            return "Please enter the valid value"


def isNoneOrEmpty(text: str):
    """Check if the string is None or Empty"""
    check = False
    text = str(text).strip()
    if text == "None":
        check = True
    elif text == None:
        check = True
    elif text == "":
        check = True
    return check