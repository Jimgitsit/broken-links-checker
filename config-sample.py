name = "myspider"
allowed_domains = ["example.com", ]
tags = ['a']
start_urls = [
	"http://example.com",
	"http://another-example.com/test"
]
match = ["\/somepath\/", "\/another-path\/"]
show_passed = True
follow = False