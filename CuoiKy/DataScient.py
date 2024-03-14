import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_scores(student_code):
    url = f"https://diemthi.vnexpress.net/index/detail/sbd/{student_code}/year/2023"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    parents = soup.find_all("div", {"class": "o-detail-thisinh__diemthi"})
    if parents:
        elements = parents[0].find_all("tbody")
        result = elements[0].find_all("tr")
        scores = {"Mã học sinh": student_code}
        for item in result:
            column = item.find_all("td") 
            subject = column[0].get_text()
            score = column[1].get_text(strip=True)
            scores[subject] = score
        return scores
    else:
        print("Không tìm thấy kết quả cho mã học sinh:", student_code)
        return None

start_code = 1000001
end_code = 1000101

all_scores = []

with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_student_code = {executor.submit(fetch_scores, f"{student_code:08d}"): student_code for student_code in range(start_code, end_code+1)}
    for future in as_completed(future_to_student_code):
        student_code = future_to_student_code[future]
        try:
            scores = future.result()
            if scores:
                all_scores.append(scores)
                print(scores)
        except Exception as e:
            print(f"Yêu cầu cho mã học sinh {student_code} thất bại: {e}")

#df = pd.DataFrame(all_scores)

#df.to_excel("diem_thi.xlsx", index=False)
