from flask import Flask, render_template, request
import csv 
import random

app=Flask(__name__)
done=set()
name=""
reg=""
filename = "student.csv"
lim=0
exh=""

with open("student.csv") as tempf: lim=len(tempf.read().split("\n"))

lim-=1
totalstu=lim
currstu=0

print("for list of "+str(lim)+" students")

@app.route("/")
def main():
  
   name="Press button"
   reg="00000"

   templateData = {   
      'name' : name,
      'reg' : reg,
      'total' : totalstu,
      'current' : currstu,
      'exh' : exh
      }

   return render_template('main.html', **templateData)


@app.route("/<action>")
def action(action):
   global currstu
   global totalstu
   global lim
   global exh



   name="..."
   reg="..."

   print("still "+str(lim))
   if action == "generate":
      with open(filename) as csvfile:
         readCSV= csv.reader(csvfile, delimiter=',')

         randno=random.randint(1,lim)
         for row in readCSV:
               if (int(row[0]) == randno and not row[0] in done) :
                     name=row[2]
                     reg=row[1]
                     currstu += 1
                     done.add(row[0])    
   
   
   
   if (currstu == totalstu):
      exh="LIST EXHAUSTED"
      name="(x_x)"
      reg="-/-"

   templateData = {   
      'name' : name,
      'reg' : reg,
      'total' : totalstu,
      'current' : currstu,
      'exh' : exh
      }


   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)
