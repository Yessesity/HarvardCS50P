---------------------------------------------
*** POMODORO TIME SCHEDULER ***
---------------------------------------------

---------------------------------------------
CONCEPT 1: SCHEDULE BLOCK STYLE
---------------------------------------------

1. User inputs time that they are available.

Start time: (input here)
End time: (input here)

2. Subtract the start time from the end time to figure out the total available time in minutes that the user is available for.

3. Outputs a complete schedule block with pomodoro spacing between each work time.

E.g.
Pomodoro 1
9:00am to 9:25am 
Break 1
9:25 am to 9:30 am
...

4. Starts a timer once the system clock matches the first occurance of Pomodoro

5. Plays an alarm once timer runs out.

6. After 5-10 seconds start the timer for Break. Repeat steps 4 to 6.

7. Allow configuration for length of Pomodoro and Break times in minutes. Store configuration in "config.csv".

---------------------------------------------
CONCEPT 2: ALARM CLOCK STYLE
---------------------------------------------

1. User starts the timer for the first cycle of Pomodoro by typing Start.

2. User can pause the timer by typing pause.

3. An alarm rings out once time has run out for Pomodoro.

4. An alarm rings out once time has run out for Break.

5. Allow configuration for length of Pomodoro and Break times in minutes. Store configuration in "config.csv".