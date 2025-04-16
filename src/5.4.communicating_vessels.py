class CommunicatingVessels:
    def interleave(self, a: list, b: list) -> list:
        return [val for pair in zip(a, b) for val in pair]

communicating_vessels = CommunicatingVessels()
