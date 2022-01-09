# kalkulator.py
class Kalkulator:
    def __init__(self):
        self.ans = 0
        self.command = ''

    def __str__(self):
        return f'{self.ans}'

    def calculate(self, op, a1, a2):
        if '_' == a1:
            a1 = self.ans
        if '_' == a2:
            a2 = self.ans
        self.command = f'({op} {a1} {a2})'
        # ** warning: only use eval when argument has been sanitized
        self.ans = eval(f'{a1} {op} {a2}')


def str2num(opr):
    """ sanitized argument content to a valid string """
    huruf_angka = '0123456789.eE'
    if opr == '' or opr == '_':
        return '_'
    for d in opr:
        if d not in huruf_angka:
            return None
    if '.' not in opr:
        opr = opr.lower()
        if 'e' in opr:
            m, exp, *_ = opr.split('e')
            # print(f'{m=},{exp=}')
            opr = int(m) * 10 ** int(exp)
        return int(opr)
    else:
        return float(opr)


def get_entry():
    while True:
        cmd_str = input('opr number number: ')
        cmd_list = cmd_str.lstrip().split(' ')
        if len(cmd_list) < 3:
            print('Argumen tidak lengkap!')
            continue
        op, a, b, *_ = cmd_list
        if op not in '* / + - ':
            print('operasi harus salah satu dari * / + -')
            continue
        a, b = map(str2num, (a, b))
        if None in (a, b):
            print('format angka: 0~9 . E')
            continue
        return op, a, b


def main():
    print('Kalkulator sayur RPN')
    rpn = Kalkulator()
    print("format: <operasi> <angka_A> <angka_B>")
    print('\toperasi: * / + -')
    print("\tangka: '0~9', 'E' eksponen, '.' tanda desimal, '_' jawaban sebelumnya")
    print('\tCtrl-C untuk keluar')
    print(' =>', rpn.ans)
    while True:
        operasi, angka1, angka2 = get_entry()
        try:
            rpn.calculate(operasi, angka1, angka2)
            print(f'{rpn.command} => {rpn.ans:,}')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
