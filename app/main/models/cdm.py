from app.main import db, app

cdm = app.config["SCHEMA_CDM"]

t_person = db.Table(
    'person',
    db.Column("person_id"),
    db.Column("gender_concept_id"),
    db.Column("birth_datetime"),
    db.Column("race_concept_id"),
    db.Column("ethnicity_concept_id"),
    schema=cdm,
    extend_existing=True
)

t_visit_occurrence = db.Table(
    'visit_occurrence',
    db.Column("visit_occurrence_id"),
    db.Column("person_id"),
    db.Column("visit_concept_id"),
    db.Column("visit_start_datetime"),
    db.Column("visit_end_datetime"),
    schema=cdm,
    extend_existing=True
)

t_condition_occurrence = db.Table(
    'condition_occurrence',
    db.Column("person_id"),
    db.Column("condition_concept_id"),
    db.Column("condition_start_datetime"),
    db.Column("condition_end_datetime"),
    db.Column("visit_occurrence_id"),
    schema=cdm,
    extend_existing=True
)

t_drug_exposure = db.Table(
    'drug_exposure',
    db.Column("person_id"),
    db.Column("drug_concept_id"),
    db.Column("drug_exposure_start_datetime"),
    db.Column("drug_exposure_end_datetime"),
    db.Column("visit_occurrence_id"),
    schema=cdm,
    extend_existing=True
)

t_concept = db.Table(
    'concept',
    db.Column("concept_id"),
    db.Column("concept_name"),
    db.Column("domain_id"),
    schema=cdm,
    extend_existing=True
)

t_death = db.Table(
    'death',
    db.Column("person_id"),
    db.Column("death_date"),
    schema=cdm,
    extend_existing=True
)