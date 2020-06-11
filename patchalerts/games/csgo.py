from wrappers.update import Update
from games.base_class import Game
from util import loader


class CSGO(Game):
	def __init__(self):
		super().__init__('CS:GO', homepage='http://blog.counter-strike.net/')

	def scan(self):
		soup = loader.soup("http://blog.counter-strike.net/index.php/category/updates/")
		elems = soup.find_all(attrs={'class': 'inner_post'})
		for elem in elems:
			link = elem.find('a')
			_url = link["href"]
			_title = link.text
			_desc = self.get_whole_desc(elem)
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#2f2217")


	def get_whole_desc(self, elem):
		_desc = ""
		for p in elem.find_all('p', attrs={'class': None}):
			_desc = _desc + p.text + "\n\n"
		return _desc

if __name__ == "__main__":
	lol = CSGO()
	for u in lol.scan():
		print(u)

