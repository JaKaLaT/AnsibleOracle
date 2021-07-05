import random
import time


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

def random_string(length):
    random_string = ''
    for _ in range(length):
        random_integer = random.randint(97, 122)
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string

# print(random_date("2000-01-01", "2021-06-28", random.random()))
# print(random.randint(1,1000))
# print(random_string(6))

output=''
for _ in range(1000001):
    output += "INSERT INTO sample_data (a_number, a_date, a_char) VALUES ("+str(random.randint(1,1000))+", DATE '"+random_date("2000-01-01", "2021-06-28", random.random())+"', '"+random_string(8)+"');\n"

# print(output)
with open('./insert_sample_data.sql', 'w') as file:
    file.write(output)