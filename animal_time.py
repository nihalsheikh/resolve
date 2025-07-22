# Animal says time of different countries

from datetime import datetime
from dateutil import tz

# ASCII art for animals
bison = """
       /\\
      /  \\
     /____\\
     |    |
     |    |
     |{time}|
     |    |
     |    |
    /|    |\\
   / |    | \\
  /  |    |  \\
 /___|____|___\\
"""

elephant = """
     _____
    /     \\
   /_______\\
   |  ***  |
   |  ***  |
   | {time} |
   |_______|
   |  ***  |
   |  ***  |
"""

rhinoceros = """
     _____
    /     \\
   /_______\\
   |  ***  |
   | {time} |
   |_______|
   |  ***  |
   |  ***  |
"""

# Get current time in Kolkata
current_time = datetime.now(tz.gettz("Asia/Kolkata")).strftime("%H:%M:%S")

# Write animal ASCII art to Markdown file
with open("animal_time.md", "w") as f:
    f.write("# Animal Time\n\n")
    f.write("## Bison says:\n\n")
    f.write("```\n")
    f.write(bison.format(time=current_time))
    f.write("```\n\n")
    f.write("## Elephant says:\n\n")
    f.write("```\n")
    f.write(elephant.format(time=current_time))
    f.write("```\n\n")
    f.write("## Rhinoceros says:\n\n")
    f.write("```\n")
    f.write(rhinoceros.format(time=current_time))
    f.write("```\n")
