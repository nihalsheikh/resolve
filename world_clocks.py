# Checking time across different countries

from datetime import datetime
from dateutil import tz

# Define time zones
time_zones = {
    "Kolkata-India": tz.gettz("Asia/Kolkata"),
    "Delhi-India": tz.gettz("Asia/Kolkata"),  # Same as Kolkata
    "Dubai-UAE": tz.gettz("Asia/Dubai"),
    "Abu Dhabi-UAE": tz.gettz("Asia/Dubai"),  # Same as Dubai
    "London-UK": tz.gettz("Europe/London"),
    "New York-US": tz.gettz("America/New_York")
}

# Simple ASCII clock template
clock_template = """
        _____
     _.'_____`._
   .'.-'  12 `-.`.
 ,'       |       `.
;;        |        ::
||        |        ||
|| 9 {time}--- 3 ||
||                 ||
::                 ;;
 `.              ,'
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
"""

# Generate Markdown file with ASCII clocks
with open("world_clocks.md", "w") as f:
    f.write("# World Clocks\n\n")
    for city, tz_info in time_zones.items():
        current_time = datetime.now(tz_info).strftime("%H:%M:%S")
        f.write(f"## {city}\n\n")
        f.write("```\n")
        f.write(clock_template.format(time=current_time))
        f.write("```\n\n")
