# Python Loop Statements
# 1. The Range Riddle
"""Objective:
The aim of this assignment is to deepen your understanding of Python's range() function and its application
in loops.  You will correct a code snippet, simulate moods for  different days, and create a countdown 
timer.
"""
# Task 1: Your mood today
"""Write a program that prints off different moods for each day of the week. Create a list of moods such
as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week
and for each day, randomly select a mood from the list and print it. Ensure that your program includes 
the use of the random module to select the mood.
"""
import random
moods = ["Happy", "Sad", "Cheerful", "Romantic", "Angry", "Mysterious", "Nervous", "Reflective"]
Days = ["Monday", "Tuesday","Wednesday","Thursday"," Friday", "Saturday", "Sunday"] 
for i in range(len(Days)):
    print(f"It's {Days[i]} I am {random.choice(moods) }")

#2. Double Scoop with Nested Loops
"""The aim of this assignment is to practice using nested loops in Python. You will correct a nested
 loop code snippet, simulate a mood tracker, and generate a multiplication table.
"""
# Task 1: Your Mood Tracker
import random
moods = ["Happy", "Sad", "Cheerful", "Romantic", "Angry", "Mysterious", "Nervous", "Reflective"]
Days = ["Monday", "Tuesday","Wednesday","Thursday"," Friday", "Saturday", "Sunday"] 
time_of_day = ["Morning", "Afternoon", "Night"]
for day in Days:
       for time in time_of_day:
        print(f" On {day} {time}you were {random.choice(moods)}")