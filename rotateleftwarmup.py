#this_is_fake_DheethyaB_RotateLeftwarmupc#1
#c#1

#Written by Dheethya_Balaji
def rotateleft(a, b, c):
    list1 = [a, b, c]
    x = (list1.pop(0))
    list1.append(x)

    return list1

print(rotateleft(1, 2, 3))
