'''dldl'''
def calculate_digital_root(number_str):
    '''dadad'''
    while len(number_str) > 1:
        total = 0
        for char in number_str:
            total += int(char)
        number_str = str(total)
    return number_str
def main():
    '''dadad'''
    while True:
        line = input().strip()
        if line == "0":
            break
        print(calculate_digital_root(line))
main()
