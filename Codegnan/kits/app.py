import flask as fl
from flask import Flask 
app = Flask(__name__)
@app.route('/')
def index():
    a = "<a href='./nitin'> 1st page </a> <br> <a href='./sravs'> 2nd page </a> <br> <a href='./khaleel'> 3rd page </a> <br>  <a href='./anil'> 4th page </a>"
    t = "I am in my first page and my other pages are <br>"
    return t+a

# routes are known as view functions
# routes and function can be named different but it is not advisable

@app.route('/nitin')
def nitin():
    return "I am Venkata Rama Nitin Pathuri a final year Data Science student in KKR & KSR Institute of Technology and Sciences <br><a href='./'>Home page</a>"

@app.route('/sravs')
def sravs():
    return "I am Sravan and my classmates calls me Sravs <br><a href='./'>Home page</a>"

@app.route('/khaleel')
def khaleel():
    return "I am Khaleel and my classmates calls me K <br><a href='./'>Home page</a>"

@app.route('/anil')
def anil():
    return "I am Anil and my classmates calls me Anila <br><a href='./'>Home page</a>"

@app.errorhandler(404)
def page_not_found(error):
    return fl.  render_template('/404.html'), 404

@app.errorhandler(500)
def page_notfound(error):
    return fl.render_template('/404.html'), 500

app.run(use_reloader=True,debug=True)