from flask import Flask, render_template, request
from saleapp import app
import utils
import math

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/viewdata")
def View_Data():
    page = request.args.get('page', 1)
    page = int(page)
    cumthis = Cumthi.query.all()
    
    selected_cumthi = request.args.get('cumthi', None)
    
    if selected_cumthi:
        cates = utils.load_thongtin_by_selected_cumthi(selected_cumthi, page=page)
        count = len(cates)
    else:
        count = utils.count_thongtinthisinh()
        cates = utils.load_thongtin(page=page)
    total_data_count = utils.get_total_data_count()
    return render_template('viewdata.html', Thongtinthisinh=cates, cumthis=cumthis, pages=math.ceil(count/app.config['PAGE_SIZE']), page=page,total_data_count=total_data_count)

@app.route("/searchdata")
def View_Search_Data():
    page = request.args.get('page', 1)
    page = int(page)
    cumthis = Cumthi.query.all()
    
    selected_cumthi = request.args.get('cumthi', None)
    
    if selected_cumthi:
        cates = utils.load_thongtin_by_selected_cumthi(selected_cumthi, page=page)
        count = len(cates)
    else:
        count = utils.count_thongtinthisinh()
        cates = utils.load_thongtin(page=page)

    total_data_count = utils.get_total_data_count()
    return render_template('searchdata.html', Thongtinthisinh=cates, cumthis=cumthis, pages=math.ceil(count/app.config['PAGE_SIZE']), page=page,total_data_count=total_data_count)

@app.route("/viewcumthi")
def View_Data_CumThi():
    page = request.args.get('page', 1)
    page = int(page)
    count = utils.count_cumthi()
    cates = utils.load_cumthi(page=page)
    total_datacumthi_count = utils.get_total_datacumthi_count()
    return render_template('viewcumthi.html',Cumthi=cates, pages=math.ceil(count/app.config['PAGE_SIZE']), page=page,total_datacumthi_count=total_datacumthi_count)

@app.route("/search", methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if keyword:
        search_results = utils.search_thongtinthisinh(keyword)
        return render_template('search_result.html', keyword=keyword, search_results=search_results)
    else:
        return render_template('search_result.html', keyword=keyword, search_results=[])

if __name__=='__main__':
    from saleapp.admin import *
    app.run(debug=True)
