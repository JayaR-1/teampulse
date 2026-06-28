# TeamPulse — Sprint Model
# This is the foundation of everything we build

class Sprint:

    def __init__(self, id, planned, done):
        self.id = id
        self.planned = planned
        self.done = done

    def velocity(self):
        if self.planned == 0:
            return 0
        return round(self.done / self.planned * 100, 1)

    def status(self):
        if self.velocity() >= 90:
            return "On Track"
        elif self.velocity() >= 75:
            return "At Risk"
        else:
            return "Critical"

    def __str__(self):
        return f"Sprint {self.id}: {self.velocity()}% — {self.status()}"

