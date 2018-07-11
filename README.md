
# douban_movie
--------------------------------------------------

## 项目概述

在这个项目中, 从豆瓣电影的网页中获取三个电影类别，各个地区的高评分电影，收集了他们的名称、评分、电影页面的链接和电影海报的链接。最后对收集的数据进行简单的统计。

### 任务1:获取每个地区、每个类型页面的URL

url格式为：
https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影

分解 URL 可以看到其中包含

+ ```https://movie.douban.com/tag/#/```: 豆瓣电影分类页面
+ ```sort=S```: 按评分排序
+ ```range=9,10```: 评分范围 9 ~ 10
+ ```tags=电影```: 标签为电影

其中参数```tags```可以包含多个以逗号分隔的标签，可以分别选取类型和地区来进行进一步的筛选,我选择了```音乐``` ```黑色幽默``` ```家庭``` 三个类型。

### 任务2: 获取电影页面 HTML

获得URL后，获取 ```URL``` 对应页面的 ```HTML```使用库 ```requests get``` 函数。

```import requests
response = requests.get(url)
html = response.text```

### 任务3: 定义电影类

电影类包含以下变量

+ 电影名称
+ 电影评分
+ 电影类型
+ 电影地区
+ 电影页面链接
+ 电影海报图片链接


### 任务4: 获得豆瓣电影的信息

通过URL返回的HTML，获取网页中所有电影的名称，评分，海报图片链接和页面链接，同时在任务1构造URL时，也有类型和地区的信息，因为完整的构造每一个电影，并得到一个列表。

### 任务5: 构造电影信息数据表

从网页上选取最爱的三个电影类型，然后获取每个地区的电影信息后，获得一个包含三个类型、所有地区，评分超过9分的完整电影对象的列表。将列表输出到文件 ```movies.csv```。

### 任务6: 统计电影数据

统计所选取的每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比。

结果输出文件 ```output.txt```。
