import copy

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2} #python3.5++
print(dict3)

dict4 = copy.deepcopy(dict1) #python3.4-- (python2 included)
dict4.update(dict2)
print(dict4)

sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])


employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'salary': 8000}

dict5 = {key: defaults for key in employees}
print(dict5)