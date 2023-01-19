C_WIDTH_TEXT = 50

def get_input_item(text: str, result_type:int = 0) -> any:
    """asks input and returns in correct type

    Args:
        text (str): text questions,
        result_type (int, optional): 
            0 -> default -> str
            1 -> converts result to an int
            2 -> converts result to float

    Returns:
        any: returns result in type specified by result_type
    """
    result = input(f'{text}: ').strip()
    try:
        if result_type == 1:
            result = int(result)
        elif result_type == 2:
            result = float(result.replace(',', '.'))
    except Exception as e:
        result = 0

    return result


def get_input_text(text: str):
    inp = input(f'{text}: ')
    cnt = 1
    while len(inp) > C_WIDTH_TEXT * cnt:
        beg_substr = inp[:C_WIDTH_TEXT * cnt]
        end_substr = inp[C_WIDTH_TEXT * cnt:]
        inp = beg_substr + '\n' + end_substr
        cnt += 1
    return inp
