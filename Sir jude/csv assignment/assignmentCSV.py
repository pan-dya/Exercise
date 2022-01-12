import csv
from os import sep
import statistics as st
import matplotlib.pyplot as plt
import datetime

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    wr = open("activity2.csv", "w")
    wr.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2]))
    wr.write("\n")

    for row in reader:
        if (row[0]== 'NA'):
            row[0] = 0
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2]))
        wr.write("\n")

    wr.close()

filename = 'activity2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dictDateDay = {}
    dictIntervalDay = {}
    dictDateEnd = {}
    dictIntervalEnd = {}
            
    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])
        dates = row[1].split('-')
        year, month, day = (int(x) for x in dates)
        numday = (datetime.date(year,month,day).weekday())
        if numday == 5 or numday == 6:
            dates.append("weekend")
            dictDateEnd.setdefault(str(date),[])
            dictDateEnd[str(date)].append(int(steps))

            dictIntervalEnd.setdefault(str(date),[])
            dictIntervalEnd[str(date)].append(int(steps))
        else:
            dates.append("weekday")
            dictDateDay.setdefault(str(date),[])
            dictDateDay[str(date)].append(int(steps))

            dictIntervalDay.setdefault(str(date),[])
            dictIntervalDay[str(date)].append(int(steps))

    listDateEnd = []
    listTotalEnd = []
    listDateDay = []
    listTotalDay = []

    for i in dictDateDay.keys():
        listDateDay.append(i)
        listTotalDay.append(sum(dictDateDay.get(i)))
    for i in dictDateEnd.keys():
        listDateEnd.append(i)
        listTotalEnd.append(sum(dictDateEnd.get(i)))

    listAvePerIntervalDay = []
    for i in dictIntervalDay.keys():
        listAvePerIntervalDay.append(st.mean(dictIntervalDay.get(i)))
    
    listAvePerIntervalEnd = []
    for i in dictIntervalEnd.keys():
        listAvePerIntervalEnd.append(st.mean(dictIntervalEnd.get(i)))
    
    fig = plt.figure(dpi = 80, figsize = (20,6))
    plt.plot(list(dictDateDay.keys()),  listAvePerIntervalDay, c="blue")
    plt.title("Average Daily Activity (Weekday)")
    plt.xlabel("5 Minute Interval")
    plt.ylabel("Average Number of Steps Taken")
    fig.autofmt_xdate()
    plt.savefig("ActivityWeekDay.svg")
    plt.show()
    plt.close()

    fig = plt.figure(dpi = 80, figsize = (20,6))
    plt.plot(list(dictDateEnd.keys()),  listAvePerIntervalEnd, c="blue")
    plt.title("Average Daily Activity (Weekend)")
    plt.xlabel("5 Minute Interval")
    plt.ylabel("Average Number of Steps Taken")
    fig.autofmt_xdate()
    plt.savefig("ActivityWeekDay.svg")
    plt.show()
    plt.close()