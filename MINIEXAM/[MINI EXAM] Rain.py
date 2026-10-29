weather=input()
air_speed=input()
if weather=="Gloomy" and air_speed=="High"\
    or weather=="Gloomy" and air_speed=="Medium":
    print("100%")
elif weather=="Cloudy":
    print("50%")
elif weather=="Clear" and air_speed=="Low":
    print("0%")
else:
    print("Not sure.")
