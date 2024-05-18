


def cal_sim():
    import numpy as np

def cosine_similarity(vector1, vector2):
    # 计算两个向量的点积
    dot_product = np.dot(vector1, vector2)
    
    # 计算两个向量的范数（即向量的长度）
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    
    # 计算余弦相似度
    cosine_sim = dot_product / (norm_vector1 * norm_vector2)
    
    return cosine_sim

# 示例向量
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# 计算并打印余弦相似度
similarity = cosine_similarity(vector1, vector2)
print(f"Cosine Similarity: {similarity}")





def main():


if __name__ == "__main__":
    main()
