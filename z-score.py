
import pandas as pd
import numpy as np
import scipy.stats as stats

data = np.array([6, 7, 7, 12, 13, 4, 15, 16, 19, 4200])

z_data = stats.zscore(data, nan_policy='omit', ddof=0)
z_data


plt.figure(figsize=(10,7), dpi= 80)
# sns.distplot(Z_data, color="dodgerblue", label="Compact", **kwargs)
sns.distplot(Z_data, color="dodgerblue", label="Compact",
    bins=None,
    hist=False,
    kde=True,
    rug=True,
    fit=None,
    hist_kws=None,
    kde_kws=None,
    rug_kws=None,
    fit_kws=None,
    vertical=False,
    norm_hist=None,
    axlabel=None,
    ax=None,
            )
    
plt.xlim(-5,5)
plt.legend();
