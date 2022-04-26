def print_models(unprinted_design, completed_models):
    '''
    Stimutlate printing each design, untill none is left.
    Move each design to completed_models after printing.
    '''

    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    '''
    Show all the models that were printed.
    '''
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

'''print_models(unprinted_design, completed_models)
show_completed_models(completed_models)'''