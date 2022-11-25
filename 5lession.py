season = "summer"
time = "Noon"

print("App is starting")

if season == "winter":
    print("it's cold now")
    if time == "Night":
        print("Are you fool? Sleep.")
    if time == "Day":
        print("Well. And what do you want?")
else:
    print("Slow down with you data")

if season == "summer":
    print("It's probably hot.")
    if time == "Night":
        print("You are going to dancing?")
    if time == "Day":
        print("I will go to vacation this summer.")
    elif time == "Noon":
        print("Hot sun.")
    else:
        print("Slow down with you data")
