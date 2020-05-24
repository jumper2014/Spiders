# 命令行
- scrapy crawl quotes
- scrapy shell 'http://quotes.toscrape.com/page/1/'
- scrapy shell 'http://quotes.toscrape.com'
- scrapy crawl quotes -o out/quotes.json
- scrapy crawl quotes -o out/quotes.jl
- scrapy crawl author
- scrapy crawl quotes -o out/quotes-humor.json -a tag=humor 传参
- scrapy crawl douban_movie_top250 -o out/douban.csv