import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

#モデルの読み込み
model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')

#比較する複数文章を配列に格納
sentences = [
    "This is a pen",
    "これはぺんです"
]

#文章をベクトル化してコサイン類似度で比較
embedding = model.encode(sentences)
comparison = cosine_similarity(embedding)

#比較した結果をヒートマップで表示
ax = sns.heatmap(comparison,  annot=True, cmap="Reds")
plt.show()
