# Application Programming Interface used to facilitate communication between two or more systems

# RESTful API: Concept where the communicating systems(client/server) should not know their underlying architecture(how they were developed)

# E-commerce - client
# safaricom mpesa - server

#  API server can be developed by any backed technology: e.g pythonflask, django, javascript(nodejs), php(laravel), java(springboot)

# The API can be consumed(used) by any fronted e.  Android(kotlin), flask-boostrap, javascript(reactJS) , angularJS, vUEjs....),iOS(flutter/swift)

#  flask(python) <-> restful api<-> android(kotlin) -> FullStack



from flask import *
from flask_restful import Api, Resource

import pymysql 
from pymysql import cursors

app = Flask(__name__)

# cHANGE THE FLASK APP TO RUN A RESTFUL API
api = Api(app)

# Create a resource and specifying the methods e.g Employee, Department, Salaries

class Farmer(Resource):




    def get(self):
        connection = pymysql.connect(host = 'localhost',user='root',password='',database = 'kifaruApiDB')
        cursor = connection.cursor(cursors.DictCursor)

        sql = 'select *from farmers'

        cursor.execute(sql)
        if cursor.rowcount == 0 :
              return jsonify({"message":"No records found"})
        else:
              Farmers = cursor.fetchall()
              return jsonify(Farmers)
        


    def post(self):
              
        data = request.json

        farmers_id=data['farmers_id']
        farmers_name = data['famers_name']
        farmers_location = data['farmers_location']
        earnings = data['earnings']
        
        connection = pymysql.connect(host = 'localhost',user='root',password='',database = 'kifaruApiDB')

        try:
                    sql = 'insert into employees(farmers_id,farmers_name,farmers_location,earnings) values (%s,%s,%s,%s)'
                    cursor = connection.cursor()
                    cursor.execute(sql,(farmers_id,farmers_name,farmers_location,earnings))
                    connection.commit()
                    return jsonify({"message":"New Farmer Posted successfully"})

        except:
             connection.rollback()
             return jsonify({"message":"Internal Server Error"})
        
    def put(self):
        data = request.json
        farmers_id = data['farmers_id']
        earnings= data['earnings']

        connection = pymysql.connect(host = 'localhost',user='root',password='',database = 'kifaruApiDB')

        cursor =connection.cursor()

        sql ='update farmers set earnings == %s where farmers_id == $s '
        try:
              cursor.execute(sql,(earnings, farmers_id))
              connection.commit()
              return jsonify({"message":f"Farmer of id {farmers_id} salary updated successfully"})
        
        except:
              connection.rollback()
              return jsonify({"message":"Server Error"})
              

        
    

    def delete(self):
        return jsonify({"message": "Accessing the DELETE method"})
    
      




api.add_resource(Farmers, '/farmers')

app.run(debug=True)