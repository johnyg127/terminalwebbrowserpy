from googlesearch import search
print("Welcome To The YT Search Engine!")
search_query = input("Search the yt web: ")
number_results = input("How many results to show (leave empty for 10): ")
if (number_results == ""):
    number_results = "10"

for x in search(search_query, tld="co.in", num=int(number_results), stop=int(number_results), pause=2):
    print("")
    print(x)
    print("")