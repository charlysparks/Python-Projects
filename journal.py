import os

def load(name):
    # todo: populate from file if it exists.
    return []

def save(name, journal_data):
    filename = os os.path.join('./journals/', name, '.jrl')
    print('Would load from: {}'.format(filename))
    # f_ouput = open(filename, 'w')

def add_entry(text, journal_data):
    journal_data.append(text)
