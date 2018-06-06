# -*- coding:utf-8 -*-
import string
import xml.dom.minidom
import urllib2
import base64
import time
import socket
import xxx_config as config


class MQStatus:
    def __init__(self):
        self.client = config.Config()
        self.activemq_host, self.activemq_port, self.activemq_user, self.activemq_password = self.client.activemq_config()
        self.endpoint = socket.gethostname()
        self.step = 60
        self.ts = int(time.time())
        self.tag = 'test'
        self.keys = ('size', 'consumerCount', 'enqueueCount', 'dequeueCount')

    def activemq_info(self):
        request = urllib2.Request("http://{0}:{1}/admin/xml/queues.jsp".format(self.activemq_host, self.activemq_port))
        base64string = base64.b64encode('{0}:{1}'.format(self.activemq_user, self.activemq_password))
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        xmlStr = string.replace(result.read(), '\t', '')
        xmlStr = string.replace(xmlStr, '\n', '')
        data = xml.dom.minidom.parseString(xmlStr)
        queues = data.getElementsByTagName("queues")[0]

        p = []

        for queue in queues.childNodes:
            for key in self.keys:
                q = {}
                q["endpoint"] = self.endpoint
                q["timestamp"] = self.ts
                q["step"] = self.step
                q["counterType"] = "GAUGE"
                q["metric"] = "activemq.{0}".format(key)
                q["tags"] = "queuename={0},{1}".format(queue.getAttribute('name'), self.tag)
                q["value"] = int(queue.getElementsByTagName("stats")[0].getAttribute(key))
                print(q)
                p.append(q)
        return p


if __name__ == "__main__":
    mqobj = MQStatus()
    mqobj.activemq_info()
