# maRig

Maya Rigging Utility using Mel and Python

# Rig Library

## Utils

### Create Controls

Joint Orient Axis for controls

- Aim Axis (Y)
- Up Axis (X)
- World Up Axis (Z)

#### Create your first control

```python
from utils.controls import control_create

Control = control_create.Contorl()
# Control object
control_1 = Control.create(name="base",
                           scale=1.4,
                           type="Square",
                           suffix="_ctrl",
                           thickness="2.0",
                           parent="group1",
                           color=10)
```

_Parameter_
`@param name: str, name of the controller, @default: control`
`@param type: str, shape of the controller, @default: circle`
`@param scale: float, scale of the controller, @default: 1.0`
`@param suffix: str, contoller suffix, @default: "_ctrl"`
`@param color: int, controller color index, @default: 21`
`@param thickness: float, thickness of the controller, @default: 1`
`@param parent: str, parent of the current locator, @default: None`
`@param return: str, controller`
