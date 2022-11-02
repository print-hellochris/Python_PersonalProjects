def add_time(start_time,duration_time,week_day=''):

#---Declaring list of days of the week
    days_of_the_week= ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
#---Preparing the strings for parsing    
    week_day = week_day.capitalize()    
    start_time = start_time.replace(' ','')
    duration_time=duration_time.replace(' ','')
    day_period = ''

#---Variable to detect the colons and time period
    colon_index = start_time.index(':')
    period_index = start_time.index('M')    
    colon_index_2 = duration_time.index(':')

#---Separates time from minutes to hours based on the position of the period and colon
    start_hour = start_time[0:colon_index]
    start_minute = start_time[colon_index+1:period_index-1]
    day_period = start_time[period_index-1:]
    duration_hour = duration_time[0:colon_index_2]
    duration_minute = duration_time[colon_index_2+1:]
    days =0
    total_time = 0
    total_minute = 0
    total_time_module = 00
    hours_from_minutes = 00
    total_minute_module = 00

#---Variables for the output    
    minute_output =''
    period_output =''
    whitespace = ' '

#---Creates a variable total hour and total minute
    total_time = int(start_hour) + int(duration_hour) + int(hours_from_minutes)
    total_minute = int(start_minute) + int(duration_minute) +int(total_minute_module)
    hour_output = int(total_time)
    minute_output = int(total_minute)
    how_many_periods = total_time/12
    how_many_periods_module = how_many_periods%12
    is_it_odd_or_even = how_many_periods%2    

#---Assigns variables for the dinal display    
    hour_display = str(hour_output)
    minute_display = str(minute_output)
    days_display =''
    weekday_display=''
    final_point =''
    time_display = ''
#---If the duration time equals 24, then the function will return the same time and show it ends the following day
    if duration_time =='24:00' and week_day in days_of_the_week:        
        starting_point = days_of_the_week.index(week_day)
        final_point = starting_point+1
        if final_point > len(days_of_the_week):
            weekday_display = days_of_the_week[0+(final_point%7)]
        else:
            weekday_display = days_of_the_week[0+(final_point%7)]
               
        time_display = '{0}:{1} {2}, {3} (next day)'.format(start_hour, start_minute, day_period, weekday_display)
        return time_display

    if duration_time == '24:00':
        time_display = '{0}:{1} {2} (next day)'.format(start_hour, start_minute, day_period)        
        return time_display 

#---How many hours does the minutes have?
    if total_minute >59:
        hours_from_minutes = total_minute/60
        total_time = int(start_hour) + int(duration_hour) + int(hours_from_minutes)
        total_minute_module = total_minute%60
        total_minute = total_minute_module
        minute_output = minute_output -60
        hour_output = int(total_time)
        
#---How many days are in the total hours?
    if total_time > 24:
        days = total_time/24
        total_hour_module = total_time%24
        hour_output = int(total_time)

# #---In what period of the day does the task finish?
    how_many_periods = int(how_many_periods)
    if how_many_periods == 0:        
        period_output = day_period
    if how_many_periods/2 ==0:
        day_period = period_output   
    elif how_many_periods/2 != 0:
        if day_period == 'AM':
            period_output = 'PM'            
        elif day_period == 'PM':
            period_output = 'AM'
            days = days+1   
    
#---Makes the Hour lesser than 12 on output    
    while hour_output> 12:        
        hour_output = hour_output - 12
    if hour_output == 12:
        if day_period == 'PM':
            period_output = 'AM'
        elif day_period =='AM':
            period_output ='PM'

#---Assigns variables for the dinal display    
    hour_display = str(hour_output)
    minute_display = str(minute_output)
    days_display =''
    weekday_display=''
    final_point =''
    time_display = ''
    days = int(days)
#---Makes the minutes less than 59 on output
    if minute_output < 9:
        minute_display = '0'+minute_display
#---How many days later?
    if days == 0:
        days_display = ''
    if days ==1:
        days_display = ' (next day)'       

    elif days >1:
        days_display = ' ({0} days later)'.format(int(days))

#----What day of the week?   
    if week_day in days_of_the_week:
        if int(days) < 1:
            weekday_display = week_day
            time_display = hour_display+':'+minute_display+whitespace+period_output+','+whitespace+weekday_display+days_display
        elif int(days) >= 1:
            difference = int(days)%7
            starting_point = days_of_the_week.index(week_day)
            final_point = starting_point + difference
            # weekday_display = days_of_the_week[final_point]
            if final_point > len(days_of_the_week):
                weekday_display = days_of_the_week[0+(final_point%7)]
            else:
                weekday_display = days_of_the_week[0+(final_point%7)]
            
            time_display = hour_display+':'+minute_display+whitespace+period_output+','+whitespace+weekday_display+days_display
    else: 
        time_display ='{}:{} {}{}'.format(hour_display,minute_display,period_output,days_display)
        # time_display = hour_display+':'+minute_display+whitespace+period_output+whitespace+days_display
        return time_display
    
    return time_display
        

print(add_time("8:16 PM", "466:02", "tuesday")) #to return "6:18 AM, Monday (20 days later

print(add_time("11:59 PM", "24:05", "Wednesday")) # to return "12:04 AM, Friday (2 days later)"')