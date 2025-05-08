import csv


from typing import List, Dict, Union

def read_file_windows(filename:str)->List[List[str]]:
	"""
		function to read a .csv file.
		input:
			filename - name of the file
		output:
			data contained in .csv file
	"""
	data = []
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			data.append(row)
		data = data[1:]
		data = [x for x in data if x != []]
	return data

	
def write_file_html(filename:str, x:str)->None:
	"""
		function to write a .txt/.html file.
		input:
			filename - name of the file (to write)
			x - html string (to create file)
		output:
			None
	"""
	with open(filename, 'w') as f:
		f.write(x)
	return None
	

def create_table(x:List[List[str]])->str:
	"""
		function to create html table (from data).
		input:
			x - data to fill table
		output:
			content html
	"""
	return "".join(["<tr>%s</tr>" % ("".join(["<td>%s</td>" % (i) for i in j])) for j in x])
	
	
	
def generate_html(img:str, x:List[List[str]], y:List[List[str]])->str:
	"""
		function to generate html content.
		input:
			img - path of the image to include in html content
			x - data of the first table
			y - data of the second table
		output:
			html content (str)
	"""
	contentUsr =  create_table(x)
	contentRights = create_table(y)
	
	
	html ="""<!DOCTYPE html>
		<html>
		<head>
		<style>
		* {
		  box-sizing: border-box;
		}

		.row {
		  margin-left:-5px;
		  margin-right:-5px;
		}
		  
		.column {
		  float: left;
		  width: 50%;
		  padding: 5px;
		  
		}

		/* Clearfix (clear floats) */
		.row::after {
		  content: "";
		  clear: both;
		  display: table;
		}

		table {
		  border-collapse: collapse;
		  border-spacing: 0;
		  width: 100%;
		  border: 1px solid #ddd;
		}

		th, td {
		  text-align: left;
		  padding: 16px;
		}

		tr:nth-child(even) {
		  background-color: #f2f2f2;
		}
		</style>
		</head>
		<body>

		<h2>LDAP</h2>
		
		<div class='fill-screen'> 
                                <img class='make-it-fit' src= "%%img%%" alt="graph"> 
                </div>
                
                <p>Tables of users and rights by groups:</p>
		
		<div class="row">
		  <div class="column">
		    <table>
		      <tr>
			<th>Group</th>
			<th>User</th>
			<th> </th>
		      </tr>
		      
		      
		      %%contentUsr%%
		    </table>
		    
		    
		  </div>
		  <div class="column">
		    <table>
		      <tr>
			<th>Group</th>
			<th>RIghts</th>
			<th> </th>
		      </tr>
		      
		      %%contentRights%%
		      
		    </table>
		  </div>
		</div>

		</body>
		</html>"""
		
	html = """<!DOCTYPE html>
			<html>
			<head>
			<style>
			
			h1 {
			  background: black;
			  display: block;
			  padding: 65px;
			  text-decoration: none;
			  letter-spacing: 0.5px;
			  color: white;
			}
			* {
			  box-sizing: border-box;
			}
			.row {
			  margin-left:-5px;
			  margin-right:-5px;
			} 
			.column {
			  float: left;
			  width: 50%;
			  padding: 5px;
			}
			/* Clearfix (clear floats) */
			.row::after {
			  content: "";
			  clear: both;
			  display: table;
			}
			table {
			  border-collapse: collapse;
			  border-spacing: 0;
			  width: 100%;
			  border: 1px solid #ddd;
			}

			th, td {
			  text-align: left;
			  padding: 16px;
			}
			tr:nth-child(even) {
			  background-color: #f2f2f2;
			}

			.fixed_header {
				width: 450px;
				table-layout: fixed;
				border-collapse: collapse;
			 }
			 .fixed_header tbody {
				display: block;
				width: 100%;
				overflow: auto;
				height: 200px;
			  }
			  .fixed_header thead tr {
				display: block;
			   }
			  .fixed_header thead {
				background: black;
				color: #fff;
			   }
			   .fixed_header th,
			   .fixed_header td {
				padding: 5px;
				text-align: left;
				width: 450px;
			}
			
			div.image-container {
			  overflow-y: scroll;
			  max-height: 400px;
			}
		
			</style>
			</head>
			<body>
			<!--<h2 style="text-align:center">LDAP</h2>-->
			
			
			<!--<p>Table of users and rights by groups:</p>-->
			
        			<h1 a style="text-align:center">LDAP</h1 a>
    				
			<div class="row">

			  <div class="column">
			    <table class="fixed_header" style="margin-left:auto;margin-right:auto;">
			      
			      
			      <thead>
				<tr>
				  <th>Group</th>
				  <th>User</th>
				</tr>
			      </thead>
			      
			      <tbody>
				%%contentUsr%%
			      </tbody>
			      
			    </table>
			  </div>
			  
			  <div class="column">
			 <table class="fixed_header" style="margin-right:auto;margin-right:auto;">
			      
			      
			      <thead>
				<tr>
				  <th>Group</th>
				  <th>Right</th>
				</tr>
			      </thead>
			      
			      <tbody>
				%%contentRights%%
			      </tbody>
			      
			    </table>
			  </div>
			</div>
			
			
			<br>
			<br>
			<br>
			
			<div class='fill-screen' style="text-align:center"> 
			<!--<div class='image-container' style="text-align:center"> -->
                                <img class='make-it-fit' src= "%%img%%" alt="graph"> 
                	</div>

			</body>
			</html>"""

		
	html = html.replace("%%img%%", img)
	html = html.replace("%%contentUsr%%", contentUsr)
	html = html.replace("%%contentRights%%", contentRights)
	return html

	
def html_func(filename:str)->None:
	"""
		function to create html file from data.
		input:
			filename - path of the file
		output:
			file .html
	"""
	dataUsr = read_file_windows("{}/csv_users.csv".format(filename))
	dataRights = read_file_windows("{}/csv_rights.csv".format(filename))
	img = "{}/clustering.png".format(filename)
	
	x = generate_html(img, dataUsr, dataRights) # Change file path,
	write_file_html("./summary.html".format(filename), x)	
	return None



