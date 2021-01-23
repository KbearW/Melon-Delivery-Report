def report(delivery_date, file_name):
    print(delivery_date)
    the_file = open(file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()
report("Day 1", "um-deliveries-20140519.txt")
report("Day 2", "um-deliveries-20140520.txt")
report("Day 3", "um-deliveries-20140521.txt")