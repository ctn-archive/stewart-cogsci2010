from spa import *

D=32

class Rules:
    def start(state='START'):
        set(state='A')
    def A(state='A'):
        set(state='B')
    def B(state='B'):
        set(state='C')
    def C(state='C'):
        set(state='D')
    def D(state='D'):
        set(state='E')
    def E(state='E'):
        set(state='F')
    def F(state='F'):
        set(state='G')
    def G(state='G'):
        set(state='H')
    def H(state='H'):
        set(state='II')
    def II(state='II'):
        set(state='J')
    def J(state='J'):
        set(state='K')
    def K(state='K'):
        set(state='L')
    def L(state='L'):
        set(state='M')        
    def M(state='M'):
        set(state='A')
"""        
    def N(state='N'):
        set(state='O')
    def O(state='O'):
        set(state='P')
    def P(state='P'):
        set(state='Q')
    def Q(state='Q'):
        set(state='R')
    def R(state='R'):
        set(state='S')
    def S(state='S'):
        set(state='T')
    def T(state='T'):
        set(state='U')
    def U(state='U'):
        set(state='V')
    def V(state='V'):
        set(state='W')
    def W(state='W'):
        set(state='X')
    def X(state='X'):
        set(state='Y')
    def Y(state='Y'):
        set(state='Z')
    def Z(state='Z'):
        set(state='A')
"""    


class Sequence1(SPA):
    dimensions=D
    align_hrrs=True
    
    state=Buffer()
    BG=BasalGanglia(Rules(),same_neurons=False)
    thal=Thalamus(BG,pstc_output=0.002)    
    input=Input(0.02,state='START')

seq=Sequence1()
log=seq.net.log()
log.add_vocab('state.buffer',threshold=None)
log.add_spikes('BG.GPi')
seq.net.run(0.4)
