path = './Lab05/a/'
with open(f'{path}q5_output.txt', 'w') as file:
    s = input('The output for the input line: ')
    file.write(f'The output for the input line: {s}\n\n')
    clean_s = ''.join(c for c in s if c.isalpha())
    count = dict()

    for c in clean_s:
        count[c] = count.get(c, 0) + 1

    sorted_count = dict(sorted((count.items()), key = lambda item: item[0]))
    print(' ')
    for key, value in sorted_count.items():
        print(f"The letter '{key}' appears {value} time(s).")
        file.write(f"The letter '{key}' appears {value} time(s).\n")



