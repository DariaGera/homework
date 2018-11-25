dataset = {
			'bob@kpi.ua':{
							'person': {
										'name':'Bob',
										'email':'bob@kpi.ua'
										},
							'foods': {
										'apple':[1.3,12.1],
										'milk':[45]
										}							
							},
						
			'boba@kpi.ua':{
							'person': {
										'name':'Boba',
										'email':'boba@kpi.ua'
										},
							'foods': {
										'milk':[35]
										}						
							}
			}
#---------------recursive functia---------------------	
def func(NumberKey):
	if NumberKey == 0:
		return 0
	else:
		func(NumberKey-1)
		NamesList.append(dataset[listKeys[NumberKey-1]]['person']['name'])
#---------------simple functia---------------------	
def funcProducts():
	appls = 0
	milk = 0
	
	for a in dataset:
		milk+=len(dataset[a]['foods']['milk'])
		
	appls=len(dataset['bob@kpi.ua']['foods']['apple'])
	dictProducts = dict(apple=appls, milk=milk)
	return dictProducts
#---------------simple cost functia---------------------	
def funcCostProducts():
	name = []
	milk = []
	
	for a in dataset:
		name.append(dataset[a]['person']['name'])
		milk.append(dataset[a]['foods']['milk'])

	appls=dataset['bob@kpi.ua']['foods']['apple'][0]+dataset['bob@kpi.ua']['foods']['apple'][1]
	
	dictCostProducts = dict(name1=name[0], milk1=milk[0][0], apple=appls, name2=name[1], milk2=milk[1][0])
	return dictCostProducts
#-------------------main---------------------------------
listKeys = []
NamesList = []
k = 0
for a in dataset:
	listKeys.append(a)
	k = k + 1		

func(k)
print(NamesList)
print(funcProducts())
print(funcCostProducts())
