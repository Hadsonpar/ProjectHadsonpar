from flask import Flask, render_template # import to initialize                    

app = Flask(__name__) # initial Object

@app.route('/') # initial (home page) route
def home():# home page function
    return render_template('home.html')

@app.route('/about') # about page route
def about():# about page function
    return render_template('about.html')

@app.route('/projects') # projects page route
def projects(): # projects page function
    return render_template('projects.html')

@app.route('/contact') # contact page route
def contact(): # contact page function
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) # project debug