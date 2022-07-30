import bs4
with open('static/index.html') as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")

color = '#F1A94E' #Blue 44B3C2 and Yellow F1A94E

soup.find('div')['style'] = 'background:' + color
# print(soup)


from flask import Flask, render_template_string

app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template_string(str(soup))
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')