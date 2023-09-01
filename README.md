# notifer

这是一个基于Django的，用asyncio调度的，用sqlite3做持久化的通知管理器。

可以配置用email或者用notify软件来发送通知。目前没有实现动态加载json配置，
需要手动去改代码里的常量。

由于asyncio实现了一个时间堆，而且python里也没见好用的时间轮，所以干脆直接用
asyncio协程编写。好像还依托asyncio实现了超时功能？具体的我也忘了。

Django提供了一个管理Message的页面。可以撤销你的消息，可以查看消息目前的状态。
这就实现了系统的可观测性。

消息通过Django的Controller，通过核心组件的一个addMessage接口加入进来。
然后落盘到sqlite。

之后，每次启动核心的时候，都自动加载sqlite里的Message，把所有信息调度进时间轮里。

至于为何不用crontab，因为crontab粒度为1min，太拉了。轮询又太费资源。不如
这个asyncio底层用的epoll省电。

发邮件的时候会开新线程，涉及到asyncio的一些集成。需要python3.11版本支持。
3.8版本是跑不起来的，有bug。

