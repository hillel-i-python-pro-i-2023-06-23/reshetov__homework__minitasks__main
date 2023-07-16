from minitasks.file_rider import reader
from minitasks.midle import get_csv
from minitasks.user_generator import generator
from minitasks.who_is_here import number_of_astronauts


def main():
    print(f'\nNow function "get_csv" is using:\n')
    get_csv()
    print(f'\nNow function "reader" is using:\n')
    reader("minitasks/files/message.txt")
    print(f'\nNow function "genarator" is using:\n')
    generator()
    print(f'\nNow function " number_of_astronauts" is using:\n')
    number_of_astronauts()


if __name__ == "__main__":
    main()
