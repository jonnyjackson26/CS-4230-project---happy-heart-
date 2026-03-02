# CS-4230 Milestone 1: Happy Heart
Colton Evans, Tyler Webster, Matthew Jorgensen, and Jonny Jackson

## Run from source (portable on any PC with Python 3)

This is the most reliable way to run on other people's computers.

1. Open a terminal in this project folder.
2. Run:

```bash
python3 happy_heart.py data.txt
```

If no input file is provided, the program reads from keyboard input:

```bash
python3 happy_heart.py
```

## Run prebuilt executable (Linux)

If you are on Linux, you can run:

```bash
/dist/happy_heart data.txt
```



## Example:
```
python happy_heart.py  data.txt 
00:00   None            Everything normal
00:10   None            Everything normal
00:20   None            Everything normal
00:30   None            Everything normal
00:40   None            Everything normal
00:50   None            Everything normal
01:00   None            Everything normal
01:10   None            Everything normal
01:20   None            Everything normal
01:30   Alarm.MEDIUM Alarm      Pulse very low (35)
01:40   Alarm.HIGHEST Alarm     Pulse critically low (18)
01:50   None            Everything normal
02:00   Alarm.LOW Alarm Oxygen slightly low (84.8%)
02:10   Alarm.LOW Alarm Oxygen slightly low (83.3%)
02:20   Alarm.LOW Alarm Oxygen slightly low (81.8%)
02:30   Alarm.LOW Alarm Oxygen slightly low (80.3%)
02:40   Alarm.MEDIUM Alarm      Oxygen dangerously low (78.8%)
02:50   Alarm.MEDIUM Alarm      Pulse too high (140)
03:00   Alarm.HIGHEST Alarm     Pulse dangerously high (180)
03:10   Alarm.MEDIUM Alarm      Oxygen dangerously low (75.5%)
03:20   Alarm.MEDIUM Alarm      Oxygen dangerously low (74.7%)
03:30   Alarm.MEDIUM Alarm      Oxygen dangerously low (74.0%)
03:40   Alarm.LOW Alarm Oxygen sensor missing
03:50   Alarm.MEDIUM Alarm      Oxygen dangerously low (76.3%)
04:00   Alarm.MEDIUM Alarm      Oxygen dangerously low (79.3%)
04:10   Alarm.LOW Alarm Oxygen slightly low (82.5%)
04:20   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:30   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:40   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:50   Alarm.HIGHEST Alarm     Blood pressure critically low (40/30)
@jonnyjackson26 ➜ /workspaces/CS-4230-project---happy-heart- (main) $ python3 happy_heart.py  data.txt 
00:00   None            Everything normal
00:10   None            Everything normal
00:20   None            Everything normal
00:30   None            Everything normal
00:40   None            Everything normal
00:50   None            Everything normal
01:00   None            Everything normal
01:10   None            Everything normal
01:20   None            Everything normal
01:30   Alarm.MEDIUM Alarm      Pulse very low (35)
01:40   Alarm.HIGHEST Alarm     Pulse critically low (18)
01:50   None            Everything normal
02:00   Alarm.LOW Alarm Oxygen slightly low (84.8%)
02:10   Alarm.LOW Alarm Oxygen slightly low (83.3%)
02:20   Alarm.LOW Alarm Oxygen slightly low (81.8%)
02:30   Alarm.LOW Alarm Oxygen slightly low (80.3%)
02:40   Alarm.MEDIUM Alarm      Oxygen dangerously low (78.8%)
02:50   Alarm.MEDIUM Alarm      Pulse too high (140)
03:00   Alarm.HIGHEST Alarm     Pulse dangerously high (180)
03:10   Alarm.MEDIUM Alarm      Oxygen dangerously low (75.5%)
03:20   Alarm.MEDIUM Alarm      Oxygen dangerously low (74.7%)
03:30   Alarm.MEDIUM Alarm      Oxygen dangerously low (74.0%)
03:40   Alarm.LOW Alarm Oxygen sensor missing
03:50   Alarm.MEDIUM Alarm      Oxygen dangerously low (76.3%)
04:00   Alarm.MEDIUM Alarm      Oxygen dangerously low (79.3%)
04:10   Alarm.LOW Alarm Oxygen slightly low (82.5%)
04:20   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:30   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:40   Alarm.MEDIUM Alarm      Blood pressure dangerously high (210/130)
04:50   Alarm.HIGHEST Alarm     Blood pressure critically low (40/30)
@jonnyjackson26 ➜ /workspaces/CS-4230-project---happy-heart- (main) $ 
```