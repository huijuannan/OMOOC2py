#-*-coding: utf-8-*-
import datetime
text = ""
print ('How is your day today? -->')

sentinel = 'quit()' # ends when this string is seen
for line in iter(lambda: raw_input(), sentinel):
	text += "%s\n" % line


current_time = datetime.datetime.now()

file = open("DiaryPool.txt","a")
file.write (current_time.__format__('%c')+"\n")
file.write(text+"\n\n")
file.close()
print ("-->Diary is finished. Well done: )")


"""My Diary.

Usage:
  MyDiary.py ship new <name>...
  MyDiary.py ship <name> move <x> <y> [--speed=<kn>]
  MyDiary.py ship shoot <x> <y>
  MyDiary.py mine (set|remove) <x> <y> [--moored | --drifting]
  MyDiary.py (-h | --help)
  MyDiary.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='MyDiary 0.01')
    print(arguments)