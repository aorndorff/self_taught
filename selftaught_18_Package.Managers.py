# Package Manager - Installs and manages other programs
# Web Framerwork - helps build websites
# pip - package manager 

#Package - sofrware packaged for distribution
# includes files that make up actual program and metadata

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello Mother Fuckers!"
app.run(port='8000')
