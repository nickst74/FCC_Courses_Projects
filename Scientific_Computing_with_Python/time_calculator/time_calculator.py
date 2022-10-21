def add_time(start, duration, start_day = None):
  # parse start time
  [hr, min, tok] = start.replace(':', ' ').split()
  hr = int(hr); min = int(min)
  # convert to 24hour format
  if tok == 'PM' and hr < 12:
    hr += 12
  if tok == 'AM' and hr == 12:
    hr = 0
    
  #parse duration
  [dhr, dmin] = duration.split(':')
  dhr = int(dhr); dmin = int(dmin)

  # calculate return time
  ret_hr = hr + dhr
  ret_min = min + dmin
  if ret_min >= 60:
    ret_hr += ret_min // 60
    ret_min %= 60
  days_later = ret_hr // 24
  ret_hr %= 24
  
  # convert back to 12hour format
  if ret_hr >= 12:
    tok = 'PM'
    if ret_hr != 12:
      ret_hr -= 12
  else:
    tok = 'AM'
    if ret_hr == 0:
      ret_hr = 12
    
  # format time
  ret_hr = str(ret_hr)
  ret_min = ("0" + str(ret_min))[-2:]
  new_time = ret_hr + ":" + ret_min + " " + tok
    
  # find what day if needed
  if(start_day is not None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    old_day_idx = days.index(start_day.capitalize())
    new_day = days[(old_day_idx + days_later) % len(days)]
    new_time += ", " + new_day
  # add day delay
  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += " (" + str(days_later) + " days later)"
  return new_time
