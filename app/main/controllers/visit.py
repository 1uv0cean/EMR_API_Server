from sqlalchemy import func
from flask_restx import Resource, Api, Namespace, fields
import json
from app.main import db

visit = Namespace(
    name = "Visit",
    description= "방문자 수에 대한 통계",
)

count_visitor= visit.model('count_all',{
     'visit_count': fields.String(
          description='전체 방문자 수', 
          required=True, 
          example='1234'
          )
})

def rep(data):
     data = data.replace("(","").replace(")","").replace(",","")
     return data


@visit.route("/count-visitor")
class personCount(Resource):
     @visit.expect(count_visitor)
     def get(self):
          """전체 방문자 수를 반환합니다"""
          visit_count = db.engine.execute('SELECT COUNT(*) FROM visit_occurrence')
          row = visit_count.first()
          return {
               "visit_count":str(row[0])
          }

