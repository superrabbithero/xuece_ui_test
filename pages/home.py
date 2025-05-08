class HomePage:
	def __init__(self, page):
		self.page = page
		self.baseUrl = "https://xuece-stagingtest1.unisolution.cn/home/content"

	def navigate(self):
		self.page.goto(self.baseUrl)

	

	