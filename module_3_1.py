calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return(string)

def is_contains(string, list_to_search):
    list_to_search = map(str.lower, list_to_search)
    string = string.lower()
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

