#作业内容 ——————宿舍信息管理系统

参与者
#1 学生 浏览自己的信息
#2 管理员 记录学生的信息，更新学生信息，删除学生信息，浏览所有学生的信息
#3 教师 更新学生信息，查看学生信息



##系统需求##
#1 上传宿舍成员信息 包含宿舍号，学号，姓名，专业
#2 修改宿舍成员信息
#3 删除宿舍成员信息
#4 查询宿舍成员信息并且输出

#类图#
#类1：student info
#类2：administrator
#类3：teacher
#类4：student
#类5：logon

##功能
@1 记录信息 student info
@2 删除信息 student info
@3 更新信息 student info
@4 查看信息 student info
@5 加载信息 student info
@6 保存信息 student info
@7 登录 logonui

##关联
@@1 student 查看info
@@2 teacher 查看，更新info
@@3 administrator 查看更新增加删除info



##规范化的关系模型

#教师 ！教师编号！ 教师姓名
#管理员 ！管理员ID！ 管理员密码
#学生 ！学号！ 姓名 专业 宿舍号 
#管理 !编号！ 密码 人员类别