#######################################################
################  Flask Application  #################
#####################################################

from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template("home.html")


@app.route("/temp")
def temp():
    print("Server received request for 'Temperature' page...")
    return render_template("temp.html")


@app.route("/humid")
def humid():
    print("Server received request for 'Humidity' page...")
    return render_template("humid.html")


@app.route("/wind")
def wind():
    print("Server received request for 'Wind Speed' page...")
    return render_template("wind.html")


@app.route("/cloud")
def cloud():
    print("Server received request for 'Cloud Coverage' page...")
    return render_template("cloud.html")


@app.route("/comps")
def comps():
    print("Server received request for 'Comparisons' page...")
    return render_template("comps.html")


@app.route("/data")
def data():
    print("Server received request for 'Data' page...")
    return render_template("data.html")



if __name__ == "__main__":
    app.run(debug=True)




# Considerations
# You may use the weather data or choose another dataset. Alternatively, you may use the included cities dataset 
# and pull the images from the assets folder.
# You must use bootstrap. This includes using the bootstrap navbar component for the header on every page, 
# the bootstrap table component for the data page, and the bootstrap grid for responsiveness on the comparison page.
# You must deploy your website to GitHub pages, with the website working on a live, publicly accessible URL as a result.
# Be sure to use a CSS media query for the navigation menu.
# Be sure your website works at all window widths/sizes.
# Feel free to take some liberty in the visual aspects, but keep the core functionality the same.



# Bonuses
# Use a different dataset! The requirements above still hold, but make it your own.
# Use a bootstrap theme to customize your website. You may use a tool like Bootswatch. 
# Make it look snazzy, give it some attitude. If using this, be sure you also meet all of the requirements listed above.
# Add extra visualizations! The more comparisons the better, right?
# Use meaningful glyphicons next to links in the header.
# Have visualization navigation on every visualizations page with an active state. See the screenshots below.