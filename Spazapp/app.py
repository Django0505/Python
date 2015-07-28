from flask.ext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'spot'
app.config['MYSQL_DATABASE_DB'] = 'spaza'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()

@app.route("/")
def main():
	cur = conn.cursor()
	cur.execute('SELECT product_id,product_name from products')
	entries = [dict(product_id=row[0],product_name = row[1]) for row in cur.fetchall()]
	return render_template('index.html',entries = entries)

@app.route('/products')
def products():
	return render_template('products.html')



if __name__ == '__main__':

	app.run(debug=True,
	host="172.18.0.76 ",
    port=int("3000"))
