import requests
from bs4 import BeautifulSoup
movie =("https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(movie)
soup = BeautifulSoup(page.text,"html.parser")

def scrap_top_list():
    main_div = soup.find("div",class_ ="lister")
    tbody = main_div.find("tbody",class_= "lister-list")
    trs=tbody.find_all("tr")
    
    movie_rank=[]
    movie_name=[]
    release_year=[] 
    movie_url=[]
    movie_rating=[]
    # print(trs)
    for tr in trs:
        pos=tr.find("td", class_="titleColumn").get_text().strip()
        rank=""
        for i in pos:
            if "." not in i:
                rank=rank+i
            else:
                break
         
        movie_rank.append(rank)


        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find("td",class_="titleColumn").span.get_text()
        release_year.append(year)

        rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)

        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_url.append(movie_link)
    Top_movie=[]
    details={"positions":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_rank)):
        details["positions"]=int(movie_rank[i])
        details["name"]=str(movie_name[i])
        release_year[i]=release_year[i][1:5]
        details["year"]=int(release_year[i])
        details["rating"]=float(movie_rating[i])
        details["url"]=movie_url[i]
        Top_movie.append(details.copy()) 
    return Top_movie

print(scrap_top_list())


 