import requests
import pprint
from bs4 import BeautifulSoup
movie =("https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(movie)
soup = BeautifulSoup(page.text,"html.parser")
Top_movie=[]
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

scrapped=scrap_top_list()

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
        
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    return movie_dict
dec_arg=(group_by_year(scrapped))

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    return (moviedec)
pprint.pprint(group_by_decade(dec_arg))