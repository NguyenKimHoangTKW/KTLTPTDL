from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Chuẩn bị dữ liệu
so_bao_danh = ["123456", "234567", "345678", "456789"]
thong_tin_thisinh = [
    "Thí sinh có số báo danh 123456 đã đạt điểm cao.",
    "Số báo danh 234567 tương ứng với thí sinh đáng chú ý.",
    "345678 là số báo danh của một thí sinh khác.",
    "456789 là số báo danh cuối cùng trong danh sách."
]

# Xây dựng ma trận TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(thong_tin_thisinh)

# Tìm kiếm số báo danh
def tim_kiem_so_bao_danh(so_bao_danh, vectorizer, tfidf_matrix):
    query_vector = vectorizer.transform([so_bao_danh])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_idx = similarities.argmax()
    most_similar_text = thong_tin_thisinh[most_similar_idx]
    return most_similar_text

# Thực hiện tìm kiếm
so_bao_danh_can_tim = "456789"
ket_qua = tim_kiem_so_bao_danh(so_bao_danh_can_tim, vectorizer, tfidf_matrix)
print("Kết quả tìm kiếm cho số báo danh {}: {}".format(so_bao_danh_can_tim, ket_qua))
