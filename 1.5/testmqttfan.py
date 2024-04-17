import web
from hardware.fan import Fan

# 初始化 Fan 类
fan = Fan(mqtt_server='192.168.3.6')

urls = (
    '/', 'Index',
    '/open', 'OpenFan',
    '/close', 'CloseFan',
)

app = web.application(urls, globals())

class Index:
    def GET(self):
        return """
            <html>
                <head>
                    <title>Fan Controller</title>
                </head>
                <body>
                    <h1>Fan Controller</h1>
                    <button onclick="location.href='/open'">Turn On</button>
                    <button onclick="location.href='/close'">Turn Off</button>
                </body>
            </html>
        """

class OpenFan:
    def GET(self):
        fan.open()
        return "Fan turned on."

class CloseFan:
    def GET(self):
        fan.close()
        return "Fan turned off."

if __name__ == "__main__":
    app.run()
