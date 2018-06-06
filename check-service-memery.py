import commands

list = []
list.append("tomcat")

for service in list:
    # top 百分比
    men_percent = float(commands.getoutput(
        "top -b -n 1|grep `ps -ef|grep %s|grep -v grep|awk '{print $2}'`|awk '{print $10}'" % service))
    men_total = float(commands.getoutput("free -m|grep 'Mem:'|awk '{print $2}'"))
    service_men = int(men_total * men_percent / 100)
    print(service + " 占用 " + str(service_men) + " MB")
