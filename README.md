# python-sherpas
Charla de la pycon 2017

Slides: https://docs.google.com/presentation/d/1iAUi3eB15tifetwll2ritBHkAEBVS1gOQYgOePEBJEk/edit?usp=sharing

# Environment:
```
docker build . -t sherpas
docker run -v $PWD:/sherpas -it sherpas /bin/bash
alias pyclean='find . -name "*.pyc" -exec rm -rf {} \; && find . -name "*.so" -exec rm -rf {} \; && find . -name "*.c" -exec rm -rf {} \; && find . -name "*.pyo" -exec rm -rf {} \;'

```
Note: due to a current bug in sharedbuffers you can't install cython, chorde and sharedbuffers using
`pip install -r` you need to install chython and chorde first and then install sharedbuffers

build
```
python setup.py build_ext --inplace
```

```
import timeit
from examples.cython import std_dev as s
from examples.cython import std_dev_cython as sc
from examples.cython import std_dev_pure as scp

timeit.timeit('scp.std_dev(a)', setup='from __main__ import s, sc, scp; a=[v for v in range(1000000)]', number=100)
timeit.timeit('sc.std_dev(a)', setup='from __main__ import s, sc, scp; a=[v for v in range(1000000)]', number=100)
timeit.timeit('s.std_dev(a)', setup='from __main__ import s, sc, scp; a=[v for v in range(1000000)]', number=100)
```

