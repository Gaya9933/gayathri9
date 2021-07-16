import sys
import re
import datetime

with open(sys.argv[1], 'r') as f:
    date_format = "%m/%d/%y"
    time_format = ""
    time_succeeding_date = False
    delta = datetime.timedelta(days=0, seconds=0, minutes=0, hours=0)
    for line in f:
        str_line = line.strip()
        str_line_tokens = re.split('[:]', str_line, maxsplit=1)
        str_line_token1 = str_line_tokens[0]
        try:
            datetime.datetime.strptime(str_line_token1, date_format)
            time_succeeding_date = True
            #print("This is the correct date string format. "+str_line_token1)
            str_line_token2 = re.split('-', str_line_tokens[1])
            #print(str_line_token2)
            time_token1 = str_line_token2[0].strip()
            time_token2 = re.split(' ', str_line_token2[1].strip())
            #print("Time Tokens" + time_token1 + ", " + time_token2[0])
            datetime1 = datetime.datetime.strptime(time_token1,"%I:%M%p")
            datetime2 = datetime.datetime.strptime(time_token2[0].strip(),"%I:%M%p")
            time_difference = datetime2 - datetime1
            delta = delta + time_difference
            #print(time_difference)
            #print(delta)
        except ValueError:
            #print("This is the incorrect date string format. It should be MM/DD/YY "+str_line)
            if time_succeeding_date == True:
                str_line_tokens3 = re.split('-', str_line, maxsplit=1)
                #print(str_line_tokens3)
                time_token3 = str_line_tokens3[0].strip()
                time_token4 = re.split(' ', str_line_tokens3[1].strip())
                #print("Time Tokens" + time_token3 + ", " + time_token4[0])
                datetime3 = datetime.datetime.strptime(time_token3,"%I:%M%p")
                datetime4 = datetime.datetime.strptime(time_token4[0].strip(),"%I:%M%p")
                time_difference1 = datetime4 - datetime3
                delta = delta + time_difference1
                #print(time_difference1)
                #print(delta)
                time_succeeding_date = False
    print(delta)
f.close()


