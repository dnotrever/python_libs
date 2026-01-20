### Install

```
pip install -e ~/workspace/personal/python_libs/helpers
```

### Importing

```
from helpers import echo
```

#### echo

```
echo('Hello, $2[World] !', 'default, success', 'tb')
echo('Hello, $2[World], $3[welcome] !', 'info, success, error', 'tb')
```

#### execute

```
execute('git pull', capture=True, show=True)
```
