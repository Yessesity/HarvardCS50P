# CONFIGURABLE POMODORO TIMER
#### Video Demo:  https://youtu.be/BIQ6nQXgjDk?si=q653P9d6aoVLwpXH
#### Description: This program utilizes the Pomodoro technique wherein rest is periodically done between periods of work. This program allows for the standard work and rest durations (25 minutes work and 5 minutes rest) while also allowing an option where the user can input their desired amount of work and rest.
#### Basic Instructions:
1. Make sure you are running Python version 3.9, this is because the playsound library does not support Python version 3.10 and beyond.

2. Install playsound version 1.2.2, specifically install this version of the library because later versions will generate error, some context: https://stackoverflow.com/questions/68704443/python-playsound-error-261-for-command-the-driver-cannot-recognize-the-specifie

3. Make sure that you have used <cd path/to/pomodoro> in order to make sure alarm.mp3 and config.csv are accessible by the code

4. Follow the text prompts accurately. Even though I have done a lot of error checking, I still cannot assure that all errors are accounted for.

5. Enjoy!

#### Program Explanation:

There are 2 files which are essential for the project to run. These 2 files are alarm.mp3 for the alarm sound to play, and of course project.py.

>binary = get()

Under the main function, project.py calls the get() function in order to get a binary answer (yes or no) from the user. the get()
function prompts the user if they want to use default pomodoro values for work and rest durations or if they want to customize their own values instead.

>work, rest = get_work_rest(binary)

Depending on the answer of the user (binary), the get_work_rest() function will then get the work and rest values. If the user wants the default values to be used for the timer, get_work_rest() returns the default values of (work=25, and rest=5).

If the user wants to customize their own values for work and rest, then the program will prompt the user if they want to use the values that are already set in config.csv.

>except TypeError:

>work, rest = reader()

This is probably where the sketchiest part of the program dwells. I have programmed it so that when the program raises a TypeError, then read config.csv. This is because under the get_duration() function, I have programmed it so that in the instance that the user answers "yes" to the question of "Do you want to open an existing config.csv?", then the program raises a TypeError. I do not exactly remember why I have programmed it in this way, which is unfortunate.

But moving on, after getting the work and rest durations, the timer starts after the user types "yes". The countdown timer function I used here is from this link here: https://stackoverflow.com/questions/68283946/python-count-down-timer-for-date-hour-minute-and-second

The timer first uses the work duration integer then I multiplied that integer by 60 since the timer function I use accepts time in seconds. After depleting the amount of time that was displayed, the program then runs "alarm.mp3". Once "alarm.mp3" has run, the program then prompts the user in order to start the rest duration. After the rest duration has been depleted then the program prompts the user again if they want to repeat another pomodoro cycle. The user can keep repeating for as many cycles as they want. And once they feel like they are done, just answer no to the prompt mentioned earlier.
