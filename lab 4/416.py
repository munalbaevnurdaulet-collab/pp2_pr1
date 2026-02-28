from datetime import datetime, timedelta

def parse_line(line: str) -> datetime:
    date_part, time_part, tz_part = line.split()
    dt = datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H:%M:%S")
    sign = 1 if "+" in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm)
    return dt - offset if sign == 1 else dt + offset

start_utc = parse_line(input().strip())
end_utc = parse_line(input().strip())

print(int((end_utc - start_utc).total_seconds()))