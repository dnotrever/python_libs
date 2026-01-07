import getpass
from .utils import colors, prefix

def question(value, secret=False, line_break=True):

    _reset = prefix + colors['reset']
    _type = prefix + colors['question']

    _value = value if isinstance(value, str) else str(value)

    if line_break:
        _content = '\n' + _type + _value + _reset + " "
    else:
        _content = _type + _value + _reset + " "

    if secret:
        answer = getpass.getpass(_content)
    else:
        answer = input(_content)

    return answer
