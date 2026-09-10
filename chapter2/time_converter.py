#gets the number of seconds from user.
total_seconds = float(input("Enter the total seconds: "))

#calulate number of hours
hours = total_seconds // 3600

#calulate the remaining minutes.
minutes = (total_seconds // 60) % 60

#calulate the remaining seconds.
seconds = total_seconds % 60 

#Display the results.
print("Here is the time in hours, minutes, seconds: ")
print("Hours:", hours)
print("Minutes:", minutes)
print("seconds:", seconds)