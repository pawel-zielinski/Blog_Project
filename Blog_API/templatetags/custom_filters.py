from django import template

register = template.Library()

def range_filter(value):
    counter = 600
    if len(value) >= 600:
        while True:
            if value[counter] == ' ':
                return value[0:counter+1].rstrip() + "(...)"
            elif value[counter+1] == ' ':
                return value[0:counter+1] + "(...)"
            elif value[counter] == '\n':
                return value[0:counter - 1] + "(...)"
            else:
                counter += 1
    else:
        return value

register.filter('range_filter', range_filter)
