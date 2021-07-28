sec = input("Enter the seconds:")
sec = int(sec)
hours = sec//3600
remaining_sec = sec%3600
minutes = remaining_sec//60
final_sec = remaining_sec%60
print("hours", hours, "minutes", minutes, "seconds", final_sec)