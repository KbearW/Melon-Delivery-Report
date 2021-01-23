'''Build a function to print lines in muli-files w/ a loop.'''
# Function with 2 variables
def report(delivery_date, file_name):
    print(delivery_date)
    # call the open function as a variable and reuse it later
    the_file = open(file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # used unpacking to reduce the # of lines
        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    # close the file by calling the function
    the_file.close()
report("Day 1", "um-deliveries-20140519.txt")
report("Day 2", "um-deliveries-20140520.txt")
report("Day 3", "um-deliveries-20140521.txt")