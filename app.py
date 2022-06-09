from flask import Flask
from flask import render_template
app = Flask('server app')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
   app.run()

{% block styles %}
{{super()}}
<link rel="stylesheet"
      href="{{url_for('.static', filename='mystyle.css')}}">
{% endblock %}