def get_neuron_connections(neuron_connections: str) -> list[str]:
    """Given a neuron connections returns an array defining all its connections."""
    inputs, outputs = neuron_connections.split("#")
    inputs_connections = inputs.split("/")
    outputs_connections = outputs.split("/")
    connections = [*inputs_connections, *outputs_connections]
    return connections


def get_tables_from_topology(topology: str):
    pos = len(topology) - 1
    while topology[pos] != "/":
        pos -= 1

    while topology[pos] != "i":
        pos += 1

    hidden_layer = topology[:pos]
    output_layer = topology[pos:]

    hidden_layer_neurons = hidden_layer.split("_")
    output_layer_neurons = output_layer.split("_")

    first_table = {}
    for idx, neuron in enumerate(hidden_layer_neurons):
        key = f"h{idx}"
        first_table[key] = get_neuron_connections(neuron)

    second_table = {}
    for idx, neuron in enumerate(output_layer_neurons, start=1):
        key = f"o{idx}"
        second_table[key] = [neuron]

    return first_table, second_table


s = "i4,+5566.8/i0,-9390.0#o2,-679.02/o1,-67.459/o3,+8623.122_i2,+5.0099/i0,9.9999#o2,+9.000_i3,+2.4/i2,-3.89999/i0,-1.99#o2,-9.9/o3,+9.9944_i4,-285.0/i2,+77.8247/i0,+7.231#o2,78113.54/o1,+39.6_i2,-1.0/i0,-3.0#o3,+999.9_i3,-8.50/i0,+41.9#o3,-18.0/o2,+9.99i0,-9.9_i0,-4.9_i0,-5.40"
result = get_tables_from_topology(s)

first_table, second_table = result
print(first_table)
print()
print(second_table)

"""
{'h0': ['i4,+5566.8', 'i0,-9390.0', 'o2,-679.02', 'o1,-67.459', 'o3,+8623.122'],
 'h1': ['i2,+5.0099', 'i0,9.9999', 'o2,+9.000'],
 'h2': ['i3,+2.4', 'i2,-3.89999', 'i0,-1.99', 'o2,-9.9', 'o3,+9.9944'],
 'h3': ['i4,-285.0', 'i2,+77.8247', 'i0,+7.231', 'o2,78113.54', 'o1,+39.6'],
 'h4': ['i2,-1.0', 'i0,-3.0', 'o3,+999.9'],
 'h5': ['i3,-8.50', 'i0,+41.9', 'o3,-18.0', 'o2,+9.99']
 }



{'o1': ['i0,-9.9'],
 'o2': ['i0,-4.9'],
 'o3': ['i0,-5.40']
 }
 """