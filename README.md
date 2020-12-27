## introduction

A tensorflow implement dsfd, and there is something different with the origal paper.

The evaluation results are based on vgg with batchsize(2x6),pretrained model can be download from

## requirment

- tensorflow1.12

- tensorpack (for data provider)

- opencv

- python 3.6

## useage

### evaluation

** fddb **

```
    python model_eval/fddb.py [--model [TRAINED_MODEL]] [--data_dir [DATA_DIR]]
                          [--split_dir [SPLIT_DIR]] [--result [RESULT_DIR]]
    --model              Path of the saved model,default ./model/detector.pb
    --data_dir           Path of fddb all images
    --split_dir          Path of fddb folds
    --result             Path to save fddb results
```

example `python model_eval/fddb.py --model model/detector.pb --data_dir 'fddb/img/' --split_dir fddb/FDDB-folds/ --result 'result/' `

** widerface **

```
    python model_eval/wider.py [--model [TRAINED_MODEL]] [--data_dir [DATA_DIR]]
                           [--result [RESULT_DIR]]
    --model              Path of the saved model,default ./model/detector.pb
    --data_dir           Path of WIDER
    --result             Path to save WIDERface results
```

example `python model_eval/wider.py --model model/detector.pb --data_dir 'WIDER/WIDER_val/' --result 'result/' `

### visualization

![A demo](https://github.com/610265158/DSFD-tensorflow/blob/master/figures/res_screenshot_11.05.2019.png)

if u get a trained model, run `python tools/auto_freeze.py`, it will read the checkpoint file in ./model, and produce detector.pb, then

`python vis.py`

u can check th code in vis.py to make it runable, it's simple.

### details

#### anchor

if u like to show the anchor stratergy, u could simply run :

`python lib/core/anchor/anchor.py`

it will draw the anchor one by one,

### References

[DSFD: Dual Shot Face Detector](https://arxiv.org/abs/1810.10220?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+arxiv%2FQSXk+%28ExcitingAds%21+cs+updates+on+arXiv.org%29)
