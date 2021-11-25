# data font = https://www.kaggle.com/laotse/credit-risk-dataset
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# %%
# LOAN AMOUNT Inicial Valores
base_credit = pd.read_csv('C:\Code\ds\credit_risk_dataset.csv')
base_credit # DEFAULTED

# %%
base_credit.describe()

# %%
# LOAN AMOUNT Max
base_credit[base_credit['loan_amnt'] >= 35000]

# %%
# LOAN AMOUNT Min
base_credit[base_credit['loan_amnt'] <= 500]

# %%
# Graphics 
np.unique(base_credit['cb_person_default_on_file'], return_counts=True)


# %%
# Yes/No loyal clients
sns.countplot(x = base_credit['cb_person_default_on_file']);

# %%
# Age Graphics
plt.hist(x = base_credit['person_age']);

# %%
plt.hist(x = base_credit['loan_amnt']);

# %%
graphic = px.scatter_matrix(base_credit, dimensions=['person_age', 'person_income', 'loan_amnt'], color = 'cb_person_default_on_file')
graphic.show()


