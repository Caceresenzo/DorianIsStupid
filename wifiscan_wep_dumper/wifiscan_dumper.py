import csv
import datetime

found = total = 0

with open('wifiscan-export.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        total += 1
        
        if '[WEP]' in row['AP Capabilities']:
            found += 1
            
            for (key, value) in row.items():
                if key == 'Unix time':
                    value += ' [' + datetime.datetime.fromtimestamp(int(value) / 1000).strftime('%d/%m/%y %H:%M') + ']'
                formatted = '{:30}| {:10}'.format(key.strip(), value)
                print('| {:70} |'.format(formatted))
            print('+' + ("-" * 31) + '+' + ("-" * 40) + '+')
    
    
    print('| {:70} |'.format('{:30}| {}'.format('Found values', found)))
    print('| {:70} |'.format('{:30}| {}'.format('Total values', total)))
    print('+' + ("-" * 31) + '+' + ("-" * 40) + '+')