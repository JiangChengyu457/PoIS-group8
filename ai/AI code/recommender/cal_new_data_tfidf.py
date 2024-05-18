from Preprocessing import Tfidf_Vectorization
import numpy as np
import pandas as pd

def main():
    # read_data
    df = pd.DataFrame(columns=['text'])
    df.text = pd.DataFrame(content_set)
    Tfidf_Vectorization.Tfidf_Vectorization(df)
    # 存入数据库

if __name__ == "__main__":
    main()
