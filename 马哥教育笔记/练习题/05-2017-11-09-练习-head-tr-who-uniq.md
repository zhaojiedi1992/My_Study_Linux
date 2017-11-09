## 练习1
1. 将/etc/passwd 文件的前5行内容转化为大写后保存到/tmp/passwd.out文件
1. 将登陆到当前系统的用户信息的后3行信息转化为大写保存到/tmp/who.out文件中

```bash
[root@centos6 dirtest]# head -n 5 /etc/passwd |tr 'a-z' 'A-Z' > /tmp/passwd.out

```

```bash
[root@centos6 dirtest]# who |tail -n 3  | tr 'a-z' 'A-Z' > /tmp/who.out

```
## 练习2
1. 取出/etc/passwd 文件中的第6行至第10行，并将这些信息按第3个字段数值进行排序，最后显示进显示第一个字段，
```bash
[root@centos6 ~]# head -n 10 /etc/passwd | tail -n 5 | sort -t ":" -k 3 | cut -d ":" -f 1
```