import json 

class cook_book():

	def makeDish(self):
		count = 1
		ingridients_arr = []
		dish = input('Введите название нового блюда: ')
		total = int(input('Введите количество ингредиентов: '))
		newdish = {dish:{'total':total, 'ingridient' : []}}
		print("=== ингредиенты ===")
		while count <= total:
			print(f'ингредиент №{count}:')
			ingridients = input('Введите через запятую c пробелом наименование игредиента, количетво, единицу измерения: ')
			ingridients= ingridients.lower().split(', ') 
			if len(ingridients) == 3:
				try:
					ingridients_arr.append({'ingridient_name':ingridients[0],'quantity':int(ingridients[1]),'measure':ingridients[2]})
				except ValueError:
					print('Возможно вы не корректно ввели количество. Попробуйте еще раз.')
				else:	
					count += 1
			else:
				print('Возможно данные введены не корректно. Попробуйте еще раз.')
		newdish[dish]['ingridient'] = ingridients_arr
		with open(self.cook_book, 'a') as json_:
			json_.write(json.JSONEncoder().encode(newdish))

	def get_shop_list_by_dishes(self, dishes, person_count): 
		shop_list = {} 
		for dish in dishes: 
			items = self.cook_book.get(dish,None)
			if items is None:
				print(f'блюдо {dish} не обнаружено в меню')
				return {}
			ingridients = items['ingridient']
			for ingridient in ingridients: 
				new_shop_list_item = dict(ingridient) 
				new_shop_list_item['quantity'] *= person_count 
				if new_shop_list_item['ingridient_name'] not in shop_list: 
					shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item 
				else: 
					shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity'] 
		return shop_list 
        

	def print_shop_list(self, shop_list): 
		for shop_list_item in shop_list.values(): 
			print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
			shop_list_item['measure'])) 

	def create_shop_list(self): 
		person_count = int(input('Введите количество человек: ')) 
		dishes = input('Введите блюда в расчете на одного человека (через запятую c пробелом): ').lower().split(', ') 
		shop_list = self.get_shop_list_by_dishes(dishes, person_count) 
		self.print_shop_list(shop_list) 

	def __init__(self,cook_book = 'cook_book.json'):
		self.cook_book = {}
		self.cook_book = cook_book
		if cook_book is None or (not isinstance(cook_book,str)):
			self.cook_book = cook_book
		else:
			try:
				with open(self.cook_book, 'r') as json_:
					for row in json_:
						self.cook_book.update(json.loads(row))
			except FileNotFoundError:
				self.cook_book = open(self.cook_book,'w')
				print(f'создан или прочитан файл рецептов - {self.cook_book}')
			except:
				raise
				return 



if __name__ == "__main__":
	cook = cook_book()