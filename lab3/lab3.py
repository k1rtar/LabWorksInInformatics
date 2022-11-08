import re

##first task
print('##first task\n')
tests = ["","=-{","=-{P=-{P","dgdgdgd=-{Pgdg={Pd=-{P","=-=-{=-{PP{P"]

for test in tests:
    result = len(re.findall(r'=-{P',test))
    print(result)

##second task
print('\n\n##second task\n')
tests = ["Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже точно кончится.",
         "3243200:00:00234423","00","03:69","01:01:0123:0244:33:33","19:50:60","19:50:59","14:47:70"]


for test in tests:
    result = re.sub(r'(?<![:\d])([01]\d|2[0-3])(:[0-5]\d){1,2}(?![:\d])','(TBD)',test)
    print(result)

##third task
print('\n\n##third task\n')
tests = ["students.spam@yandex.ru","example@example","example@example.com",
         "foo.@ya.ru", "foo@.ya.ru",
         "boo@ya_ru", ".boo@ya.ru.", "foo#boo@ya.ru"]

for test in tests:
    result = re.match(r'([a-zA-Z\d._]{1,})@([a-zA-Z.]{1,})\.([a-zA-Z.]{1,})',test)
    print(result.group(2)+'.'+result.group(3) if result else "Fail!")
