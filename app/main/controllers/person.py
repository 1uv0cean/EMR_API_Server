from sqlalchemy import func
from flask_restx import Resource, Api, Namespace, fields
import json
from app.main import db

person = Namespace(
    name = "Person",
    description= "환자 수에 대한 통계",
)

count_all= person.model('count_all',{
     'person_count': fields.String(
          description='전체 환자 수', 
          required=True, 
          example='1234'
          )
})

count_gender= person.model('count_gender',{
     'female_count': fields.String(
          description='여성 환자 수', 
          required=True, 
          example='600'
          ),
     'male_count': fields.String(
          description='남성 환자 수', 
          required=True, 
          example='523'
          )
})

table_person = db.Table('t_person', db.MetaData())
Chars = "(),"

@person.route("/count-all")
class personCount(Resource):
     @person.expect(count_all)
     def get(self):
          """전체 환자 수를 반환합니다"""
          person_count = db.engine.execute('SELECT COUNT(*) FROM person')
          row = person_count.first()
          return {
               "person_count":str(row[0])
          }

@person.route("/count-gender")
class personCount(Resource):
     @person.expect(count_gender)
     def get(self):
          """성별 환자 수를 반환합니다"""
          female = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY gender_source_value = 'F';")
          male = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY gender_source_value = 'M';")
          frow = female.first()
          mrow = male.first()
          return {
               "female_count": str(frow[0]),
               "male_count": str(mrow[0])
          }
