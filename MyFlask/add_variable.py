from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')  # Here we will pass name as argument  for a function and if we pass  with name then
# this name will be passsed to the function as argument.There is no type defined for the name of the function .By
# default it is string
def hello_name(name):
    return f"hello {name}"


@app.route('/flask')
# this will give error if we pass /flask/ and only work for /flask
def hello_flask():
    return "hello Flask"


@app.route('/python/')
# this will not give error if we pass /python/ and also work for /flask
def hello_python():
    return "hello python"


@app.route('/blog/<int:post_id>')
#the routing method is for pass a variable of type int in URL along with /blog/and also pass this value to teh function
def show_blog(post_id):
    return f"Blog no is : {post_id}"

@app.route('/blog/<float:rev_no>')
#the routing method is for pass a variable of type float  in URL along with /blog/ and also pass this value to teh function
def show_revision(rev_no):
    return f"Rev no is {rev_no}"

if __name__ == '__main__':
    app.run(debug=True)
