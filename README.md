# beauty-photography
爬虫习作 Nr. 2: 以佳丽摄影作品网站为目标的定向爬取 

## 目标
爬取四海资讯图库 (https://www.shzx.org/b/12-0.html) 的图集信息, 以及下载图集中的图片
![img](introduction/screenshot-001.PNG)

## 技术栈
主要是Scrapy结合SQLAlchemy. Scrapy爬取网页内容并提取出项目(item), SQLAlcehmy将项目存储在数据库

## 项目结构
```
.
├── logs
│   └── 2019-11-16.log
├── photos
│   └── img.shzx.org
│       ├── 138-7500
│       │   ├── 138-7500-1573929540.webp
│       │   └── 138-7500-1573929818.webp
│       ├── 141-7501
│       │   ├── 141-7501-1573929546.webp
│       │   └── 141-7501-1573929587.webp
│       └── 162-2550
│           ├── 162-2550-1573929592.jpg
│           └── 162-2550-1573929596.jpg
├── README.md
├── scraper
│   ├── database.py
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       ├── photo.py
│       ├── photoset.py
│       └── __pycache__
├── scrapy.cfg
```
`logs`文件夹存放爬虫的运行日志  
`photos`文件夹存放爬虫下载的图片


## 主要实现



## 成果


## 存在的缺陷


## 要做的改进
- 提升爬取效率
- 提升入库速度
- 提升图片下载的成功率


## 结语
这车一般
