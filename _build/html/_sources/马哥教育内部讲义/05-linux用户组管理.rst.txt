05 linux用户和组管理
==========================================================

用户分类

- 系统用户:1-499(centos6),1-999(centos7)
- 登陆用户： 500+（centos6）,1000+(centos7)

5.1 主要配置文件分析
---------------------------------------------------

5.1.1 /etc/passwd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

name:password:uid:gid:geocos:homedir:shell

.. code-block:: bash

    [root@centos6 ~]# head -1 /etc/passwd
    root:x:0:0:root:/root:/bin/bash

5.1.2 /etc/group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

groupname:password:gid:userlist

.. code-block:: bash

    [root@centos6 ~]# head -1 /etc/group
    root:x:0:

5.1.2 /etc/shadow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

name:password: date of last password change : minimum password age : maximum password age : password warning period: password warning period: password inactivity period

.. code-block:: bash

    [root@centos6 ~]# tail -n 1 /etc/shadow
    zhaojiedi:$6$rZ5h80aV/7Sci.YB$D25I/MTmTHyo.2XhUNSiJab1BU/qf1vgpdZ3c0JBgzSDMG8tKzyUsPk..xJ9a31a17kGctcgm0OBIUTQGf7Uv0:17477:0:99999:7:::

- 用户名
- 加密密码
- 上次修改的密码
- 最小使用时间
- 最大使用时间
- 密码警告时间
- 密码禁用期
- 账户过期日期
- 保留字段

5.2 用户管理命令
---------------------------------------------------------------------

5.2.1 useradd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-u              指定用户id
-g              基本组
-G              附加组
-c              注释信息
-s              shell类型
-d              用户的家目录

5.2.2 groupadd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-g              组id
-r              系统用户

id

.. code-block:: bash

    [root@centos6 ~]# id
    uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    [root@centos6 ~]# id -u 
    0
    [root@centos6 ~]# id -g
    0
    [root@centos6 ~]# id -G
    0
    [root@centos6 ~]# id -un
    root

5.2.3 su 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- su username: 非登录切换，不会读取目标用户的配置文件
- su -username:登陆切换，会读取目标用户配置文件，完全切换

5.2.4 usermod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-g:             
-G:                 
-u:
-s:
-c:
-d:
-l
-L
-U 
-e              指定过期日期
-f              指定非活动期限

5.2.5 passwd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-l          锁定用户
-u          解锁
-n          最短期限
-x          最大期限
-w          警告期限
-i          非活动期限
--stdin     接受终端输入

5.2.6 userdel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-r          删除用户家目录

5.2.7 groupdel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5.2.8 groupmod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-n              新名字
-g              新的id

5.2.9 gpasswd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-a              添加到指定的组
-d              从指定组删除
-A              设置用户列表

5.2.10 newgrp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

用户临时切换基本组

5.2.11 chage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-d              修改用户最近一次修改时间
-I              修改用户的非活动期限
-E              过期日期

5.3 sudo
-------------------------------------------------------

-l              查看用户可以执行的sudo
-k              清楚记一下的令牌
-u              以指定用户运行命令

配置文件是/etc/sudoers

账号 登陆这来源主机名 （可切换的身份） 命令

注意事项

- ALL大写
- 命令使用全路径
- 组使用%
- 别名 User_Alias User1 = magedu,centos,test
