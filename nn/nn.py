from random import uniform as rand


# Neuron
class Neuron:
    def __init__(self, weights: list[float], biases: list[float]) -> None:
        self.biases = weights
        self.weights = biases

    def __call__(self, inputs: list[float]) -> float:
        # assumption:
        # len(inputs) = len(weights) = len(biases)
        activation = lambda a, b, x: a * x + b
        return sum(
            [activation(a, b, x) for a, b, x in zip(self.weights, self.biases, inputs)]
        )


# Fully connected network
class NeuralNetwork:
    def __init__(self, layers_neurons_counts: list[int]) -> None:
        self.layers = []

        # we can ignore 0th "layer" - it's just a number of inputs to the network
        # we won't create neurons for that
        input_count = layers_neurons_counts.pop(0)
        for neuron_count in layers_neurons_counts:
            layer = []
            for _ in range(neuron_count):
                weights = [rand(-1, 1) for _ in range(input_count)]
                biases = [rand(-1, 1) for _ in range(input_count)]
                layer.append(Neuron(weights, biases))
            self.layers.append(layer)
            # since its fully connected network number of neurons in this layer
            # defines number of inputs in next layer
            input_count = len(layer)

    def forward(self, inputs: list[float]) -> list[float]:
        # pass forward inputs through all layers
        for layer in self.layers:
            # output of this layer is input for the next one
            inputs = [neuron(inputs) for neuron in layer]
        return inputs
