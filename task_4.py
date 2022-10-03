# import requests
# import pprint
# from bs4 import BeautifulSoup
# movie =("https://www.imdb.com/india/top-rated-indian-movies/")
# page=requests.get(movie)
# soup = BeautifulSoup(page.text,"html.parser")
# Top_movie=[]
# def scrap_top_list():
#     main_div = soup.find("div",class_ ="lister")
#     tbody = main_div.find("tbody",class_= "lister-list")
#     trs=tbody.find_all("tr")
    
#     movie_rank=[]
#     movie_name=[]
#     release_year=[] 
#     movie_url=[]
#     movie_rating=[]
#     # print(trs)
#     for tr in trs:
#         pos=tr.find("td", class_="titleColumn").get_text().strip()
#         rank=""
#         for i in pos:
#             if "." not in i:
#                 rank=rank+i
#             else:
#                 break
         
#         movie_rank.append(rank)


#         title=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(title)

#         year=tr.find("td",class_="titleColumn").span.get_text()
#         release_year.append(year)

#         rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         movie_rating.append(rating)

#         link=tr.find("td",class_="titleColumn").a["href"]
#         movie_link="https://www.imdb.com"+link
#         movie_url.append(movie_link)
#     Top_movie=[]
#     details={"positions":"","name":"","year":"","rating":"","url":""}
#     for i in range(0,len(movie_rank)):
#         details["positions"]=int(movie_rank[i])
#         details["name"]=str(movie_name[i])
#         release_year[i]=release_year[i][1:5]
#         details["year"]=int(release_year[i])
#         details["rating"]=float(movie_rating[i])
#         details["url"]=movie_url[i]
#         Top_movie.append(details.copy())
#     return Top_movie

# scrapped=scrap_top_list()
# print(scrapped)
import requests
from bs4 import BeautifulSoup

def scrap_movie_detail(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
     


#     #Here i scrap movie name

    title_div=soup.find("div",class_="sc-80d4314-1 fbQftq").h1.get_text()
    return title_div
url1="https://www.imdb.com/title/tt0066763/"
print(scrap_movie_detail(url1))

#     movie_name=""
#     for i in title_div:
#         if "(" not in i:
#             movie_name=(movie_name+i).strip()
#         else:
#             break
    
    
#     #n this div where i get all the other things like runtime,gender and more
#     sub_div=soup.find("div",class_="subtext")

#     #Here i scrap movie run time
#     runtime=sub_div.find("time").get_text().strip()
#     runtime_hours=int(runtime[0])*60
#     if "min" in sub_div:
#         runtime_minutes=int(movie_runtime[3:].strip("min"))
#         movie_runtime=runtime_hours+runtime_minutes
#     else:
#         movie_runtime=runtime_hours

#     #Here i scrap movie gener

#     gener=sub_div.find_all("a")
#     gener.pop()
#     movie_gener=[i.get_text() for i in gener]

#     #movie bio and movie director
#     summary=soup.find("div",class_="plot_summary")
#     # Here i scrap movie_bio
#     movie_bio=summary.find("div",class_="summary_text").get_text().strip()

#     #Here i scrap diractor of movie
#     director=summary.find("div",class_="credit_summary_item")
#     director_list=director.find_all("a")
#     movie_directors=[i.get_text().strip() for i in director_list]

#     #in thisdiv i get country and launguage detail 

#     extra_details=soup.find("div",attrs={"class":"artical","id":"titleDetails"})
#     list_of_divs=extra_details.find_all("div")
#     for div in list_of_divs:
#         tag_h4=div.find_all("h4")
#         for text in tag_h4:
#             if "Language" in text:
#                 tag_anchor=div.find_all("a")
#                 movie_country="".join([country.get_text() for country in tag_anchor])
    
#     #Her i scrap poster url
#     movie_poster_link=soup.find("find",class_="poster").a["href"]
#     movie_poster="https://www.imdb.com"+movie_poster_link

#     #Here i create dic for movie-details

#     movie_detail_dic={"name":"","bio":"","runtime":"","gener":"","language":"","country":"","poster_img_url":""}

#     movie_detail_dic["name"]=movie_name
#     movie_detail_dic["director"]=movie_directors
#     movie_detail_dic["bio"]=movie_bio
#     movie_detail_dic["runtime"]=movie_runtime
#     movie_detail_dic["gener"]=movie_gener
#     movie_detail_dic["country"]=movie_country
#     movie_detail_dic["poster_img_url"]=movie_poster

#     return movie_detail_dic
# url1=scrapped[0]["url"]
# movie_detail=scrap_movie_detail(url1)
# print(movie_detail)



