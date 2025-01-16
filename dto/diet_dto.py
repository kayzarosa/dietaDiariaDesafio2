def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "date_time": self.date_time,
        "is_within_the_diet": self.is_within_the_diet,
    }
