import casbin

enforcer = casbin.Enforcer("basic_model.conf", "basic_policy.csv")
policy = enforcer.get_policy()
print(f"Permitted activities:\n{policy}")

attempts= [("amy", "files", "read"),
           ("amy", "files", "write"),
           ("amy", "files", "delete"),
           ("amy", "secrets", "read"),
           ("bob", "files", "read"),
           ("bob", "files", "write"),
           ("baddie", "files", "read")
           ]

print("\nAttempts")
for attempt in attempts:
    if enforcer.enforce(*attempt):
        print(f"{attempt} - Allowed")
    else:
        print(f"{attempt} - Denied")
