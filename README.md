# notifer

## 概述和注意事项

这是一个基于Django的，用asyncio调度的，用sqlite3做持久化的通知管理器。

可以配置用email或者用notify软件来发送通知。目前没有实现动态加载json配置，
需要手动去改代码里的常量。

Django提供了一个管理Message的页面。可以撤销你的消息，可以查看消息目前的状态。
这就实现了系统的可观测性。

邮件的时候会开新线程，涉及到asyncio的一些集成。需要python3.11版本支持。
3.8版本是跑不起来的，有bug。

## 设计思路

**为何用asyncio实现**

由于asyncio实现了一个时间堆，而且python里也没见好用的时间轮，所以干脆直接用
asyncio协程编写。好像还依托asyncio实现了超时功能？具体的我也忘了。

**为何不用crontab或者Django那个消息队列集成**

至于为何不用crontab，因为crontab粒度为1min，太拉了。轮询又太费资源。不如
这个asyncio底层用的epoll省电。

Django那个消息队列集成很重，要rabbitmq，而且说实话不好用，消息撤销等逻辑不好。
不如时间轮+epoll来得直观。

**核心数据怎么流动的？**

发消息通过Django的Controller，通过核心组件的一个addMessage接口加入进来。
然后落盘到sqlite。

之后，每次启动核心的时候，都自动加载sqlite里的Message，把所有信息调度进时间轮里。

## 文件创建日期历史

之前没有用git管理，一些文件提交记录可以以这些时间来表示。

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----           8/17/2023  1:31 PM                notification_app
d----           8/17/2023 10:11 AM                notification_project
-a---           8/15/2023  6:30 PM         253952 db.sqlite3
-a---           8/13/2023 10:16 AM            698 manage.py
-a---            9/2/2023  1:06 AM           1148 README.md


    Directory: C:\Users\qq769\notifer\notification_project\notification_app

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----           8/17/2023 10:09 AM                __pycache__
d----           8/15/2023 10:09 AM                migrations
d----           8/13/2023 10:37 AM                templates
-a---           8/13/2023 10:16 AM              0 __init__.py
-a---           8/13/2023 10:41 AM            166 admin.py
-a---           8/15/2023 12:09 AM            171 apps.py
-a---           8/14/2023  2:26 PM            593 forms.py
-a---           8/15/2023  4:30 PM           3149 mailqq.py
-a---           8/15/2023 10:07 AM            731 models.py
-a---           8/13/2023 12:56 PM            561 sendmail.py
-a---           8/17/2023 12:52 AM           4945 startup.py
-a---           8/14/2023  8:14 AM           1051 tasks.py
-a---           8/13/2023 10:16 AM             63 tests.py
-a---           8/15/2023  1:07 PM            345 urls.py
-a---           8/17/2023 10:08 AM           1776 views.py
```

## 待办

- 只有startup.py和mailqq.py是有用的，tasks.py和sendmail.py等老旧代码得删掉。
- ctrl+c优雅退出不知道为啥，capture不了，想办法改进
