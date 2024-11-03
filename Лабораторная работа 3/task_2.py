# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separator=','):
    first_list = str_1.split(separator)
    second_list = str_2.split(separator)
    set_list_participants = set(first_list)
    intersection_set = set_list_participants.intersection(second_list)
    intersection_list = []
    for i in intersection_set:
        intersection_list.append(i)
    intersection_list.sort()
    return intersection_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

intersection = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", intersection)

