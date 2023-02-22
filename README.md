# working-CIF-service
这是一个简易的发送邮件的程序，其内核是python

## 配置文件使用方式
所有的配置文件都将会集成在init_conf中，如果你第一次使用程序。init_conf将会直接转换conf.

如果你已经使用过该程序。请注意未来更新的版本。作者并未使用类似自动更新的手段来更新conf中的一部分内容。请按照每个release 的操作来更新你的conf的配置文件。


## 配置文件使用方式

<details>
  <summary>email配置文件</summary>
    | 字段名 | 介绍|
    |-----|-----|
    | name | 这是发送邮件时显示在邮件头上的昵称|
    |smtp_server|这是发送邮件的服务器|
    |smtp_port|这是发送邮件服务器的端口，一般不需要修改国内基本都是465|
    |smtp_user|这是你的发送账号|
    |smtp_password| 这是你的发送账号的密码|
</details>