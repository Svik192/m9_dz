def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, KeyError, ValueError, IndexError) as e:
            print(f"Error: {e}")
            return None

    return wrapper


def hello(data):
    return "How can I help you?"


@input_error
def add_contact(data, name, phone):
    data[name] = phone
    return f"Contact '{name}' with phone number '{phone}' added successfully."


@input_error
def change_phone(data, name, phone):
    data[name] = phone
    return f"Phone number for '{name}' changed to '{phone}'."


@input_error
def get_phone(data, name):
    return f"The phone number for '{name}' is {data[name]}."


def show_all(data):
    if not data:
        return "No contacts available."

    result = "All contacts:\n"
    for name, phone in data.items():
        result += f"{name}: {phone}\n"
    return result


def good_bye(data):
    return "Good bye!"


def default_handler(data):
    return "Unknown command. Please try again."


commands = {
    "hello": hello,
    "add": add_contact,
    "change": change_phone,
    "phone": get_phone,
    "show all": show_all,
    "good bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
}


@input_error
def parse_command(user_input):
    command, args = None, []

    for cmd in commands:
        if user_input.startswith(cmd):
            command = cmd
            args = user_input.replace(cmd, "").split()

    return command, args


@input_error
def curry_command_handler(data):
    def command_handler(command, *args):
        return commands.get(command, default_handler)(data, *args)

    return command_handler


def main():
    data = {}
    handle_command = curry_command_handler(data)

    while True:
        user_input = input("Enter command: ")

        command, args = parse_command(user_input)
        print("command: ", command, type(command))
        print("args: ", args)

        result = handle_command(command, *args)
        print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
