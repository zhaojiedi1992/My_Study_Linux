Openssl
================================================
ssl(secure socket layer)安全套接字协议，是一种应用层协议，主要用于传输数据加密，
而openssl是ssl协议的开源实现，是广泛使用的商业及ssl工具。

常见的加密算法和协议
-----------------------------------------------

对称加密
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
对称加密： 加密和加密使用同一个秘钥，依赖于算法和秘钥，但其安全性依赖于秘钥而非算法。

常见对称加密算法： 

- DES 
- 3DES 
- AES 
- Blowfish 
- Twofish 
- IDEA 
- RC6 
- CAST5 

对称加密的特点

#. 加密和解密使用同一秘钥
#. 将明文分割为固定大小的块，逐个进行加密
#. 秘钥过多
#. 密码分发复杂

非对称加密
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
非对称加密： 采用的是公钥加密方法，需要私钥来解密。公钥可以公开，私钥只能个人使用。 

特点： 

- 可以身份认证，私钥加密的，对应公钥才能解密
- 公钥加密只能私钥解密，私钥加密只能公钥解密。
- 秘钥长度较大

常要的非对称加密算法： 

- RSA 
- DSA 
- ELGamal

单向加密
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
只能加密，不能解密。

特点： 

- 定长输出
- 同样数据，每次结果都一样
- 不同数据，计算结果不同
- 雪崩效应，数据修改一点点，结果变换很大
- 不可逆


常见的单向加密算法

- MD5 
- SHA1
- SHA256
- SHA384
- SHA512
- CRC32

用处： 

- 数据完整性校验
- 系统账号密码校验

秘钥交换
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
秘钥交互（internet key exchange）： 双方通过交互秘钥来实现数据加密解密。

交互方法： 

- 公钥加密
- DH

一次加密通信过程
-----------------------------------------------

发送方： 

#. 使用单向加密算法提取生成数据的特征码
#. 使用自己的私钥加密特征码放到数据后面
#. 生成用于对称加密的临时秘钥
#. 用临时秘钥来加密数据和私钥加密后的特征码
#. 使用接受方的公钥加密临时秘钥，附加到对称加密后的数据后方

接受方： 

#. 使用自己的私钥解密临时秘钥，获取对称秘钥
#. 使用对称秘钥解密数据，得到数据和特征码的密文
#. 使用发送的公钥来解密特征码的密文，获取特征码
#. 使用对方同样的单向加密算法来计算数据的特征码和获取到的特征码进行比较

数字证书
-----------------------------------------------
ca是一个证书办法机构，这个机构负责证书的办法。

ca只是pki（public key infrastructure 公钥基础设施）的一个组成部分。pki包括： 

- 签证机构ca
- 注册机构ra
- 证书吊销列表crl
- 证书存放库

数字证书格式： 

- 版本号
- 序列号
- 签名算法标志
- 发行者的名称
- 有效期
- 证书主体名称
- 证书主体公钥信息
- 发行商的唯一标示
- 证书主体的唯一标示
- 扩展信息
- 签名（ca对证书的签名）

ssl
--------------------------------------------------------------------
ssl(secure sockets layers 安全套接层) 是为网络通信提供安全及数据完整性的一种安全协议。

tls(translater layer secure 传输层安全) 是ssl的继承版本，与sslzai 传输层对网络连接进行加密。

openssl
--------------------------------------------------------------------
openssl是ssl的一个开源项目，由三部分组成。

加密文件
    des,3des,aes,blowfish ,twofish,idea,CAST5
单向加密
    md5,sha1,
生成用户密码
    passwd
生成随机数
    rand

样例： 

.. code-block:: bash 

    # 加密文件和解密文件
    [root@centos-155 ~]# cat /root/test.sh
    date
    df -h
    [root@centos-155 ~]# openssl  enc -e -a -salt -in /root/test.sh  -out /root/test.sh.enc
    [root@centos-155 ~]# cat /root/test.sh.enc
    ZGF0ZQpkZiAtaAo=
    [root@centos-155 ~]# openssl  enc -d -a -salt -out /root/test.sh.dec  -in /root/test.sh.enc
    [root@centos-155 ~]# cat /root/test.sh.dec 
    date
    df -h

    # 单向加密
    [root@centos-155 ~]# openssl dgst  /root/test.sh 
    MD5(/root/test.sh)= 220f72b1a4e636373d4b9310569cf027

    # 生成密码
    [root@centos-155 ~]# openssl passwd -1 
    Password: 
    Verifying - Password: 
    $1$QfprG3kQ$WrY4N1mbw4IdQc0uFyvBF/

    # 生成随机数
    [root@centos-155 ~]# openssl rand 24  -base64  | head -c 8
    VnNpgcFj

    # 生成公钥和秘钥
    VnNpgcFj[root@centos-155 ~]# openssl genrsa -out test 1024 
    [root@centos-155 ~]# ll test
    -rw-r--r-- 1 root root 887 Feb 11 19:16 test
    [root@centos-155 ~]# openssl rsa -in test -pubout  -out test.pub
    [root@centos-155 ~]# cat test.pub 
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9agUiRyfROeBNy2ZPIduxwcwo
    mRssh2gMv7I7EIHA/GNKJiW8znjq/uuZDERD699+y9d1C8Q4sh761Za6ec0DU5eP
    QcTEuOByi4Dh34B6Ofco00d+30nku8AaXE+vBouE9oL95vJbYz0uCcVNXycZQL42
    qYmtfutw/Qnek44a1QIDAQAB
    -----END PUBLIC KEY-----

数字证书的获取
----------------------------------------------------------------

自建ca_

.. _自建ca: http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_011_ca.html

.. code-block:: bash  

    # 1 生成自己的私钥
    [root@centos-155 ~]# (umask 066; openssl genrsa -out /etc/pki/CA/private/cakey.pem 2048)

    # 2 给自己颁发证书
    [root@centos-155 ~]# openssl req -new -x509 -key /etc/pki/CA/private/cakey.pem -out /etc/pki/CA/cacert.pem -days 3650

    # 3 查看辅助文件
    [root@centos-155 ~]# cat /etc/pki/tls/openssl.cnf  |grep dir
    dir		= /etc/pki/CA		# Where everything is kept
    certs		= $dir/certs		# Where the issued certs are kept
    crl_dir		= $dir/crl		# Where the issued crl are kept
    database	= $dir/index.txt	# database index file.
    new_certs_dir	= $dir/newcerts		# default place for new certs.
    certificate	= $dir/cacert.pem 	# The CA certificate
    serial		= $dir/serial 		# The current serial number
    crlnumber	= $dir/crlnumber	# the current crl number
    crl		= $dir/crl.pem 		# The current CRL
    private_key	= $dir/private/cakey.pem# The private key
    RANDFILE	= $dir/private/.rand	# private random number file
    dir		= ./demoCA		# TSA root directory
    serial		= $dir/tsaserial	# The current serial number (mandatory)
    signer_cert	= $dir/tsacert.pem 	# The TSA signing certificate
    certs		= $dir/cacert.pem	# Certificate chain to include in reply
    signer_key	= $dir/private/tsakey.pem # The TSA private key (optional)

    # 4 创建辅助文件
    [root@centos-155 ~]# touch /etc/pki/CA/index.txt 
    [root@centos-155 ~]# echo "01" >> /etc/pki/CA/serial


    # 5 节点生成自己的证书请求
    [root@centos-155 ~]# (umask 066; openssl genrsa -out test 1024)
    [root@centos-155 ~]# openssl req -new -days 365 -key test -out test.csr

    # 6 ca颁发证书
    [root@centos-155 ~]# openssl ca -in test.csr -out /etc/pki/CA/certs/test.pem -days 300


吊销证书

.. code-block:: bash 

    # 查看吊销证书编号
    [root@centos-155 ~]# openssl x509 -in /etc/pki/CA/cacert.pem  -noout  -serial  -subject 
    serial=986C2523B50ABD8C
    subject= /C=cn/ST=henan/L=nanyang/O=linuxpanda/OU=opt/CN=ca.linuxpanda.tech

    # 吊销证书
    [root@centos-155 ~]# openssl ca -revoke /etc/pki/CA/cacert.pem 
    # 生成吊销证书编号
    [root@centos-155 ~]# echo 01 >> /etc/pki/CA/crlnumber
    # 更新证书吊销列表






