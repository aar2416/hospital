#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
<html>
<head>
<script type="text/javascript">
//auto expand textarea
function adjust_textarea(h) {
    h.style.height = "20px";
    h.style.height = (h.scrollHeight)+"px";
}
</script>
<style>
.form-style-7{
    max-width:400px;
    margin:50px auto;
    background:#fff;
    border-radius:2px;
    padding:20px;
    font-family: Georgia, "Times New Roman", Times, serif;
}
.form-style-7 h1{
    display: block;
    text-align: center;
    padding: 0;
    margin: 0px 0px 20px 0px;
    color: #5C5C5C;
    font-size:x-large;
}
.form-style-7 ul{
    list-style:none;
    padding:0;
    margin:0;   
}
.form-style-7 li{
    display: block;
    padding: 9px;
    border:1px solid #DDDDDD;
    margin-bottom: 30px;
    border-radius: 3px;
}
.form-style-7 li:last-child{
    border:none;
    margin-bottom: 0px;
    text-align: center;
}
.form-style-7 li > label{
    display: block;
    float: left;
    margin-top: -19px;
    background: #FFFFFF;
    height: 14px;
    padding: 2px 5px 2px 5px;
    color: #B9B9B9;
    font-size: 14px;
    overflow: hidden;
    font-family: Arial, Helvetica, sans-serif;
}
.form-style-7 input[type="text"],
.form-style-7 input[type="date"],
.form-style-7 input[type="datetime"],
.form-style-7 input[type="email"],
.form-style-7 input[type="number"],
.form-style-7 input[type="search"],
.form-style-7 input[type="time"],
.form-style-7 input[type="url"],
.form-style-7 input[type="password"],
.form-style-7 textarea,
.form-style-7 select 
{
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    width: 100%;
    display: block;
    outline: none;
    border: none;
    height: 25px;
    line-height: 25px;
    font-size: 16px;
    padding: 0;
    font-family: Georgia, "Times New Roman", Times, serif;
}
.form-style-7 input[type="text"]:focus,
.form-style-7 input[type="date"]:focus,
.form-style-7 input[type="datetime"]:focus,
.form-style-7 input[type="email"]:focus,
.form-style-7 input[type="number"]:focus,
.form-style-7 input[type="search"]:focus,
.form-style-7 input[type="time"]:focus,
.form-style-7 input[type="url"]:focus,
.form-style-7 input[type="password"]:focus,
.form-style-7 textarea:focus,
.form-style-7 select:focus 
{
}
.form-style-7 li > span{
    background: #F3F3F3;
    display: block;
    padding: 3px;
    margin: 0 -9px -9px -9px;
    text-align: center;
    color: #C0C0C0;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 11px;
}
.form-style-7 textarea{
    resize:none;
}
.form-style-7 input[type="submit"],
.form-style-7 input[type="button"]{
    background: #2471FF;
    border: none;
    padding: 10px 20px 10px 20px;
    border-bottom: 3px solid #5994FF;
    border-radius: 3px;
    color: #D2E2FF;
}
.form-style-7 input[type="submit"]:hover,
.form-style-7 input[type="button"]:hover{
    background: #6B9FFF;
    color:#fff;
}
</style>
</head>
<form class="form-style-7" action="/confirm" method="post">
<ul>
<li>
    <label for="name">Patient Name</label>
    <input type="text" name="name" maxlength="100">
    <span>Enter your full name here</span>
</li>
<li>
    <label for="email">Patient Email</label>
    <input type="email" name="email" maxlength="100">
    <span>Enter a valid email address</span>
</li>
<li>
    <label for="url">Address</label>
    <textarea name="url" cols="17" rows="7"></textarea>
	<span>Enter your address</span>
</li>
<li>
    <label for="bio">Disease</label>
    <input type="text" name="bio" maxlength="1000">
    <span>Enter your disease</span>
</li>
<li>
    <label for="des">Description</label>
	<textarea name="des" cols="17" rows="7"></textarea>
	<span>Enter your description</span>
<li>
    <input type="submit" value="Send This" >
</li>
</ul>
</form>
</html>
 """  
   
   
class Hospital(ndb.Model):
    name = ndb.StringProperty(indexed=True)
     email = ndb.StringProperty(indexed=True)
     url = ndb.StringProperty(indexed=True)
     bio= ndb.TextProperty(indexed=True)
     des = ndb.IntegerProperty(indexed=True)	 
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     name = self.request.get('name')
     email = self.request.get('email')
     url = self.request.get('url')
     bio = self.request.get('bio')
     des = self.request.get('des')
     hospital = Hospital()
     hospital.name=name
     hospital.email=email
     hospital.url=url
     hospital.bio=bio
     hospital.des=des
     hospital.put()
     self.redirect('/')
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler)], 
 debug=True)
