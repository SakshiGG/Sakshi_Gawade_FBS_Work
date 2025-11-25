#WAP convert the time entered in hh,min and sec into seconds.

#Take inputs from user
hrs = int(input('Enter Hours:'))
mins = int(input('Enter Minutes:'))
sec = int(input('Enter Seconds:'))

#convert hours into seconds
hrs_sec = hrs * 60 * 60

#convert minutes into seconds
mins_sec = mins * 60

#convert hh,min and sec into seconds
seconds = hrs_sec + mins_sec + sec

#Display result
print(f'{hrs}hrs: {mins}mins : {sec}sec in seconds is {seconds}sec')
