
07-22 16:37  
// 折腾了半个月啊, 修复靠自愈,呵呵,终结一下
// traefik 算基本跑通,其他需要的时候,再测吧
// ceph 算跑通了基础

07-05 16:04  
// 1.6.2 差不多都通了, 安装个 prometheus然后铲平吧


07-01 12:03  
// 测试一下EFK, 完成后把内存改回来
// 依然,连不上es,缺乏对组件间的调试技能, 进入容器, 查看端口, 查看连接 



06-26 10:13  
// 现在看来,起是起来了,连接有点问题
// 如何排查?  es red



06-25 01:15  
// dns 回头整吧,需要清理部署,服务,更新等多个操作
// 全跑完后整理排查,归纳总结,整理

// EFK , es, fluentd, kibana

// Docker-Registry 浏览

// harbor 成功

// dns ok

// grafana 如何基础设置 ok
// influxdb 也不会用,需要基础
// efk同上,需要补充

// 目前问题, 全部署成功,但不会使用, 图表 无法查看,
// 还有普罗米修斯

06-24 11:23  
// 归纳整理之前的文件关系

// 配置另一个kubelet  成功

// dns 失败, 服务起来了,pods没起来,奇怪?



06-22 09:47 
// kubectl

// flannet

// master

// node

// 思维导图太臃肿了, 后面笔记还是要放目录中,导图只放关键词


06-21 16:09  
// 项目重起, 备份之前下载的文件,先搭起来  
// v1.6.2 已不更新, 仅回忆  

// 以ip段为区分, 环境变了,克隆重启一个新项目


// 配置基础  
// 把长久变量写在文件里,发给每个机器是个好习惯  


// 安装 CFSSL, 打印模板  
// 配置ca  

// 配置  
ca-config.json  
ca-csr.json  


// 把生成文件复制到各台机器对应目录


// etcd  
// 配置变量  
// 创建证书和服务  
// 启动  
// 验证  

