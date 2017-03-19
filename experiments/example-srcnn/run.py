"""Example experiment."""
from functools import partial

from toolbox.data import load_set
from toolbox.models import compile
from toolbox.models import srcnn
from toolbox.experiment import SRCNNExperiment


# Model
scale = 3
model = compile(srcnn(c=1, f1=9, f2=1, f3=5, n1=64, n2=32))
model.summary()

# Data
train_set = '91-image'
val_set = 'Set5'
test_sets = ['Set5', 'Set14']
load_set = partial(load_set, sub_size=20, sub_stride=100, scale=scale)

# Training
experiment = SRCNNExperiment(scale=scale, model=model, load_set=load_set,
                             save_dir='.')
experiment.train(train_set=train_set, val_set=val_set, epochs=2, resume=True)

# Evaluation
for test_set in test_sets:
    experiment.test(test_set=test_set)