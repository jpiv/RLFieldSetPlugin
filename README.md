# RLFieldSetPlugin
Rocket League bakkesmod plugin and python module for setting field state. 

## Installation
1) Copy `FieldSetPlugin.dll` to `bakkesmod/plugins` directory
2) Edit `bakkesmod/cfg/plugins.cfg` and add line `plugin load fieldsetplugin`

## Examples:
```
from field_set import FieldSet
import rlgym

env = rlgym.make("default")
field_set = FieldSet()

while True:
    obs = env.reset()
    field_set.randomize_ball_state()
    done = False

    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample()
      
      next_obs, reward, done, gameinfo = env.step(action)
      
      obs = next_obs
```

