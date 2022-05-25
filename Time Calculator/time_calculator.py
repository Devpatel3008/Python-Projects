def add_time(start, duration,day=None):
  
  #List with Time & AM/PM
  start_time = start.split(' ')
  duration_time = duration.split(' ')
  days_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  #List with Hours & Minutes
  start_time1 = start_time[0].split(':')
  duration_time1 = duration_time[0].split(':')
  start_hours = start_time1[0]
  start_minutes = start_time1[1]
  duration_hours = duration_time1[0]
  duration_minutes = duration_time1[1]

  #Sum of Time
  count = 0
  days = 0
  sum_time = ''
  sum_hours = int(start_hours) + int(duration_hours)
  sum_minutes = int(start_minutes) + int(duration_minutes)
  if sum_minutes >= 60:
    sum_hours = sum_hours + 1
    sum_minutes = sum_minutes - 60
    if len(str(sum_minutes)) == 1:
      sum_minutes = '0' + str(sum_minutes)
  if sum_hours > 12:
    count = sum_hours//12 #To count days
    sum_hours = sum_hours % 12 
    #Exception case when time is b/w 12 to 1
    if sum_hours == 0:
      sum_hours = 12
    if count%2==0:
      pass
    else:
      if start_time[1]=='AM':
        sum_time = 'PM'
        days = count//2
      elif start_time[1]=='PM':
        sum_time = 'AM'
        days = (count //2)+1
      else:
        pass

  elif sum_hours == 12:
    if start_time[1]=='AM':
      sum_time = 'PM'
    elif start_time[1]=='PM':
      sum_time = 'AM'
      days+=1

  else:
    if start_time[1]=='AM':
      sum_time = 'AM'
    elif start_time[1]=='PM':
      sum_time = 'PM'
  #Return if day is True
  if day:
    pos = days_list.index(day.capitalize())
    new_day = pos + days
    if new_day > 6:
      counter = new_day%7
      sum_day = days_list[counter]
    else:
      sum_day = days_list[new_day]
    if days == 0:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+sum_time+" "+sum_day
    elif days == 1:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+sum_time+" (next day)"+" "+sum_day
    else:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+sum_time+" ("+str(days)+" days later)"+" "+sum_day
  #Return if day is not True
  else:
    if days == 0:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+ sum_time
    elif days == 1:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+ sum_time+" (next day)"
    else:
      ans = str(sum_hours)+":"+str(sum_minutes)+" "+ sum_time+" ("+str(days)+" days later)"

  return ans




#Call a function
#add_time("3:00 PM", "3:10")
#add_time("11:43 AM", "00:20")
#add_time("10:10 PM", "3:30")
#add_time("11:30 AM", "2:32")
#add_time("6:30 PM", "205:12","Monday")
#add_time("11:43 PM", "24:20")
#add_time("11:30 AM", "2:32", "Monday")
#add_time("11:43 PM", "24:20", "tueSday")



