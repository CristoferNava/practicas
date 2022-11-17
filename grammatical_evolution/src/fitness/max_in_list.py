from fitness.base_ff_classes.base_ff import base_ff
import random
import time
def generate_list():
    """Generates 10 random integers between 0, and some number between 10 and 100."""
    return [random.randint(0, round(random.random() * 90 + 10, 0)) for _ in range(9)]

class max_in_list(base_ff):
    def __init__(self):
        super().__init__()

    def evaluate(self, ind, **kwargs):
        """The evaluate() method of a fitness function contains the code that is used to directly evaluate
        the phenotype string of an individual and return an appropriate fitness value."""
        p = ind.phenotype
        print(f"\n{p}")

        fitness = 0

        for trial in range(50):
            self.test_list = generate_list()
            m = max(self.test_list)

            d = {"test_list": self.test_list}

            try:
                t0 = time.time()
                exec(p, d)
                t1 = time.time()

                guess = d["return_val"]

                fitness += len(p)
                # print(f"fitness: {fitness}")
                v = abs(m - guess)
                if v <= 10**6:
                    fitness += v
                else:
                    fitness = self.default_fitness
                    break
                if t1 - t0 < 10:
                    fitness = self.default_fitness
                    break
                else:
                    fitness += (t1 - t0) * 1_000

            except:
                fitness = self.default_fitness
                break
        return fitness


