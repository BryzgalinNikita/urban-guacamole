import json

def employees_rewrite(sort_type):

    with open('employees.json', 'r') as f:
        data = json.load(f)

    if sort_type == 'string':
        data_sorted = sorted(data, key=lambda x: x['name'])
    elif sort_type == 'number':
        data_sorted = sorted(data, key=lambda x: x['salary'], reverse=True)
    else:
        print("Unsupported sort type. Please choose 'string' or 'number'.")
        return

    with open(f'employees_{sort_type}_sorted.json', 'w') as f:
        json.dump(data_sorted, f, indent=4)

employees_rewrite('string')

employees_rewrite('number')
