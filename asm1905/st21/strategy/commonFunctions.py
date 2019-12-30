from colorama import Fore


def get_menu_input(menu):
    for i, key in enumerate(menu):
        print(Fore.YELLOW + str(i) + ') ' + key[0])
    response = len(menu)

    while int(response) >= len(menu):
        response = return_number('Please, input your choice: ')
    return response


def return_number(input_text='Input employee number: '):
    while 1:
        try:
            return int(input(Fore.BLUE + input_text))
        except ValueError:
            print(Fore.MAGENTA + 'Input only number!')
