import web


temp = "30°C"
humi = "30%"

urls = (
  '/', 'index'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)

class index:
    def GET(self):
        return render.index(temp, humi)

if __name__ == '__main__':
    app.run()
