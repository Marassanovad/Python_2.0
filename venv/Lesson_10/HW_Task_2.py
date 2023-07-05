

class Information_output:

    @classmethod
    def herringbone_2(cls, height=5):
        for i in range(height):
            print(f'{"*" * (i * 2 + 1):^{height * 2 + 1}}')

    @classmethod
    def multiplication_table_2(cls):
        for x in range(2, 11):
            for y in range(2, 6):
                print(f'{y:^3} X {x:^3} = {x * y:^3}\t\t\t', end='')
            print()
        print()
        for x in range(2, 11):
            for y in range(6, 10):
                print(f'{x:^3} X {y:^3} = {x * y:^3}\t\t\t', end='')
            print()

if __name__ == '__main__':
    Information_output.herringbone_2(5)
    Information_output.multiplication_table_2()


