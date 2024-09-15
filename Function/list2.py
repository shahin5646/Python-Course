""" 
Simulate printing each design, until none are left.     Move each design to completed_models after printing. """

def print_models(unprinted_models,completed_models):
    while unprinted_models:
        current_models=unprinted_models.pop()
        print('Printing Model: '+current_models)
        completed_models.append(current_models)
        
def show_model(completed_models):
    print('The following Model will bw printed: ')
    
    for model in completed_models:
        print(completed_models)
        
        
unprinted_models=['Faruk','Onik','Fuad']
completed_models=[]

print_models(unprinted_models,completed_models)