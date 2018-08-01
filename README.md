# mxProfileParser
A simple tool for parsing the profile.json file of mxnet
### Enable mxnet profiler with environment variables
```
export MXNET_EXEC_BULK_EXEC_INFERENCE=0
export MXNET_EXEC_BULK_EXEC_TRAIN=0
export MXNET_PROFILER_AUTOSTART=1
```
### Specify the json file. The tool will load `profile.json` by default
```
$ python mxProfileParser.py --file demo.json
Time of each OP:
Convolution     10563.795 ms    13.2877924528  ms/call  795 calls       58.63 %
elemwise_add    3119.924  ms    12.9996833333  ms/call  240 calls       17.32 %
BatchNorm       2406.835  ms    3.14618954248  ms/call  765 calls       13.36 %
Activation      1383.968  ms    1.84529066667  ms/call  750 calls       7.68 %
FullyConnected  200.596   ms    13.3730666667  ms/call  15  calls       1.11 %
_copy           198.52    ms    13.2346666667  ms/call  15  calls       1.10 %
Pooling         136.808   ms    4.56026666667  ms/call  30  calls       0.76 %
Flatten         4.969     ms    0.331266666667 ms/call  15  calls       0.03 %
SoftmaxOutput   1.724     ms    0.114933333333 ms/call  15  calls       0.01 %

Total OP Time: 18017.13900000 ms
```
### Specify the operator name which you want to parse.
```
$ python mxProfileParser.py --file demo.json --op BatchNorm
Time of BatchNorm:
BatchNorm       2406.835  ms    3.14618954248  ms/call  765 calls       13.36 %
```
### Specify the # of iteration if you know the exact number
```
$ python mxProfileParser.py --file demo.json --iterations 15
Time of each OP:
Convolution     10563.795 ms    13.2877924528  ms/call  795 calls       53   calls/iter         58.63 %
elemwise_add    3119.924  ms    12.9996833333  ms/call  240 calls       16   calls/iter         17.32 %
BatchNorm       2406.835  ms    3.14618954248  ms/call  765 calls       51   calls/iter         13.36 %
Activation      1383.968  ms    1.84529066667  ms/call  750 calls       50   calls/iter         7.68 %
FullyConnected  200.596   ms    13.3730666667  ms/call  15  calls       1    calls/iter         1.11 %
_copy           198.52    ms    13.2346666667  ms/call  15  calls       1    calls/iter         1.10 %
Pooling         136.808   ms    4.56026666667  ms/call  30  calls       2    calls/iter         0.76 %
Flatten         4.969     ms    0.331266666667 ms/call  15  calls       1    calls/iter         0.03 %
SoftmaxOutput   1.724     ms    0.114933333333 ms/call  15  calls       1    calls/iter         0.01 %

Total OP Time: 18017.13900000 ms
Iteration Time: 1201.14260000 ms
```
  * First column are operator names. Second column are the total execution time of each operator. Third column are the average execution time of each operator. Third column are the number of calls of each operator. The last column are the number of calls in one iteration.
