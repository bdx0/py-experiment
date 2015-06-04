# https://gist.github.com/huyng/35033eda747313460fad
import pickle
import gzip
import theano
import theano.tensor as T
import numpy as np
import pylab as P
 
# load the dataset
with gzip.open('mnist.pkl.gz', 'rb') as fh:
    train_set, valid_set, test_set = pickle.load(fh)
 
trn_x, trn_y = train_set
tst_x, tst_y = test_set
vld_x, vld_y = valid_set
 
n_feats = trn_x.shape[1]
 
# hyperparams
reg = 0.01
learning_rate = 0.01
max_epochs = 100000
batch_size = 100
 
 
w = theano.shared(np.random.randn(n_feats), name="w")
b = theano.shared(0.0, name="b")
 
b.get_value()
w.get_value()
 
x = T.dmatrix('x')
y = T.dvector('y')
p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))
h = p_1 > 0.5
loss_xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1)
cost = loss_xent.mean() + reg * (w**2).sum()
gw, gb = T.grad(cost, [w,b])
learner = theano.function(
            inputs=[x,y],
            outputs=[h, cost],
            updates=[
                (w, w - learning_rate*gw),
                (b, b - learning_rate*gb)
            ]
          )
 
 
# training
epochs = 0
trn_costs = []
tst_costs = []
print "training ..."
while epochs < max_epochs:
    start = (epochs*batch_size) % trn_x.shape[0]
    stop = start + batch_size
    batch_x = trn_x[start:stop]
    batch_y = (trn_y[start:stop] == 1)*1
    preds, c = learner(batch_x, batch_y)
    epochs += 1
 
    if epochs % 200 == 0:
        trn_costs.append(c)
        d = cost.eval({
            x: tst_x,
            y: (tst_y == 1) * 1
        })
        tst_costs.append(d)
 
    print("trn_cost=%s" % c)
 
P.clf()
P.plot(trn_costs)
P.plot(tst_costs)