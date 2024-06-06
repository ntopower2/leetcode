# Read from the file words.txt and output the word frequency list to stdout.
# egrep -oi [a-z]+ words.txt 
# grep -o is words.txt | wc -l
words=$(paste -s -d" " words.txt | egrep -oE [a-z]+ | sort | uniq)
for word in "${words[@]}"
do
    echo $word 1
done
