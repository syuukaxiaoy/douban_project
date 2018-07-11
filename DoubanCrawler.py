import expanddouban
import csv
from bs4 import BeautifulSoup

starting_url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,"
#得到url
def getMovieUrl(category, location):
    url = starting_url + category + "," + location
    return url
#定义电影的类
class Movie():
    def __init__ (self, name, rate, category, location, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.category = category
        self.location = location
        self.info_link = info_link
        self.cover_link = cover_link

    def print_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location,
                                          self.category, self.info_link, self.cover_link)


#得到电影的HTML
def getmovieHTML(url):
    return expanddouban.getHtml(url,loadmore=True)

#获得电影信息
def getMovies(category, location):
    movies = []
    for cat in category:
        for loc in location:
            html = expanddouban.getHtml(getMovieUrl(cat, loc), True)
            soup = BeautifulSoup(html, "html.parser")
            content_a = soup.find(class_ = "list-wp").find_all("a", recursive = False)
            for element in content_a:
                m_name = element.find(class_ = "title").string
                m_rate = element.find(class_ = "rate").string
                m_location = loc
                m_category = cat
                m_info_link = element.get("href")
                m_cover_link = element.find("img").get("src")
                movies.append([m_name, m_rate, m_location, m_category, m_info_link, m_cover_link])
    return movies

category_list = ["音乐", "黑色幽默", "家庭"]
location_list = ["大陆", "美国","香港","台湾","日本","韩国","英国","法国","德国","意大利",
                 "西班牙","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]

#写入csv
def write_to_csv():
    movies_list = getMovies(category_list, location_list)
    with open("movies.csv", "w", encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        for row in movies_list:
            writer.writerow(row)

#计算结果并写入txt
m = "{}电影数量排名前三的地区是{},{},{}, 分别占此类电影总数的百分比为{},{},{}. \n"
def percent(count, sum):

    pct = "%.2f%%" % (count / sum * 100)
    return pct


with open("output.txt", "w") as f:
    with open("movies.csv", "r", encoding="utf-8") as csvfile:
        movicesCsv=list(csv.reader(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL))

    for cat in category_list:
        temp = []
        sum = 0
        for loc in location_list:
            count = 0
            for movie in movicesCsv:
                if movie[3] == cat and movie[2] == loc:
                    count +=1
                    sum +=1
            temp.append((loc, count))
            temp = sorted(temp, key = lambda x:x[1], reverse = True)
        pct = []
        for i in range(3):
            pct.append(percent(temp[i][1], sum))
        print(m.format(cat, temp[0][0], temp[1][0], temp[2][0], pct[0], pct[1], pct[2]))
        f.write(m.format(cat, temp[0][0], temp[1][0], temp[2][0], pct[0], pct[1], pct[2]))


if __name__=="__main__":
    write_to_csv()
    percent()