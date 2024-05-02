from saleapp import app
from saleapp.models import Cumthi, Thongtinthisinh
from flask import session
import math

def load_thongtin(page=1):
    thong_tin_thisinh = Thongtinthisinh.query.all()
    for thisinh in thong_tin_thisinh:
        cumthi = Cumthi.query.filter_by(macumthi=thisinh.macumthi).first()
        if cumthi:
            thisinh.TenCumThi = cumthi.tencumthi
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size
    return thong_tin_thisinh[start:end]

def load_cumthi(page=1):
    cum_thi = Cumthi.query.all()
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size
    return cum_thi[start:end]
def get_total_data_count():
    total_count = Thongtinthisinh.query.count()
    return total_count

def get_total_datacumthi_count():
    total_count = Cumthi.query.count()
    return total_count
def search_thongtinthisinh(keyword):
    search_result = Thongtinthisinh.query.filter_by(sbd=keyword).all()
    for thisinh in search_result:
        cumthi = Cumthi.query.filter_by(macumthi=thisinh.macumthi).first()
        if cumthi:
            thisinh.TenCumThi = cumthi.tencumthi
    return search_result
def count_cumthi():
    return Cumthi.query.count()

def count_thongtinthisinh():
    return Thongtinthisinh.query.count()


