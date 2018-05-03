import journal

def main():
    print_header()
    run_event_loop()




def print_header():
    print('-----------------------------------')
    print('             Dear Journal')
    print('-----------------------------------')

def run_event_loop():
    print('What would you like to do with your journal?')
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name) #[] #list()

    while  cmd!= 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd.lower().strip != 'x':
            print("Sorry, we do not understand '{}' ." 'Please try again.'.format(cmd))

    print('Done, see you later!')
    journal.save(journal_name, journal_data)

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(' *[{}] {}'.format(idx+1, entry ))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    #  data.append(text)

main( )
