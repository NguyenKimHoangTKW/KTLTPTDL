import newspaper


bbc = newspaper.build('https://tuoitre.vn/')

for article in bbc.articles:
    print(article.url)