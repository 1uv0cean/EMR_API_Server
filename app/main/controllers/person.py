from sqlalchemy import func
from flask_restx import Resource, Namespace, fields
from app.main import db
from app.main.models.cdm import t_person, t_death

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
          example='623'
          ),
     'male_count': fields.String(
          description='남성 환자 수', 
          required=True, 
          example='600'
          )
})

count_race= person.model('count_race',{
     'white_count': fields.String(
          description='백인 환자 수', 
          required=True, 
          example='423'
          ),
     'black_count': fields.String(
          description='흑인 환자 수', 
          required=True, 
          example='400'
          ),
     'asian_count': fields.String(
          description='아시아인 환자 수', 
          required=True, 
          example='400'
          ),
     'native_count': fields.String(
          description='아메리카 원주민 환자 수', 
          required=True, 
          example='400'
          )
})

count_death= person.model('count_death',{
     'death_count': fields.String(
          description='사망자 수', 
          required=True, 
          example='12'
          )
})

def rep(data):
     data = data.replace("(","").replace(")","").replace(",","")
     return data


@person.route("/count-all")
class personCount(Resource):
     @person.expect(count_all)
     def get(self):
          """전체 환자 수를 반환합니다"""
          return {
               "person_count": db.session.query(t_person).count()
          }

@person.route("/count-death")
class personCount(Resource):
     @person.expect(count_death)
     def get(self):
          """사망자 수를 반환합니다"""
          return {
               "death_count" : db.session.query(t_death).count()
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

@person.route("/count-race")
class personCount(Resource):
     @person.expect(count_race)
     def get(self):
          """인종별 환자 수를 반환합니다"""
          white = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY race_source_value = 'white';")
          black = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY race_source_value = 'black';")
          asian = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY race_source_value = 'asian';")
          native = db.engine.execute("SELECT COUNT(*) FROM person GROUP BY race_source_value = 'native';")
          
          wrow = white.fetchall()  
          brow = black.fetchall()
          arow = asian.fetchall()
          nrow = native.fetchall()
          
          return {
               "white_count": rep(str(wrow[1])),
               "black_count": rep(str(brow[1])),
               "asian_count": rep(str(arow[1])),
               "native_count": rep(str(nrow[1]))
          }

