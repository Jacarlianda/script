import ConfigParser
import os


class Config:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(self.BASE_DIR, 'xxx-monitor.conf'))

    def redis_config(self):
        redis_host = self.config.get('redis', "redis_host")
        redis_port = self.config.get("redis", "redis_port")
        redis_password = self.config.get('redis', "redis_password")
        return redis_host, redis_port, redis_password

    def mysql_config(self):
        mysql_host = self.config.get('mysql', "host")
        mysql_port = self.config.get("mysql", "port")
        mysql_user = self.config.get('mysql', "user")
        mysql_password = self.config.get('mysql', "password")
        mysql_database = self.config.get('mysql', "database")
        return mysql_host, mysql_port, mysql_user, mysql_password, mysql_database

    def mail_config(self):
        mail_sender = self.config.get('mail', "mail_sender")
        mail_password = self.config.get("mail", "mail_password")
        mail_receiver = self.config.get('mail', "mail_receiver")
        stmp_server = self.config.get('mail', "stmp_server")
        stmp_server_port = self.config.get('mail', "redis_password")
        return mail_sender, mail_password, mail_receiver, stmp_server, stmp_server_port

    def activemq_config(self):
        activemq_host = self.config.get('activemq', "activemq_host")
        activemq_port = self.config.get('activemq', "activemq_port")
        activemq_user = self.config.get('activemq', "activemq_user")
        activemq_password = self.config.get('activemq', "activemq_password")
        return activemq_host, activemq_port, activemq_user, activemq_password
