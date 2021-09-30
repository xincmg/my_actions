import hashlib

'''
md5
output
readtext
'''
def md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()


def output(file_name, text):
    with open(file_name, mode='w+', encoding='utf-8') as file:
        file.write(text)


def readtext(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        return file.read()