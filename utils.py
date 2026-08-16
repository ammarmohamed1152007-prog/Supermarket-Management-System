class IDGenerator:
    counters = {}

    @classmethod
    def generate_id(cls, prefix):
        if prefix not in cls.counters:
            cls.counters[prefix] = 1
        else:
            cls.counters[prefix] += 1
        return f"{prefix.upper()}{cls.counters[prefix]}"    