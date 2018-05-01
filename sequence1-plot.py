import sys
sys.path.append('python')

import stats
import stats.plot

data=stats.reader.Reader('Sequence1')

plot=stats.plot.Time(data.time-0.02,width=6,height=6,border_left=0.8,time_range=(0,0.32),color=False)

buf=data.get('state.buffer_vocab',keys=['A','B','C','D','E','F','G','H'],normalize=True)
plot.add('Working Memory (Similarity)',buf,linewidth=2)

gpi=data.get('BG.GPi_spikes')
gpi=gpi[:,:100*8]  # only use first 800 neurons (the rest are for other actions)

plot.add_spikes('Actions',gpi,sample=400,contrast_scale=0.5,yticks=['A','B','C','D','E','F','G','H'],style='image')
   # sample: show this many neurons (by choosing the most active neurons from among neighbours)
   # merge: combine neurons down to this many rows
   # style: can be 'image', 'box', or 'dot'
   # cluster: True/False flag to group neurons by similarity
   # contrast_scale: smaller values make the spikes darker

plot.save('sequence1-plot.pdf')
plot.show()

