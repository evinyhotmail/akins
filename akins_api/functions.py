import json

# Function to return


def get_modelfieldlist(self):
    field_values = []
    for field in self._meta.get_fields():
        # here get the value of the named attribute of the object
        field_name = str(getattr(self, field.name, ''))
        field_values.append(f'{field.name}:{field_name}')

   # remove the first element [Drone] due to is not used.
    del field_values[0]

    return ', '.join(field_values)
