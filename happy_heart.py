"""
Happy Heart Program
CS 4230

Simulates patient monitoring every 10 seconds using pulse, oxygen, and blood pressure data.
Input can come from a file (command-line argument) or keyboard (stdin).
"""

import sys
from collections import deque
from enum import Enum

# helper functions
# -----------------------------

class Alarm(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGHEST = "Highest"
    ERROR = "Low (Error)"

def format_time(seconds):
    seconds = seconds % 3600
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02d}:{ss:02d}"


def parse_line(line):
    """
    Parse a single input line.
    Expected formats (flexible):
      pulse oxygen systolic/diastolic
      pulse oxygen
      pulse
    Returns a dict with possible keys: pulse, oxygen, bp
    Invalid fields are marked as 'invalid'.
    """
    result = {}
    tokens = line.strip().split()

    if not tokens:
        return result

    # Pulse
    try:
        result['pulse'] = int(tokens[0])
    except ValueError:
        result['pulse'] = 'invalid'

    # Oxygen
    if len(tokens) >= 2:
        try:
            result['oxygen'] = float(tokens[1])
        except ValueError:
            result['oxygen'] = 'invalid'

    # Blood pressure
    if len(tokens) >= 3:
        try:
            systolic, diastolic = tokens[2].split('/')
            result['bp'] = (int(systolic), int(diastolic))
        except Exception:
            result['bp'] = 'invalid'

    return result

# alarm eval functions
# -----------------------------

def pulse_alarm(pulse):
    if pulse == 'invalid' or pulse < 0 or pulse > 260:
        return (Alarm.ERROR, 'Invalid pulse reading')
    if pulse == 0 or pulse < 20:
        return (Alarm.HIGHEST, f'Pulse critically low ({pulse})')
    if pulse < 40:
        return (Alarm.MEDIUM, f'Pulse very low ({pulse})')
    if pulse > 210:
        return (Alarm.LOW, 'Impossible pulse reading')
    if pulse > 170:
        return (Alarm.HIGHEST, f'Pulse dangerously high ({pulse})')
    if pulse > 130:
        return (Alarm.MEDIUM, f'Pulse too high ({pulse})')
    if pulse > 110:
        return (Alarm.LOW, f'Pulse elevated ({pulse})')
    return None


def oxygen_alarm(avg, missing_count, invalid):
    if invalid:
        return (Alarm.ERROR, 'Invalid oxygen reading')
    if missing_count >= 3:
        return (Alarm.LOW, 'Oxygen sensor missing')
    if avg is None:
        return None
    if avg <= 0 or avg >= 100:
        return (Alarm.LOW, 'Impossible oxygen level')
    if avg < 50:
        return (Alarm.HIGHEST, f'Oxygen critically low ({avg:.1f}%)')
    if avg < 80:
        return (Alarm.MEDIUM, f'Oxygen dangerously low ({avg:.1f}%)')
    if avg < 85:
        return (Alarm.LOW, f'Oxygen slightly low ({avg:.1f}%)')
    return None


def bp_alarm(bp, active_alarm):
    if bp is None:
        return active_alarm
    if bp == 'invalid':
        return (Alarm.ERROR, 'Invalid blood pressure reading')

    systolic, diastolic = bp
    if systolic < 0 or diastolic < 0 or systolic > 260 or diastolic > 150:
        return (Alarm.ERROR, 'Invalid blood pressure reading')
    if systolic > 230 or diastolic > 150:
        return (Alarm.ERROR, 'Invalid blood pressure reading')
    if systolic < 50 or diastolic < 33:
        return (Alarm.HIGHEST, f'Blood pressure critically low ({systolic}/{diastolic})')
    if systolic < 70 or diastolic < 40:
        return (Alarm.MEDIUM, f'Blood pressure too low ({systolic}/{diastolic})')
    if systolic > 200 or diastolic > 120:
        return (Alarm.MEDIUM, f'Blood pressure dangerously high ({systolic}/{diastolic})')
    if systolic > 150 or diastolic > 90:
        return (Alarm.LOW, f'Blood pressure elevated ({systolic}/{diastolic})')
    return None

# Main monitoring loop
# -----------------------------

def main():
    # Input
    if len(sys.argv) > 1:
        infile = open(sys.argv[1], 'r')
    else:
        infile = sys.stdin

    time_sec = 0
    oxygen_window = deque(maxlen=6)  # 1-minute window (6 * 10s)
    last_oxygen = None
    missing_oxygen = 0
    bp_active_alarm = None

    for raw in infile:
        data = parse_line(raw)

        alarms = []

        # Pulse
        if 'pulse' in data:
            pa = pulse_alarm(data['pulse'])
            if pa:
                alarms.append(('Pulse', pa))

        # Oxygen
        oxygen_invalid = False
        if 'oxygen' in data:
            ox = data['oxygen']
            if ox == 'invalid' or ox <= 0 or ox >= 100:
                oxygen_invalid = True
            else:
                last_oxygen = ox
                oxygen_window.append(ox)
                missing_oxygen = 0
        else:
            if last_oxygen is not None:
                oxygen_window.append(last_oxygen)
                missing_oxygen += 1

        avg_ox = None
        if oxygen_window and missing_oxygen < 3:
            avg_ox = sum(oxygen_window) / len(oxygen_window)

        oa = oxygen_alarm(avg_ox, missing_oxygen, oxygen_invalid)
        if oa:
            alarms.append(('Oxygen', oa))

        # Blood pressure
        bp = data.get('bp', None)
        bp_active_alarm = bp_alarm(bp, bp_active_alarm)
        if bp_active_alarm:
            alarms.append(('Blood Pressure', bp_active_alarm))

        # Choose highest alarm
        priority = {Alarm.ERROR:4, Alarm.HIGHEST: 3, Alarm.MEDIUM: 2, Alarm.LOW: 1}
        precedence = ['Pulse', 'Oxygen', 'Blood Pressure']

        chosen = None
        for level in [Alarm.ERROR, Alarm.HIGHEST, Alarm.MEDIUM, Alarm.LOW]:
            for src in precedence:
                for a in alarms:
                    if a[0] == src and a[1][0] == level:
                        chosen = a[1]
                        break
                if chosen:
                    break
            if chosen:
                break

        if chosen:
            print(f"{format_time(time_sec)}\t{chosen[0]} Alarm\t{chosen[1]}")
        else:
            print(f"{format_time(time_sec)}\tNone\t\tEverything normal")

        time_sec += 10

    if infile is not sys.stdin:
        infile.close()


if __name__ == '__main__':
    main()
