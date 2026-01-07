import re

from .utils import colors, prefix

def extract_outermost_matches(value):
    pattern = r'\$\d+\[(?:[^\[\]]+|\[.*?\])*\]'
    return re.finditer(pattern, value)

def echo(value, color_string, line_break=''):
    color_list = [color.strip() for color in color_string.split(',')]
    reset = prefix + colors['reset']
    default_color = prefix + colors.get(color_list[0], reset)
    final_output = ""
    last_pos = 0
    for match in extract_outermost_matches(value):
        start, end = match.span()
        final_output += f"{default_color}{value[last_pos:start]}{reset}"
        tag = match.group()
        match_index = int(re.match(r'\$(\d+)\[', tag).group(1)) - 1
        text = re.search(r'\[(.*)\]', tag).group(1)
        if 0 <= match_index < len(color_list):
            color = prefix + colors.get(color_list[match_index], reset)
        else:
            color = default_color
        final_output += f"{color}{text}{reset}"
        last_pos = end
    final_output += f"{default_color}{value[last_pos:]}{reset}"
    if line_break.lower() == 'tb':
        final_output = f"\n{final_output}\n"
    elif line_break.lower() == 't':
        final_output = f"\n{final_output}"
    elif line_break.lower() == 'b':
        final_output = f"{final_output}\n"
    print(final_output)
