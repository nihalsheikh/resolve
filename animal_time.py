# Animal says time of different countries

from datetime import datetime
from dateutil import tz

# ASCII art for animals
bison = """
         ___,,___
                                ,d8888888888b,_
                            _,d889'        8888b,
                        _,d8888'          8888888b,
                    _,d8889'           888888888888b,_
                _,d8889'             888888889'688888, /b
            _,d8889'               88888889'     `6888d 6,_
         ,d88886'              _d888889'           ,8d  b888b,  d\
       ,d889'888,             d8889'               8d   9888888Y  )
     ,d889'   `88,          ,d88'                 d8    `,88aa88 9      ,--------------,
    d889'      `88,        ,88'                   `8b     )88a88'     _(                )_,
   d88'         `88       ,88                   88 `8b,_ d888888    0(__    {time}     ,__)
  d89            88,      88                  d888b  `88`_  8888   o   (_______________)
  88             88b      88                 d888888 8: (6`) 88') d
  88             8888b,   88                d888aaa8888, `   'Y'
  88b          ,888888888888                 `d88aa `88888b ,d8
  `88b       ,88886 `88888888                 d88a  d8a88` `8/
   `q8b    ,88'`888  `888'"`88          d8b  d8888,` 88/ 9)_6
     88  ,88"   `88  88p    `88        d88888888888bd8( Z~/
     88b 8p      88 68'      `88      88888888' `688889`
     `88 8        `8 8,       `88    888 `8888,   `qp'
       8 8,        `q 8b       `88  88"    `888b
       q8 8b        "888        `8888'
        "888                     `q88b
                                  "888'
"""

elephant = """
                           _
                          .' `'.__
                         /      \ `'"-,              ,------------,
        .-''''--...__..-/ .     |      \           _(              )_,
      .'               ; :'     '.  a   |        o(_  {time}      _,__)
     /                 | :.       \     =\      o   (_____________)
    ;                   \':.      /  ,-.__;.-;`^
   /|     .              '--._   /-.7`._..-;`
  ; |       '                |`-'      \  =|
  |/\        .   -' /     /  ;         |  =/
  (( ;.       ,_  .:|     | /     /\   | =|
   ) / `\     | `""`;     / |    | /   / =/
     | ::|    |      \    \ \    \ `--' =/
    /  '/\    /       )    |/     `-...-`
   /    | |  `\    /-'    /;
   \  ,,/ |    \   D    .'  \
jgs `""`   \  nnh  D_.-'L__nnh
"""

rhinoceros = """
               _                 __
      __.--**---**--...__..--**----*-.
    .'                                `-.
  .'                         _           \
 /                         .'        .    \   _._
:                         :          :`*.  :-'.' ;
;    `                    ;          `.) \   /.-'
:     `                             ; ' -*   ;
       :.    \           :       :  :        :           ___________
 ;     ; `.   `.         ;     ` |  '                 __(           )__,
 |         `.            `. -*"*\; /        :        0_,    {time}     )
 |    :     /`-.           `.    \/`.'  _    `.     o   (_____________'
 :    ;    :    `*-.__.-*---:`.   \ ;  'o` `. /    d
       ;   ;                ;  \   ;:       ;:   ,/
  |  | |            [bug]      /`  | ,      `*-*'/
  `  : :  :                /  /    | : .    ._.-'
   \  \ ,  \              :   `.   :  \ \   .'
    :  *:   ;             :    |`*-'   `*+-*
    `**-*`""               *---*
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
