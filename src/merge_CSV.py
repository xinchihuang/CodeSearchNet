import pandas as pd
frames=[]
for language in ('python','go', 'javascript', 'java', 'php', 'ruby'):
    path='model_predictions_{}.csv'.format(language)
    df=pd.read_csv(path)
    frames.append(df)
new_df=pd.concat(frames)
new_df.to_csv('model_predictions.csv',index=False)