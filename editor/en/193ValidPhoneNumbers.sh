# Read from the file file.txt and output all valid phone numbers to stdout.
egrep -i '^(\([0-9]{3}\)[[:space:]]|[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt