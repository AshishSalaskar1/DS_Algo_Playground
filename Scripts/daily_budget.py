import datetime


content = ['===== March', '== 6', '549 Phone recharge ', '== 11', '181 jiofi', '900 Kettle', '== 15', '17k Tata MF', '== 16 ', '3k All weather investing ', '== 23', '589 Airtel Fibre ', '== 27', '1000 clothes', '900 bus ticket ', '== 28', "13k Mother's phone", '', '', '===== April ', '== 2', '500 Auto', '100 Snacks on bus', '700 Iron box and others ', '600 groceries', '25k rent ', '== 3', '200 Noodles n food', '== 4', '150 Zomato', '== 5', '300 Umbrella', '100 groceries ', '== 6', '230 zomato ', '== 7', '450 Swiggy ', '', '']

def read_multieline_input():
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents


def process_text(content):

    content = list(filter(lambda x:len(x.strip())!=0 and (x!="\n"), content))
    content = [x.strip() for x in content]

    print(content)
    
    final_res = []
    monthly = []
    daily=[]

    last_day_seen = ""
    last_month_seen = ""

    for line in content:
        sym, line_text = line.split(" ",1)
        if sym  == "=====": # month line
            last_month_seen = line_text
            pass
        elif sym == "==": # day line
            last_day_seen = line_text
        else: # actual spent
            if sym[-1] == "k": # 35k some_description
                line_cost = int(sym[:-1])*1000
            else:
                line_cost = int(sym)
            final_res.append(
                (
                    datetime.datetime.strptime(f"{last_day_seen}-{last_month_seen}-{2023}","%d-%B-%Y"),
                    line_text, 
                    line_cost
                )
            ) 

    return final_res 

def get_monthly_average(contents, cats=False):
    monthly_total = {}

    for ldate, ltext, lcost in contents:
        month = ldate.strftime("%B-%Y")
        if month not in monthly_total:
            monthly_total[month] = []
        else:
            monthly_total[month].append((lcost, ltext, ldate))

    
    monthly_res = []
    for key,val in monthly_total.items():
        monthly_res.append((key,sum([x[0] for x in val])))

    print(monthly_total)
    return monthly_res


content = read_multieline_input()
processed_content = process_text(content=content)

# print(processed_content)
print(get_monthly_average(processed_content))