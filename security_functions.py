def check_empty(list_args):
    for arg in list_args:
        if len(arg) == 0:
            return False
    return True
