# Experiments in Casbin Config with Python

## What is this?
Experiments in using casbin configuration using model (`.conf`) and policy (`.csv`) files.

### Includes
- a basic policy
- a role-based (RBAC) policy that includes a way of assigning open access via a `*` to indicate "any user".


## Requires
- Python
- Python casbin package, installed using `pip install casbin` . Although confusingly `pycasbin` also seems to be a thing. Two options: https://pypi.org/project/casbin/ and https://pypi.org/project/pycasbin/. `pycasbin` might work as well.