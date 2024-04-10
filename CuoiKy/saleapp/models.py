from saleapp import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Cumthi(db.Model):
    __tablename__ = 'cumthi' 

    macumthi = db.Column(db.String(20), primary_key=True)
    tencumthi = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Cumthi(Macumthi={self.macumthi}, tencumthi='{self.tencumthi}')"

class Thongtinthisinh(db.Model):
    __tablename__ = 'dblthongtinthisinh' 

    sbd = db.Column(db.String(20), primary_key=True)
    macumthi = db.Column(db.String(20), db.ForeignKey('cumthi.macumthi'))
    toan = db.Column(db.Float)
    nguvan = db.Column(db.Float)
    ngoaingu = db.Column(db.Float)
    vatly = db.Column(db.Float)
    hoahoc = db.Column(db.Float)
    sinhhoc = db.Column(db.Float)
    lichsu = db.Column(db.Float)
    dialy = db.Column(db.Float)
    gdcd = db.Column(db.Float)
    diemtb = db.Column(db.Float)
    urlweb = db.Column(db.String(255))

    cumthi = db.relationship('Cumthi')

    def __repr__(self):
        return f"<Thongtinthisinh(sdb='{self.sdb}', macumthi='{self.macumthi}', toan='{self.toan}', nguvan='{self.nguvan}', ngoaingu='{self.ngoaingu}', vatly='{self.vatly}', hoahoc='{self.hoahoc}', sinhhoc='{self.sinhhoc}', lichsu='{self.lichsu}', dialy='{self.dialy}', gdcd='{self.gdcd}', diemtb='{self.diemtb}', urlweb='{self.urlweb}')>"
