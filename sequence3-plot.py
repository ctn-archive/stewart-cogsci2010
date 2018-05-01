import sys
sys.path.append('python')

import stats
import stats.plot

data=stats.reader.Reader('Sequence3')

plot=stats.plot.Time(data.time-0.02,width=6,height=6,border_left=0.8,time_range=(0,0.32),color=False)

buf=data.get('state.buffer_vocab',keys=['F','G','H','II','J','K','L','M'],normalize=True)
plot.add('Working Memory (Similarity)',buf,linewidth=2,range=(-0.3,1))

gpi=data.get('BG.GPi_spikes')

plot.add_spikes('Actions',gpi,sample=700,contrast_scale=0.5,yticks=['A','B','C','D','E','F','G','H','I','J','K','L','M','look'],style='image')
   # sample: show this many neurons (by choosing the most active neurons from among neighbours)
   # merge: combine neurons down to this many rows
   # style: can be 'image', 'box', or 'dot'
   # cluster: True/False flag to group neurons by similarity
   # contrast_scale: smaller values make the spikes darker

plot.save('sequence3-plot.pdf')
plot.show()

