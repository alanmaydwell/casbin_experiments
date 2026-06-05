import casbin

enforcer = casbin.Enforcer("rbac_model.conf", "rbac_policy.csv")
policy = enforcer.get_policy()
print(f"Role definitions:\n{policy}")

print("User's roles")
for user in ("amy", "bob", "baddie", "cat", "*"):
    print(f"{user} {enforcer.get_roles_for_user(user)}")


attempts= [("amy", "files", "read"),
           ("amy", "files", "write"),
           ("amy", "files", "delete"),
           ("amy", "files", "info"),
           ("amy", "secrets", "read"),
           ("bob", "files", "read"),
           ("bob", "files", "write"),
           ("bob", "files", "scan"),
           ("baddie", "files", "read"),
           ("baddie", "files", "info"),
           ("cat", "files", "info"),
           ("cat", "files", "delete"),
           ("cat", "files", "read"),
           ]

print("\nAttempts")
for attempt in attempts:
    if enforcer.enforce(*attempt):
        print(f"{attempt} - Allowed")
    else:
        print(f"{attempt} - Denied")
