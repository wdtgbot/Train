# time模块

|函数|描述|IDLE代码|结果|
|:---:|:---:|:---:|:---:|
|time()|获取当前时间戳|`time.time()`|`1638511150.6327093`|
|ctime()|获取当前时间并以易读方式表示，返回字符串|`time.ctime()`|`Fri Dec  3 14:00:44 2021`|
|gmtime()|获取当前时间，表示为计算机可处理的时间格式|`time.gmtime()`|`time.struct_time(tm_year=2021, tm_mon=12, tm_mday=3, tm_hour=6, tm_min=1, tm_sec=58, tm_wday=4, tm_yday=337, tm_isdst=0)`|

# 时间格式化

|函数|描述|IDLE代码|结果|
|:---:|:---:|:---:|:---:|
|strftime(tpl, ts)|tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量|`time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())`|`2021-12-03 06:05:11`|

# 时间反格式化

|函数|描述|IDLE代码|结果|
|:---:|:---:|:---:|:---:|
|strptime(str, tpl)|str时字符串形式的时间值，tpl时格式化模板字符串，用来定义输入效果|`time.strptime("2021-12-03 06:05:11", "%Y-%m-%d %H:%M:%S")`|`time.struct_time(tm_year=2021, tm_mon=12, tm_mday=3, tm_hour=6, tm_min=5, tm_sec=11, tm_wday=4, tm_yday=337, tm_isdst=-1)`|

# 时间格式化字符串

|格式化字符串|日期/时间说明|值范围|实例|
|:---:|:---:|:---:|:---:|
|%Y|年份|0000~9999|2021|
|%m|月份|01~12|12|
|%B|月份名称|January~December|December|
|%b|月份名称缩写|Jan~Dec|Dec|
|%d|日期|01~31|3|
|%A|星期|Monday~Sunday|Friday|
|%a|星期缩写|Mon~Sun|Fri|
|%H|24时制小时|00~23|14|
|%I|12时制小时|00~12|2|
|%p|上午/下午|AM,PM|PM|
|%M|分钟|00~59|11|
|%S|秒|00~59|23|

# 程序计时

|函数|描述|
|:---:|:---:|
|perf_counter()|返回一个CPU级别的精确时间计数值，单位为秒|
|sleep(s)|s是拟休眠时间，单位是秒，可以是浮点数|

```python
import time
start = time.perf_counter()
time.sleep(5)
end = time.perf_counter()
print(end - start)
```