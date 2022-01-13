def validate_pin(pin):
    #return true or false
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False