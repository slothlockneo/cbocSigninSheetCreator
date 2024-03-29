# Author: Molly Johnson
# Date:
# Description:

import calendar

####################################################################
### Function Title: incrementDate()
### Arguments: current date current day ofthe week (number and name)
### Returns: the incremented current date, date of the week, and day
### name ofthe week
### Description: Increments the date of the month and date of the week,
### checking for if the end of the week has been reached. Also updates
### the name of the day of the week. returns these updates values.
#################################################################### 
def incrementDate(curDate, dayDate, dayName):
    curDate += 1
    dayDate += 1
    #if day number is > 6, i.e. you've reached end of week, start week days over
    if (dayDate > 6):
        dayDate = 0
    dayName = calendar.day_abbr[dayDate]
    dayName = dayName.upper()
    return curDate, dayDate, dayName

####################################################################
### Function Title: january()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of the new year and MLK day
#################################################################### 
def january(curDate, endDate, dayName, holidayDates, dayDate):
    mlkMondays = 0
    while(curDate <= endDate):
        # if new year's occurs on a sat, will be taken care of in dec
        # if new year's occurs on a sun, push it to mon
        if(curDate == 1):
            if(dayName == "SUN"):
                holidayDates.append(curDate + 1)
            elif(dayName != "SAT"):
                holidayDates.append(curDate)
        if(dayName == "MON"):
            mlkMondays += 1
            # mlk bday falls on 3rd monday of january
            if(mlkMondays == 3):
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title:  february()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of President's day
#################################################################### 
def february(curDate, endDate, dayName, holidayDates, dayDate):
    washBdayMondays = 0
    while(curDate <= endDate):
        if(dayName == "MON"):
            washBdayMondays += 1
            # washington's bday falls on 3rd monday of the month
            if(washBdayMondays == 3):
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: may()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of memorial day
#################################################################### 
def may(curDate, endDate, dayName, holidayDates, dayDate):
    # keep replacing last monday in may w the current one,
    # such that the last monday in may will be the last value
    # assigned to the variable (which can then be added later)
    memorialDayLastMonInMayDate = 0
    while(curDate <= endDate):
        if(dayName == "MON"):
            memorialDayLastMonInMayDate = curDate
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    # add last monday of the month for memorial day
    holidayDates.append(memorialDayLastMonInMayDate)
    return holidayDates

####################################################################
### Function Title: june()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of Juneteenth
#################################################################### 
def june(curDate, endDate, dayName, holidayDates, dayDate):
    # juneteenth holiday
    while(curDate <= endDate):
        if(curDate == 19):
            # if 19th occurs on a sat, add fri to list
            if(dayName == "SAT"):
                holidayDates.append(curDate - 1)
            # if 19th holiday occurs on a sun, add mon to list
            elif(dayName == "SUN"):
                holidayDates.append(curDate + 1)
            else:
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: july()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of July 4
#################################################################### 
def july(curDate, endDate, dayName, holidayDates, dayDate):
    # 4th of july holiday
    while(curDate <= endDate):
        if(curDate == 4):
            # if 4th holiday occurs on a sat, add fri to list.
            if(dayName == "SAT"):
                holidayDates.append(curDate - 1)
            # if 4th holiday occurs on a sun, add mon to list
            elif(dayName == "SUN"):
                holidayDates.append(curDate + 1)
            else:
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: september()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of labor day
#################################################################### 
def september(curDate, endDate, dayName, holidayDates, dayDate):
    laborDayMon = 0
    while(curDate <= endDate):
        if(dayName == "MON"):
            laborDayMon += 1
            # if is first mon of the month, that's labor day
            if(laborDayMon == 1):
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: october()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of indigenous peoples'/columbus day
#################################################################### 
def october(curDate, endDate, dayName, holidayDates, dayDate):
    columbusDayMon = 0
    while(curDate <= endDate):
        if(dayName == "MON"):
            columbusDayMon += 1
            # if is second mon of month, that's columbus day
            if(columbusDayMon == 2):
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: november()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of veterans' day and thanksgiving
#################################################################### 
def november(curDate, endDate, dayName, holidayDates, dayDate):
    thanksgivingThurs = 0
    while(curDate <= endDate):
        # veteran's day celebrated 11th of nov
        if(curDate == 11):
            # if 11h is a sat, add fri to hols list
            if(dayName == "SAT"):
                holidayDates.append(curDate - 1)
            # if 11th is a sun, add mon to hols list
            elif(dayName == "SUN"):
                holidayDates.append(curDate + 1)
            else:
                holidayDates.append(curDate)
        if(dayName == "THU"):
            thanksgivingThurs += 1
            # if is 4th thurs of month, that's thanksgiving
            if(thanksgivingThurs == 4):
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: december()
### Arguments: current date, end date forthe month, name of the day of
### the week, holiday dates list, current day date of the week
### Returns: updated list of holiday dates
### Description: determines what date should be added to the holiday list
### for the observance of christmas and new year's (if new year's day
### falls on a Saturday and would thus be observed Fri Dec 31)
#################################################################### 
def december(curDate, endDate, dayName, holidayDates, dayDate):
    while(curDate <= endDate):
        # if new year's occurs on a sat, add fri dec 31 to hols
        if((curDate == 31) and (dayName == "FRI")):
            holidayDates.append(curDate) 
        # 25th = christmas
        if(curDate == 25):
            # if 25th is on a sat, add fri to hols list
            if(dayName == "SAT"):
                holidayDates.append(curDate - 1)
            # if 25th is on a sun, add mon to hols list
            elif(dayName == "SUN"):
                holidayDates.append(curDate + 1)
            else:
                holidayDates.append(curDate)
        curDate, dayDate, dayName = incrementDate(curDate, dayDate, dayName)
    return holidayDates

####################################################################
### Function Title: calcFedHolidays()
### Arguments: datetime object
### Returns: list of federal holiday dates for a given month
### Description: calculates all federal holiday dates for a given month
### (month provided by the datetime object). will adjust for if the
### federal holiday occurs on a saturday or sunday as needed
####################################################################    
def calcFedHolidays(dateTimeObj):
    holidayDates = []
    curDate = 1
    endDate = calendar.monthrange(dateTimeObj.year, dateTimeObj.month)[1]
    monthName = calendar.month_name[dateTimeObj.month]
    monthName = monthName.upper()
    dayDate = dateTimeObj.weekday()
    dayName = calendar.day_abbr[dayDate]
    dayName = dayName.upper()

    if(monthName == "JANUARY"):
        return january(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "FEBRUARY"):
        return february(curDate, endDate, dayName, holidayDates, dayDate)
    # no fed hols for march or april
    elif(monthName == "MAY"):
        return may(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "JUNE"):
        return june(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "JULY"):
        return july(curDate, endDate, dayName, holidayDates, dayDate)
    # no fed hols for august
    elif(monthName == "SEPTEMBER"):
        return september(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "OCTOBER"):
        return october(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "NOVEMBER"):
        return november(curDate, endDate, dayName, holidayDates, dayDate)
    elif(monthName == "DECEMBER"):
        return december(curDate, endDate, dayName, holidayDates, dayDate)