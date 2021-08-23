#indentation error

try:
    z=['abc','def']
    for i in z:
    if i == 'abc':
except IndentationError as e:
    print(e)