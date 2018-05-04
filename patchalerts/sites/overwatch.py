from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update
from sites.site_class import Site


class Overwatch(Site):
	def __init__(self):
		super().__init__("Overwatch", 'https://i.imgur.com/f2XybsY.png')

	def scan(self):
		resp = requests.get("https://playoverwatch.com/en-us/game/patch-notes/pc/")
		soup = BeautifulSoup(resp.text, "html.parser")
		bod = soup.find(attrs={'class': 'patch-notes-body'})
		link = soup.find(attrs={'class': 'blog-sidebar-list'}).find('a')

		_title = link.find('h3').text
		_url = 'https://playoverwatch.com/en-us/game/patch-notes/pc/' + link['href']  # First link in sidebar.
		_desc = 'Summary:\n\n'
		pars = bod.find_all('p')
		for p in pars[2:5]:
			_desc += p.text + '\n\n'
		_desc += '...'

		yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#f99e1a")


if __name__ == "__main__":
	lol = Overwatch()
	for u in lol.scan():
		print(u)
