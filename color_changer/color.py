class Color:
    def __init__(self, text, color=None, bold=None, underline=None):
        self.color = color
        self.bold = bold
        self.und = underline
        self.txt = text
        lib = []

        # Color
        if self.color == 'purple':
            lib.append('\033[95m')
        elif self.color == 'cyan':
            lib.append('\033[96m')
        elif self.color == 'darkcyan':
            lib.append('\033[36m')
        elif self.color == 'blue':
            lib.append('\033[94m')
        elif self.color == 'green':
            lib.append('\033[92m')
        elif self.color == 'yellow':
            lib.append('\033[93m')
        elif self.color == 'red':
            lib.append('\033[91m')
        elif self.color != 'purple' or 'cyan' or 'darkcyan' or 'blue' or 'green' or 'yellow' or 'red':
            raise Exception('Color not found'.upper())

        # Bold
        if self.bold:
            lib.append('\033[1m')

        # Underline
        if self.und:
            lib.append('\033[4m')

        lib.append(self.txt)

        txt_len = len(lib) - 1  # 3
        if txt_len == 0:
            print(self.txt)
        elif txt_len == 1:
            print(lib[0] + lib[1])
        elif txt_len == 2:
            print(lib[0] + lib[1] + lib[2])
        elif txt_len == 3:
            print(lib[0] + lib[1] + lib[2] + lib[3])
