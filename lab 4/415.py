from datetime import datetime, timedelta

DAY = 86400

def is_leap(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def parse_line(line: str):
    date_part, tz_part = line.split()
    y, m, d = map(int, date_part.split("-"))
    sign = 1 if "+" in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = sign * (hh * 60 + mm)  # minutes
    return y, m, d, offset

def local_midnight_to_utc(y: int, m: int, d: int, offset_min: int) -> datetime:
    dt_local = datetime(y, m, d, 0, 0, 0)
    return dt_local - timedelta(minutes=offset_min)

by, bm, bd, birth_off = parse_line(input().strip())
cy, cm, cd, curr_off = parse_line(input().strip())

current_utc = local_midnight_to_utc(cy, cm, cd, curr_off)

def birthday_date_for_year(year: int):
    if bm == 2 and bd == 29 and not is_leap(year):
        return year, 2, 28
    return year, bm, bd

cand_y, cand_m, cand_d = birthday_date_for_year(cy)
cand_utc = local_midnight_to_utc(cand_y, cand_m, cand_d, birth_off)

if cand_utc < current_utc:
    cand_y, cand_m, cand_d = birthday_date_for_year(cy + 1)
    cand_utc = local_midnight_to_utc(cand_y, cand_m, cand_d, birth_off)

diff_seconds = int((cand_utc - current_utc).total_seconds())

if diff_seconds <= 0:
    print(0)
else:
    print((diff_seconds + DAY - 1) // DAY)