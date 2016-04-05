class Article:
	count = 0

	def __init__(self, title, author, text):
		self.author = author
		self.title = title
		self.text = text
		Article.count = Article.count + 1
	
	def print_data(self):
		return self.title + ", " + self.author + ", " + self.text


articte1 = Article("News", "Andrij", "Some text")


articte2 = Article("News 2", "Andrij 2", "Some text 2")
articte3 = Article("News 3", "Andrij 3", "Some text 3")

article_array = [articte1, articte2, articte3]

print( "Object count: " + str(Article.count) )

for article in article_array:
	print( "Article - " + article.print_data() )