CS 4230

Project 5: The Happy Heart Program

This program monitors the heart functions of a hospital patient. Its main purpose is to raise alarms if there is something seriously wrong, and the patient might die. Specifically, it monitors the following:
Pulse rate
Blood pressure
Blood oxygen level

If this were a real system, it would be software in a special machine with sensors providing the data. But since we don’t have any fancy hardware (or any real patients, for that matter), we will make do with simulated data, as follows:

The data is read in either from a file or from the keyboard. Have a way of allowing the user to do either. For example, the filename could be given on the command line, and if there isn’t one, then assume the input comes from the keyboard. 
Assume that you get data every 10 seconds. You always get a pulse reading; you normally get an oxygen level (but see below), and get a blood pressure reading at irregular intervals (every few minutes, but the frequency isn’t specified.)
Every time you read data, (i.e., simulation of every 10 seconds), print the status. The status consists of a time stamp (start monitoring at time 0, and then each line comes 10 seconds after that), followed by an alert level (text: None, Low, Medium, Highest), followed by a description of the problem causing the alert (for example: “Blood pressure too high”.) Messages are unique for each case; for example, there are two alarm levels for high blood pressure (see below); use messages such as “Blood pressure too high” and “Blood pressure dangerously high.” Don’t use “Blood pressure too high” for both. Alarms should print the associated data; see example.

Example:
00:00	Med Alarm	Blood pressure elevated (145/100)
00:10	None		Everything normal

Times are mm:ss, and wrap around every hour.

Note: print the data input before (or on) each status line; it will make it easier to test.

Have each input line represent a set of data, with a pulse reading, an oxygen level (which might not be there), and a blood pressure (which is often not there.) Feel free to use a more complicated scheme, if you wish. Note that the data do not have a time stamp.

Sample input format (recommended only):
86 92 120/80
88 91.5
88 91.3
87
85 89.4
84 89.0 122/81

Bad data, including impossible values, is considered an equipment malfunction, and should be reported as a minor alarm. (Note that a data input line might have legitimate data for one sensor, and out of range data for another.) (If input is invalid, though, you might not be able to tell what field it should be. Report it as invalid, and keep the program running.)

Characteristics of the data:

Pulse is a number (integer) from 0 to 260. Nobody’s heart can beat 260 beats a minute, and if it’s zero, well, you can figure out what that means.
Oxygen level is a percentage, ranging from 0 to 99.9. One decimal place of precision is all that is needed, though it wouldn’t necessarily be an error if the input contains greater precision.
Blood pressure consists of the systolic reading (the high number), and the diastolic reading (the low number.) They are integer values. They are usually displayed in what looks like a fraction, e.g., 120/80. Of course, you are free to define their format in the input file and input from the keyboard. The maximum possible values are 260 for the systolic, and 150 for the diastolic.

Monitoring:

Basically, what you do is monitor the data continuously, and raise alarms to alert the nurses of any problems. There are three levels of alarms:

Highest: life threatening problem detected
Medium: dangerous condition detected
Low: potential problem; maybe it’s an equipment problem

When reporting, report the alarm for as long as it lasts; until the problem is resolved. Report ONLY the highest level of alarm; if there is a cardiac arrest, the nurses don’t care that there also a low priority problem!
When reporting an alarm, give a short description of the problem. If there are two or more simultaneous alarms of the same level, report only one, in this order of precedence:
Pulse
Oxygen
Blood pressure

Alarm Levels:

Pulse:
Under 20 – highest
Under 40 – medium
Above 110 – low
Above 130 – medium
Above 170 – highest
Above 210 is impossible


Oxygen:

The oxygen level is based on a one minute moving average of the oxygen level.
Average below 50% -- highest
Average below 80% -- medium
Average below 85% -- low
If the reading is missing for 30 seconds (3 consecutive readings), this is a low alarm. It usually indicates that the reading device fell off the patient’s finger. (This invalidates the moving average.) (If the data is missing for one or two readings, assume that the value is the same as the last reading.)
If the oxygen level average is displayed, display it with one digit to the right of the decimal point (1/10th accuracy)
Levels of 0% or less, and 100% or higher, are of course impossible.

Blood Pressure:

In the blood pressure, raise an alarm if either of the numbers exceeds the threshold.
Above 200/120 – medium
Above 150/90 – low
Below 70/40 – medium
Below 50/33 – highest
Levels above 230/150 are impossible.
Since blood pressure is taken at irregular intervals, if it doesn’t appear, that isn’t a problem. If there is an alarm active for blood pressure, keep it until you get another reading.

Note: in case it wasn’t clear, keep reporting an alarm until additional data is read that fixes the alarm.


                           