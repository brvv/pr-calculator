import datetime

pr_date = datetime.datetime(2022, 3, 8)
temp_date = datetime.datetime(2018, 1, 1)
minimum_date = pr_date + datetime.timedelta(days=365)

days_in_year = 365

target_days = 1095



trips = {
        "USA 2018" : (datetime.datetime(2018, 7, 11), datetime.datetime(2018, 7, 18)),
        "Dominican Republic 2018" : (datetime.datetime(2018, 10, 5), datetime.datetime(2018,10, 12)),
        "Istanbul 2019" : (datetime.datetime(2019, 12, 20), datetime.datetime(2020, 1, 1)),
        "Latvia 2021" : (datetime.datetime(2021, 5, 20), datetime.datetime(2021, 8, 15)),
        "USA 2022" : (datetime.datetime(2022, 2, 14), datetime.datetime(2022, 2, 21)),
        "Europe 2022" : (datetime.datetime(2022, 7, 4), datetime.datetime(2022, 8, 29)),
        "Antalya 2022" : (datetime.datetime(2022, 6, 22), datetime.datetime(2022, 7, 4)),
        }


def getValidDays(date : datetime.datetime, pr_date : datetime.datetime, temp_date:datetime.datetime, target_years=5) -> datetime.timedelta:
    start_date = date - datetime.timedelta(days = 5 * days_in_year)

    temp_days = None
    normal_days = 0

    if start_date >= pr_date:
        normal_days = date - start_date
    else:
        normal_days = date - pr_date

    if temp_date >= start_date:
        temp_days = pr_date - temp_date
        start_date = temp_date
    elif start_date <= pr_date:
        temp_days = pr_date - start_date
    else:
        temp_days = datetime.timedelta(days=0)

    #temp days
    for key in trips:
        trip_start, trip_end = trips[key][0], trips[key][1]

        if trip_start >= start_date and trip_end <= pr_date:
            temp_days -= trip_end - trip_start
        elif trip_start >= pr_date and trip_start >= start_date and trip_end <= date:
            normal_days -= trip_end - trip_start
        elif trip_start >= start_date and trip_end >= pr_date:
            temp_days -= pr_date - trip_start
            normal_days -= trip_end - pr_date
        elif trip_start <= start_date and trip_end >= start_date:
            temp_days -= trip_end - start_date
        elif trip_start <= date and trip_end >= date:
            normal_days -= date - trip_start

        
    temp_days = min(datetime.timedelta(days=365), temp_days * 0.5)

    return (temp_days, normal_days)



for i in range(0, 1000):
    delta = datetime.timedelta(days=i)
    curr_date = minimum_date + delta

    (temp_days, normal_days) = getValidDays(curr_date, pr_date, temp_date)
    valid_days = temp_days + normal_days

    if valid_days >= datetime.timedelta(days=target_days):
        print(curr_date, "    free days: ", valid_days - datetime.timedelta(days=target_days), "   temp days: ", temp_days, "   valid days: ", valid_days)