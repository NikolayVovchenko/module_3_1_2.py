
calls = 0

def count_calls(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

def string_info (s):
    return (len(s), s.upper(),s.lower())

def is_contains(s,list):
    return s.lower()in [ x.lower() for x in list]

print(string_info('Armageddon'))
print(string_info("Capibara"))
print(is_contains("Urban", ["Python", "Java", "C++", "Ruby", "Urban"]))
print(calls)