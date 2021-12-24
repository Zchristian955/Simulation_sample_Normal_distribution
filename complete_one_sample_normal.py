def random_normal1(p):
    import pandas as pd
    import numpy as np
    from numpy.random import normal
    import math
    import scipy.stats as st
    l = []
    u=p-1
    k = [[] for _ in range(u)]

    k.append([])
    #l.append([])
    o=range(p)
    f = math.sqrt(2)

    for i in o:
        j=normal(loc=-1.2, scale=f, size=20)
        k[i].append(j)
        h=np.mean(k[i])
        sd=np.std(k[i])
        ci=st.norm.interval(alpha=0.90, loc=h, scale=sd)
        l.append(ci)
    df_table = pd.DataFrame(list(zip(k, l)), columns=['sample', 'confidence'])
    print(k)
    print()
    print(df_table)






