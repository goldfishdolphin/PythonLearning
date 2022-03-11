sandwich_orders = ['tuna', 'cheese', 'egg','chicken']
finished_sandwiches = []

while sandwich_orders:
    finished_order = sandwich_orders.pop()
    finished_sandwiches.append(finished_order)

for sandwich in finished_sandwiches:
    print(f"\nYour {sandwich} sandwich is ready. ")
