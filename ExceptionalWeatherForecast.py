try:
    temp = int(input("Enter the temperature in Farenheit: ")) #Task 1 asking the user to input a number
    celcius = (temp - 32) * 5/9 #Task 2 writing a formula for converting farenheit to celcius
except ValueError: # if the user enters anything other than an integer
    print("That is not a valid number. Try again...") # resulting message if an incorrect answer is given
else: #Task 3 implimenting an else block
    print(f"{temp} degrees Farenheit is {celcius} degrees Celcius!")
finally:
    print("Thanks for using the Weather Forecast app!")