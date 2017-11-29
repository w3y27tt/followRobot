# V0.0.1 测试版
# JSON参数（此版本处理的）：
# {
#   target_url: string,    fetch的网址7
#   priority: int          优先级
# }

import time
from fetch import get

while True:
    get('http://www.freebuf.com/')
    time.sleep(600)
