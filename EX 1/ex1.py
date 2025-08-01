def mcp_neuron(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    output = 1 if total_input >= threshold else 0
    return output

# AND Gate using MCP neuron
def AND_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=2)

# OR Gate using MCP neuron
def OR_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=1)

# NOT Gate using MCP neuron (only one input)
def NOT_gate(x):
    return mcp_neuron([x], [-1], threshold=0)

# Test all gates
print("AND Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {AND_gate(x1, x2)}")

print("\nOR Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} OR {x2} = {OR_gate(x1, x2)}")

print("\nNOT Gate:")
for x in [0, 1]:
    print(f"NOT {x} = {NOT_gate(x)}")
def mcp_neuron(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    output = 1 if total_input >= threshold else 0
    return output

# AND Gate using MCP neuron
def AND_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=2)

# OR Gate using MCP neuron
def OR_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=1)

# NOT Gate using MCP neuron (only one input)
def NOT_gate(x):
    return mcp_neuron([x], [-1], threshold=0)

# Test all gates
print("AND Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {AND_gate(x1, x2)}")

print("\nOR Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} OR {x2} = {OR_gate(x1, x2)}")

print("\nNOT Gate:")
for x in [0, 1]:
    print(f"NOT {x} = {NOT_gate(x)}")
def mcp_neuron(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    output = 1 if total_input >= threshold else 0
    return output

# AND Gate using MCP neuron
def AND_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=2)

# OR Gate using MCP neuron
def OR_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=1)

# NOT Gate using MCP neuron (only one input)
def NOT_gate(x):
    return mcp_neuron([x], [-1], threshold=0)

# Test all gates
print("AND Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {AND_gate(x1, x2)}")

print("\nOR Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} OR {x2} = {OR_gate(x1, x2)}")

print("\nNOT Gate:")
for x in [0, 1]:
    print(f"NOT {x} = {NOT_gate(x)}")
def mcp_neuron(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    output = 1 if total_input >= threshold else 0
    return output

# AND Gate using MCP neuron
def AND_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=2)

# OR Gate using MCP neuron
def OR_gate(x1, x2):
    return mcp_neuron([x1, x2], [1, 1], threshold=1)

# NOT Gate using MCP neuron (only one input)
def NOT_gate(x):
    return mcp_neuron([x], [-1], threshold=0)

# Test all gates
print("AND Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {AND_gate(x1, x2)}")

print("\nOR Gate:")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} OR {x2} = {OR_gate(x1, x2)}")

print("\nNOT Gate:")
for x in [0, 1]:
    print(f"NOT {x} = {NOT_gate(x)}")
