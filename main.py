from minitasks.file_rider import reader
from minitasks.midle import get_csv
from minitasks.user_generator import generator
from minitasks.who_is_here import number_of_astronauts


def main():
    print('\nNow function "get_csv" is using:\n')
    get_csv()
    print('\nNow function "reader" is using:\n')
    reader("wd/files_input/message.txt")
    print('\nNow function "genarator" is using:\n')
    generator()
    print('\nNow function " number_of_astronauts" is using:\n')
    number_of_astronauts()


if __name__ == "__main__":
    main()
