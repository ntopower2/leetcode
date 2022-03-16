# Read from the file file.txt and output all valid phone numbers to stdout.
cat file.txt | while read line; do [[ $line =~ ^(\([0-9]{3}\)[[:space:]]|[0-9]{3}-)[0-9]{3}-[0-9]{4}$ ]] && echo $line; done