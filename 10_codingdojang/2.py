a = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
names = a.split(",")

lee = 0
kim = 0
ljy = 0

for name in names:
    last_name = name[0]
    if last_name == "이":
        lee += 1
        if last_name == "김":
            kim += 1
    if name == "이재영":
        ljy += 1

print(lee, kim, ljy)

uniq_names = list(set(names))
print(uniq_names)

uniq_names.sort()
print(uniq_names)
