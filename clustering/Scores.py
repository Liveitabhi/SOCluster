import os
import pandas as pd
import dataframe_image as dfi

join = os.path.join

path = join(os.getcwd(), 'js_python')

score_10k = {}
score_20k = {}
score_30k = {}
score_40k = {}
score_50k = {}

thresholds = [0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85,0.90]

def get_scores(score_dict, folder):
    sh_score = []
    ch_score = []
    db_score = []
    for result in sorted(os.listdir(join(path, folder))):
        with open(join(path, folder, result)) as f:
            score = f.readlines()
            for line in score:
                if line.startswith('Evaluation Score SH'):
                    sh_score.append(float(line.split(':')[1]))
                elif line.startswith('Evaluation Score CH'):
                    ch_score.append(float(line.split(':')[1]))
                elif line.startswith('Evaluation Score DB'):
                    db_score.append(float(line.split(':')[1]))

    score_dict['sh'] = sh_score
    score_dict['ch'] = ch_score
    score_dict['db'] = db_score

for folder in os.listdir(path):
    if folder.startswith('10k'):
        get_scores(score_10k, folder)
    elif folder.startswith('20k'):
        get_scores(score_20k, folder)
    # elif folder.startswith('30k'):
    #     get_scores(score_30k, folder)
    # elif folder.startswith('40k'):
    #     get_scores(score_40k, folder)
    # elif folder.startswith('50k'):
    #     get_scores(score_50k, folder)

import matplotlib.pyplot as plt
import numpy as np

def plot_scores(score_dict, title):
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.xlabel('Threshold')
    plt.ylabel('Evaluation Score')
    plt.xticks(thresholds)
    plt.plot(thresholds, score_dict['sh'], label='SH')
    plt.plot(thresholds, score_dict['ch'], label='CH')
    plt.plot(thresholds, score_dict['db'], label='DB')
    plt.legend()
    # Save
    plt.savefig(join(os.getcwd(), title + '.png'))

plot_scores(score_10k, '10k')
plot_scores(score_20k, '20k')
# plot_scores(score_30k, '30k')
# plot_scores(score_40k, '40k')
# plot_scores(score_50k, '50k')

# Make subplots for all the scores
fig, axs = plt.subplots(5, 1, figsize=(10, 20))
fig.suptitle('Evaluation Scores for different thresholds')
axs[0].plot(thresholds, score_10k['sh'], label='SH')
axs[0].plot(thresholds, score_10k['ch'], label='CH')
axs[0].plot(thresholds, score_10k['db'], label='DB')
axs[0].set_title('10k')
axs[1].plot(thresholds, score_20k['sh'], label='SH')
axs[1].plot(thresholds, score_20k['ch'], label='CH')
axs[1].plot(thresholds, score_20k['db'], label='DB')
axs[1].set_title('20k')
# axs[2].plot(thresholds, score_30k['sh'], label='SH')
# axs[2].plot(thresholds, score_30k['ch'], label='CH')
# axs[2].plot(thresholds, score_30k['db'], label='DB')
# axs[2].set_title('30k')
# axs[3].plot(thresholds, score_40k['sh'], label='SH')
# axs[3].plot(thresholds, score_40k['ch'], label='CH')
# axs[3].plot(thresholds, score_40k['db'], label='DB')
# axs[3].set_title('40k')
# axs[4].plot(thresholds, score_50k['sh'], label='SH')
# axs[4].plot(thresholds, score_50k['ch'], label='CH')
# axs[4].plot(thresholds, score_50k['db'], label='DB')
# axs[4].set_title('50k')
for ax in axs.flat:
    ax.set(xlabel='Threshold', ylabel='Evaluation Score')
    ax.label_outer()
    ax.set_xticks(thresholds)
    ax.legend()
# Save
plt.savefig(join(os.getcwd(), 'all_scores.png'))


# Make a dataframe for each 10k, 20k, 30k, 40k, 50k
# df_10k = pd.DataFrame(score_10k, index=thresholds)
# df_20k = pd.DataFrame(score_20k, index=thresholds)
# df_30k = pd.DataFrame(score_30k, index=thresholds)
# df_40k = pd.DataFrame(score_40k, index=thresholds)
# df_50k = pd.DataFrame(score_50k, index=thresholds)

# Save the dataframes as images
# dfi.export(df_10k,'df_10.png',table_conversion='matplotlib')
# dfi.export(df_20k,'df_20.png',table_conversion='matplotlib')
# dfi.export(df_30k,'df_30.png',table_conversion='matplotlib')
# dfi.export(df_40k,'df_40.png',table_conversion='matplotlib')
# dfi.export(df_50k,'df_50.png',table_conversion='matplotlib')
# fig = df2img.plot_dataframe(df_10k)
# df2img.save_dataframe(fig=fig, filename='10k_df.png')
