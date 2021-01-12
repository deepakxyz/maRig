# maRig

Maya Rigging Utility using Mel and Python

# Rig Library

## Utils

### Create Controls

```python
from utils.controls import control_create

control = control_create.Control()
# Custom control
baseCtrl = control.create(name="base",
                           scale=1.4,
                           type="Square",
                           suffix="_ctrl",
                           thickness="2.0",
                           parent="group1",
                           color=10)
```

Return, type - control (object)
