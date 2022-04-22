

# Function to return a list of model fields
def get_modelfieldlist(model, *kwars):
    all_fields = []
    all_fields = get_fields(model)

    # get a list of all next models passed
    for relational_model in kwars:
        # function bellow return model name
        # model_name = get_model_name(relational_model)
        secondary_model = get_fields(
            relational_model, is_relational_model=True)

        all_fields.extend(secondary_model)

    return all_fields


# get all model fiels
def get_fields(model, is_relational_model=False):
    field_values = []
    model_name = get_model_name(model)
    for field in model._meta.get_fields():
        if is_relational_model:
            field_values.append(f'{model_name}__{field.name}')
        else:
            field_values.append(f'{field.name}')

    if is_relational_model:
        # remove the first value of list due to alway this is the hidden relation pk
        del field_values[0]

    return field_values

# get model name


def get_model_name(model):
    # line bellow get the name of model, convert is a lower and add
    # the letter s in order get the name of relational field
    model_name = f'{(str(model._meta.model.__name__).lower())}s'
    return model_name
