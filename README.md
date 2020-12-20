# cdn-detection
检测思路：向不同的dns服务器发送解析请求 查看解析的ip是否相同，并根据获取的cname记录 利用规则字典判断出使用何种cdn
字典用的https://github.com/shiyihua/CDN 这里只采用cname判断 感觉准确率可以了



用法：
代码比较简单 大佬们一看就会了

TODO:
计划爬取ALEXA的域名 收集整理未识别的cdn 人工检测后，添加到字典中

