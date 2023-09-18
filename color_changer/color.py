class Color:
    def __init__(self, text, color=None, bold=None, underline=None, border=None, background=None):
        self.color = color.lower()
        self.bold = bold
        self.und = underline
        self.txt = text
        self.border = border
        self.back = background

    def __str__(self):
        lib = ''

        # Color
        if self.color == 'purple':
            lib += '\033[95m'
        elif self.color == 'grey':
            lib += '\033[90m'
        elif self.color == 'cyan':
            lib += '\033[96m'
        elif self.color == 'darkcyan':
            lib += '\033[36m'
        elif self.color == 'blue':
            lib += '\033[94m'
        elif self.color == 'green':
            lib += '\033[92m'
        elif self.color == 'yellow':
            lib += '\033[93m'
        elif self.color == 'red':
            lib += '\033[91m'
        elif self.color != 'purple' or 'cyan' or 'darkcyan' or 'blue' or 'green' or 'yellow' or 'red':
            raise Exception('Color not found'.upper())

        if self.back == 'purple':
            lib += '\033[45m'
        elif self.back == 'grey':
            lib += '\033[47m'
        elif self.back == 'cyan':
            lib += '\033[46m'
        elif self.back == 'black':
            lib += '\033[40m'
        elif self.back == 'blue':
            lib += '\033[44m'
        elif self.back == 'green':
            lib += '\033[42m'
        elif self.back == 'yellow':
            lib += '\033[43m'
        elif self.back == 'red' or self.back == 'pink':
            lib += '\033[41m'
        elif self.back != 'purple' or 'cyan' or 'black' or 'pink' or 'blue' or 'green' or 'yellow' or 'red':
            raise Exception('background color not found'.upper())

        if self.border:
            lib += '\033[51m'

        # Bold
        if self.bold:
            lib += '\033[1m'

        # Underline
        if self.und:
            lib += '\033[4m'

        lib += self.txt
        lib += '\033[0m'
        return lib
