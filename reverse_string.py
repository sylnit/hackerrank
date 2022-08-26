def reverse(string):
    reversed = ''

    for letter in string[::-1]:
        reversed += letter

    return reversed


def reverse2(s):
    return " ".join(reversed(s.split()))


def reverse3(s):
    return " ".join(s.split()[::-1])


print(reverse('samuel'))
