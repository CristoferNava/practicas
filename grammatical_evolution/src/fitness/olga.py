from fitness.base_ff_classes.base_ff import base_ff

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


class olga(base_ff):
    def __init__(self):
        super().__init__()

    def evaluate(self, ind, **kwargs):
        """The evaluate() method of a fitness function contains the code that is used to directly evaluate
        the phenotype string of an individual and return an appropriate fitness value."""
        p = ind.phenotype
        print(p)

        fitness = 0

        for trial in range(50):
            try:
                pass
            except:
                pass

            # self.test_list = generate_list()
            # m = max(self.test_list)

            # d = {"test_list": self.test_list}
            #
            # try:
            #     t0 = time.time()
            #     exec(p, d)
            #     t1 = time.time()
            #
            #     guess = d["return_val"]
            #
            #     fitness += len(p)
            #     # print(f"fitness: {fitness}")
            #     v = abs(m - guess)
            #     if v <= 10**6:
            #         fitness += v
            #     else:
            #         fitness = self.default_fitness
            #         break
            #     if t1 - t0 < 10:
            #         fitness = self.default_fitness
            #         break
            #     else:
            #         fitness += (t1 - t0) * 1_000
            #
            # except:
            #     fitness = self.default_fitness
            #     break
        # print(min_value, max_value)
        return fitness


