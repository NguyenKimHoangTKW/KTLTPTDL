from saleapp import app,db
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from saleapp.models import Cumthi,Thongtinthisinh
admin = Admin(app=app,name="E-commerce Administration", template_mode='bootstrap4')
class ThongTinView(ModelView):
    can_view_details = True
admin.add_view(ModelView(Cumthi,db.session))
admin.add_view(ThongTinView(Thongtinthisinh,db.session))