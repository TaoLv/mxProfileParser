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
_copy           2855.707  ms    27.1972095238   ms/call         105  calls
Convolution     29936.515 ms    3.03308156028   ms/call         9870 calls
Pooling         4265.345  ms    2.9015952381    ms/call         1470 calls
SoftmaxOutput   8.093     ms    0.0770761904762 ms/call         105  calls
Activation      6724.473  ms    0.681304255319  ms/call         9870 calls
BatchNorm       10322.554 ms    1.0458514691    ms/call         9870 calls
FullyConnected  253.268   ms    2.41207619048   ms/call         105  calls
Concat          3792.917  ms    3.28391082251   ms/call         1155 calls
Flatten         36.932    ms    0.351733333333  ms/call         105  calls

Total OP Time: 58195.80400000 ms
```
### Specify the operator name which you want to parse.
```
$ python mxProfileParser.py --file demo.json --op BatchNorm
Time of BatchNorm:
BatchNorm       10322.554 ms    1.0458514691    ms/call         9870 calls
```
### Specify the # of iteration if you know the exact number
```
$ python mxProfileParser.py --file demo.json --iterations 105
Time of each OP:
_copy           2855.707  ms    27.1972095238   ms/call         105  calls      1    calls/iter
Convolution     29936.515 ms    3.03308156028   ms/call         9870 calls      94   calls/iter
Pooling         4265.345  ms    2.9015952381    ms/call         1470 calls      14   calls/iter
SoftmaxOutput   8.093     ms    0.0770761904762 ms/call         105  calls      1    calls/iter
Activation      6724.473  ms    0.681304255319  ms/call         9870 calls      94   calls/iter
BatchNorm       10322.554 ms    1.0458514691    ms/call         9870 calls      94   calls/iter
FullyConnected  253.268   ms    2.41207619048   ms/call         105  calls      1    calls/iter
Concat          3792.917  ms    3.28391082251   ms/call         1155 calls      11   calls/iter
Flatten         36.932    ms    0.351733333333  ms/call         105  calls      1    calls/iter

Total OP Time: 58195.80400000 ms
Iteration Time: 554.24575238 ms
```
  * First column are operator names. Second column are the total execution time of each operator. Third column are the average execution time of each operator. Third column are the number of calls of each operator. The last column are the number of calls in one iteration.
