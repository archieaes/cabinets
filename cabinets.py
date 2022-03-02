# import num2words library to convert numbers to words
# https://github.com/savoirfairelinux/num2words - LGPL-2.1 License
from num2words import num2words

# print info
print("Program prints information about the Finnish Prime Minister and Government based on the given sequence number.")

# first error handling for input - if not number or empty
flag = 0
try:
    seq = int(input("Enter a sequence number to get information about the Finnish Government: "))
except:
    while flag == 0:
        try:
            seq = int(input("Input must be an integer. Enter a sequence number to get information about the Finnish Government: "))
            flag += 1
        except:
            continue

# second error handling for input - if smaller than 1 or bigger than 76
# also if input is not number or empty
flag = 0
while seq < 1 or seq >= 77:
    while seq < 1:
        try:
            print("Input must be greater than zero.")
            seq = int(input("Enter new input: "))
            break
        except:
            flag = 0
            while flag == 0:
                try:
                    seq = int(input("Input must be an integer. Enter a sequence number to get information about the Finnish Government: "))
                    flag += 1
                except:
                    flag = 0
                    continue
    while seq >= 77:
        try:
            print("Input must be smaller than 77. To date, there have been 76 governments in Finland.")
            seq = int(input("Enter new input: "))
            break
        except:
            flag = 0
            while flag == 0:
                try:
                    seq = int(input("Input must be an integer. Enter a sequence number to get information about the Finnish Government: "))
                    flag += 1
                except:
                    flag = 0
                    continue

# source file to get data
filename = "cabinets.txt"

#list for processing
lines = []

# try to open file and complete process
try:
    file = open(filename,'r')
    # remove spaces and add trimmed lines to list
    for line in file:
            x = line.replace("\n", "")
            lines.append(x)

    # format output text with function
    def print_output():

        stringi = str(lines[seq-1])

        first = stringi.find(",")
        second = stringi.find(",",first+1)
        third = stringi.find(",",second+1)

        govordinal = stringi[:int(first)]

        def ordinal(inte):
            res = num2words(inte, to="ordinal_num")
            return res

        ordinal(govordinal)

        primeminister = stringi[first+1:second]
        cabinetord = stringi[second+1:third]
        time_in_office = stringi[third+1:]

        text = "The " + ordinal(govordinal) + " government of Finland:" + "\n" +  ordinal(cabinetord) + " cabinet of Prime Minister " + primeminister + " " + time_in_office + "."

        return(text)

    file.close

    # run function and print output text
    print(print_output())

# if errors with source file do not process
except:
    print("Error with source file: " + filename + " not available.")
