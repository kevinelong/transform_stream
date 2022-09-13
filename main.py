import sys
# RUN FROM COMMAND LINE LIKE THIS
# $ python main.py < input.txt > output.txt

# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
# CTRL-D in terminal after typing input will stop looping through terminal input.
for line in sys.stdin:

    if 'foo' in line:
        line = line.replace("bar", "barbarino")

    print(line, end="")


