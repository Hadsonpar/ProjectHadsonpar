from flask import Flask, render_template, g # import to initialize, g (global variables)

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object

@app.before_request
def set_global_variables(): # global variables for the website
  g.site_title  = "Hadsonpar"

@app.route('/') # initial (home page) route
def home(): # home page function    
    return render_template('home.html', page='Home')

@app.route('/about') # about page route
def about():# about page function
    return render_template('about.html', page='About')

@app.route('/projects') # projects page route
def projects(): # projects page function
    return render_template('projects.html', page='Projects')

@app.route('/services') # services page route
def services(): # services page function
    return render_template('services.html', page='Services')

@app.route('/contact') # contact page route
def contact(): # contact page function
    return render_template('contact.html', page='Contact')

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', page='404'), 404

if __name__ == '__main__':
    app.run(debug=True) # project debug