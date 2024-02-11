from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CoursEau(db.Model):
    __tablename__ = "cours_eau"
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(45), nullable=False)
    longueur = db.Column(db.Integer, nullable=True)
    typeid = db.Column(db.Integer, db.ForeignKey('type_cours_eau.id'), nullable=False)
    derniere_crue_majeur = db.Column(db.DateTime, nullable=True)

    affluences = db.relationship('Affluence', foreign_keys='Affluence.affluent', backref='affluent_cours_eau', lazy=True)
    effluences = db.relationship('Affluence', foreign_keys='Affluence.effluent', backref='effluent_cours_eau', lazy=True)
    traverses = db.relationship('Traverse', backref='cours_eau', lazy=True)
    type_cours_eau = db.relationship('TypeCoursEau', backref='cours_eaux', lazy=True)

    def __repr__(self):
        return f"<CoursEau(id={self.id}, denomination={self.denomination}, longueur={self.longueur}, typeid={self.typeid})>"

class Affluence(db.Model):
    __tablename__ = "affluence"
    affluent = db.Column(db.Integer, db.ForeignKey('cours_eau.id'), primary_key=True, nullable=False)
    effluent = db.Column(db.Integer, db.ForeignKey('cours_eau.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f"<Affluence(affluent={self.affluent}, effluent={self.effluent})>"

class TypeCoursEau(db.Model):
    __tablename__ = "type_cours_eau"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text, nullable=True)

    cours_eaux = db.relationship('CoursEau', backref='type_cours_eau', lazy=True)

    def __repr__(self):
        return f"<TypeCoursEau(id={self.id}, label={self.label})>"

class Traverse(db.Model):
    __tablename__ = "traverse"
    id = db.Column(db.Integer, primary_key=True)
    CoursEau = db.Column(db.Integer, db.ForeignKey('cours_eau.id'), nullable=False)
    sousDivision = db.Column(db.Integer, db.ForeignKey('sous_division_geographique.id'), nullable=False)

    def __repr__(self):
        return f"<Traverse(id={self.id}, CoursEau={self.CoursEau}, sousDivision={self.sousDivision})>"

class SousDivisionGeographique(db.Model):
    __tablename__ = "sous_division_geographique"
    id = db.Column(db.Integer, primary_key=True)
    pays = db.Column(db.Integer, db.ForeignKey('pays.id'), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    denomination = db.Column(db.String(45), nullable=False)
    code_officiel = db.Column(db.String(12), nullable=True)

    traverses = db.relationship('Traverse', backref='sous_division_geographique', lazy=True)
    type_sous_division = db.relationship('TypeSousDivision', backref='sous_divisions', lazy=True)

    def __repr__(self):
        return f"<SousDivisionGeographique(id={self.id}, pays={self.pays}, type_sous_division={self.type_sous_division})>"

class TypeSousDivision(db.Model):
    __tablename__ = "type_sous_division"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text, nullable=True)

    sous_divisions = db.relationship('SousDivisionGeographique', backref='type_sous_division', lazy=True)

    def __repr__(self):
        return f"<TypeSousDivision(id={self.id}, label={self.label})>"

class Pays(db.Model):
    __tablename__ = "pays"
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(45), nullable=False)

    sous_divisions_geographiques = db.relationship('SousDivisionGeographique', backref='pays', lazy=True)

    def __repr__(self):
        return f"<Pays(id={self.id}, denomination={self.denomination})>"
