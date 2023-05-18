
def format_departments(staff):
    if isinstance(staff, list) is not True:
        raise TypeError('invalid input, input must be a list')
    if len(staff) == 0:
        raise IndexError('invalid input, list must not be empty')
    for member in staff:
        if isinstance(member, dict) is not True:
            messege = 'invalid_input, input must be a list of dictionaries'
            raise TypeError(messege)
    departments = []
    for member in staff:
        departments.append([member['department']])
    return departments
