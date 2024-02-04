def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True