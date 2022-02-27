import json
with open('data.json') as json_file:
	data = json.load(json_file)
#print(json.dumps(data, indent = 4))
print('Interface Status')
print('='*80)
names = ['DN', 'Description', 'Speed', 'MTU']
form = "{:<47}  {:<15}  {:<10}  {:<6}"
print(form.format(*names))
print('-'*47 + '  ' + '-'*15 + '  ' + '-'*10 + '  ' + '-'*6)
n = data["totalCount"]
for i in data['imdata']:
	dat = i['l1PhysIf']['attributes']
	print(form.format(*(dat['dn'], '' if dat.get('description') == None else dat['description'], dat['speed'], dat['mtu'])))
